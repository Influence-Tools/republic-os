#!/usr/bin/env python3
"""Ingest a pinned OLRC U.S. Code XML title into Republic OS legal files.

This is intentionally mechanical:
  official ZIP -> raw snapshot -> section Markdown -> manifest/checksums

No summaries, relationship extraction, or interpretation happen here. The raw
archive is preserved so any normalized output can be audited against source.
"""

import argparse
import hashlib
import json
import re
import shutil
import urllib.request
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

REPO = Path(__file__).resolve().parent.parent
RAW_ROOT = REPO / "data" / "legal" / "raw" / "us" / "code"
MANIFEST_ROOT = REPO / "data" / "legal" / "manifests"
CHECKSUM_ROOT = REPO / "data" / "legal" / "checksums"
LEGAL_ROOT = REPO / "legal" / "us" / "code"

USLM_NS = "http://xml.house.gov/schemas/uslm/1.0"
NS = {"u": USLM_NS, "dc": "http://purl.org/dc/elements/1.1/"}

DEFAULT_RELEASE = "119-100"
DEFAULT_PUBLIC_LAW_CONGRESS = "119"
DEFAULT_PUBLIC_LAW_NUMBER = "100"
DEFAULT_RELEASE_DATE = "2026-06-26"
DEFAULT_RETRIEVED_AT = "2026-07-04"


def tag_name(elem):
    return elem.tag.rsplit("}", 1)[-1]


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sha256_text(text):
    return sha256_bytes(text.encode("utf-8"))


def yval(value):
    if value is None:
        return '""'
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, list):
        return "[" + ", ".join(yval(v) for v in value) + "]"
    return json.dumps(str(value), ensure_ascii=False)


def clean_text(text):
    text = text or ""
    text = text.replace("\u2000", " ")
    text = text.replace("\u202f", " ")
    text = re.sub(r"[ \t\r\n]+", " ", text)
    return text.strip()


def child_text(elem, name):
    child = elem.find(f"u:{name}", NS)
    if child is None:
        return ""
    return clean_text("".join(child.itertext()))


def direct_child(elem, name):
    for child in list(elem):
        if tag_name(child) == name:
            return child
    return None


def local_text(elem):
    parts = []
    if elem.text:
        parts.append(elem.text)
    for child in list(elem):
        if child.tail:
            parts.append(child.tail)
    return clean_text(" ".join(parts))


def render_node(elem, depth=0):
    name = tag_name(elem)

    if name in {"num", "heading"}:
        return []

    if name in {"content", "chapeau", "continuation", "p"}:
        text = clean_text("".join(elem.itertext()))
        return [text] if text else []

    if name in {"note", "sourceCredit"}:
        text = clean_text("".join(elem.itertext()))
        return [text] if text else []

    label_bits = []
    num = direct_child(elem, "num")
    heading = direct_child(elem, "heading")
    if num is not None:
        label_bits.append(clean_text("".join(num.itertext())))
    if heading is not None:
        label_bits.append(clean_text("".join(heading.itertext())))
    label = " ".join(bit for bit in label_bits if bit)

    child_lines = []
    for child in list(elem):
        if tag_name(child) in {"num", "heading", "notes"}:
            continue
        child_lines.extend(render_node(child, depth + 1))

    lines = []
    body = local_text(elem)
    if label and body:
        lines.append(f"{label} {body}")
    elif label and child_lines:
        lines.append(f"{label} {child_lines[0]}")
        lines.extend(child_lines[1:])
    elif label:
        lines.append(label)
    elif body:
        lines.append(body)
    else:
        lines.extend(child_lines)

    return [line for line in lines if line]


def render_section(section):
    lines = []
    notes = []
    for child in list(section):
        if tag_name(child) in {"num", "heading"}:
            continue
        if tag_name(child) == "notes":
            for note in child.findall(".//u:note", NS):
                notes.extend(render_node(note))
            continue
        lines.extend(render_node(child))

    rendered = []
    if lines:
        rendered.append("## Text\n\n" + "\n\n".join(lines))
    if notes:
        rendered.append("## Notes\n\n" + "\n\n".join(notes))
    return "\n\n".join(rendered).strip() + "\n"


def slugify(value):
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return re.sub(r"-{2,}", "-", value) or "unnamed"


def source_url(public_law_congress, public_law_number, title, release):
    return (
        "https://uscode.house.gov/download/releasepoints/us/pl/"
        f"{public_law_congress}/{public_law_number}/xml_usc{title:02d}@{release}.zip"
    )


def download(url):
    with urllib.request.urlopen(url) as response:
        return response.read()


def extract_title_xml(zip_path):
    with zipfile.ZipFile(zip_path) as zf:
        names = sorted(name for name in zf.namelist() if name.endswith(".xml"))
        if len(names) != 1:
            raise ValueError(f"expected exactly one XML file in {zip_path}, found {names}")
        with zf.open(names[0]) as fh:
            return names[0], fh.read()


def parent_map(root):
    return {child: parent for parent in root.iter() for child in list(parent)}


def nearest_ancestor(elem, parents, wanted):
    cur = parents.get(elem)
    while cur is not None:
        if tag_name(cur) == wanted:
            return cur
        cur = parents.get(cur)
    return None


def title_metadata(root):
    title = root.find(".//u:main/u:title", NS)
    if title is None:
        raise ValueError("could not find title element")
    return {
        "title_number": int(child_text(title, "num").replace("Title", "").replace("—", "").strip()),
        "title_name": child_text(title, "heading"),
        "source_identifier": title.attrib.get("identifier"),
        "publication_name": child_text(root.find("u:meta", NS), "docPublicationName"),
    }


def section_number(section):
    num = direct_child(section, "num")
    if num is not None and num.attrib.get("value"):
        return num.attrib["value"]
    ident = section.attrib.get("identifier", "")
    return ident.rsplit("/s", 1)[-1]


def iter_code_sections(root):
    pattern = re.compile(r"^/us/usc/t\d+/s[^/]+$")
    for section in root.findall(".//u:section", NS):
        identifier = section.attrib.get("identifier", "")
        if pattern.match(identifier):
            yield section


def write_section(section, parents, meta, args, archive_hash, xml_path):
    number = section_number(section)
    heading = child_text(section, "heading")
    chapter = nearest_ancestor(section, parents, "chapter")
    chapter_number = ""
    chapter_name = ""
    if chapter is not None:
        chapter_number = child_text(chapter, "num").replace("CHAPTER", "").replace("—", "").strip()
        chapter_name = child_text(chapter, "heading")

    body = render_section(section)
    text_hash = sha256_text(body)
    section_xml = ET.tostring(section, encoding="unicode")
    section_hash = sha256_text(section_xml)
    citation = f"{meta['title_number']} U.S.C. § {number}"

    frontmatter = {
        "type": "LegalText",
        "title": citation,
        "description": heading,
        "jurisdiction": "us",
        "corpus": "united_states_code",
        "kind": "code_section",
        "title_number": meta["title_number"],
        "title_name": meta["title_name"],
        "chapter_number": chapter_number,
        "chapter_name": chapter_name,
        "section": number,
        "citation": citation,
        "status": "current",
        "release_point": args.release,
        "release_date": args.release_date,
        "source": "official",
        "source_url": args.source_url,
        "source_identifier": section.attrib.get("identifier"),
        "source_file": str(xml_path.relative_to(REPO)),
        "source_hash": section_hash,
        "raw_snapshot_hash": archive_hash,
        "text_hash": text_hash,
        "retrieved_at": args.retrieved_at,
        "confidence": "official",
        "tags": ["legal", "us-code", "elections"],
    }

    yaml = ["---"]
    for key, value in frontmatter.items():
        yaml.append(f"{key}: {yval(value)}")
    yaml.append("---")
    yaml.append("")
    if heading:
        yaml.append(f"# {citation} - {heading}")
    else:
        yaml.append(f"# {citation}")
    yaml.append("")
    yaml.append(body.rstrip())
    yaml.append("")

    chapter_slug = f"chapter-{chapter_number.lower()}" if chapter_number else "chapter-unknown"
    out = LEGAL_ROOT / f"title-{meta['title_number']:02d}" / chapter_slug / f"section-{slugify(number)}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    content = "\n".join(yaml)
    out.write_text(content, encoding="utf-8")
    return {
        "path": str(out.relative_to(REPO)),
        "citation": citation,
        "section": number,
        "chapter": chapter_number,
        "source_identifier": section.attrib.get("identifier"),
        "source_hash": section_hash,
        "text_hash": text_hash,
        "file_hash": sha256_text(content),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--title", type=int, default=52)
    parser.add_argument("--release", default=DEFAULT_RELEASE)
    parser.add_argument("--public-law-congress", default=DEFAULT_PUBLIC_LAW_CONGRESS)
    parser.add_argument("--public-law-number", default=DEFAULT_PUBLIC_LAW_NUMBER)
    parser.add_argument("--release-date", default=DEFAULT_RELEASE_DATE)
    parser.add_argument("--retrieved-at", default=DEFAULT_RETRIEVED_AT)
    parser.add_argument("--source-url")
    args = parser.parse_args()
    if not args.source_url:
        args.source_url = source_url(
            args.public_law_congress,
            args.public_law_number,
            args.title,
            args.release,
        )

    raw_dir = RAW_ROOT / f"title-{args.title:02d}"
    raw_dir.mkdir(parents=True, exist_ok=True)
    raw_zip = raw_dir / f"xml_usc{args.title:02d}@{args.release}.zip"

    if not raw_zip.exists():
        raw_zip.write_bytes(download(args.source_url))
    archive_bytes = raw_zip.read_bytes()
    archive_hash = sha256_bytes(archive_bytes)

    xml_name, xml_bytes = extract_title_xml(raw_zip)
    raw_xml = raw_dir / xml_name
    raw_xml.write_bytes(xml_bytes)
    root = ET.fromstring(xml_bytes)
    meta = title_metadata(root)
    parents = parent_map(root)

    out_title = LEGAL_ROOT / f"title-{args.title:02d}"
    if out_title.exists():
        shutil.rmtree(out_title)

    files = []
    for section in sorted(iter_code_sections(root), key=lambda s: section_number(s)):
        files.append(write_section(section, parents, meta, args, archive_hash, raw_xml))

    manifest = {
        "type": "LegalManifest",
        "corpus": "united_states_code",
        "jurisdiction": "us",
        "title_number": args.title,
        "title_name": meta["title_name"],
        "release_point": args.release,
        "release_date": args.release_date,
        "retrieved_at": args.retrieved_at,
        "source": "official",
        "source_url": args.source_url,
        "source_file": str(raw_zip.relative_to(REPO)),
        "source_file_sha256": archive_hash,
        "xml_file": str(raw_xml.relative_to(REPO)),
        "xml_file_sha256": sha256_bytes(xml_bytes),
        "section_count": len(files),
        "files": files,
    }

    MANIFEST_ROOT.mkdir(parents=True, exist_ok=True)
    CHECKSUM_ROOT.mkdir(parents=True, exist_ok=True)
    manifest_path = MANIFEST_ROOT / f"us-code-title-{args.title:02d}-{args.release}.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")

    checksum_path = CHECKSUM_ROOT / f"us-code-title-{args.title:02d}-{args.release}.sha256"
    lines = [f"{archive_hash}  {raw_zip.relative_to(REPO)}"]
    lines.append(f"{sha256_bytes(xml_bytes)}  {raw_xml.relative_to(REPO)}")
    for item in files:
        lines.append(f"{item['file_hash']}  {item['path']}")
    checksum_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"ingested {len(files)} U.S. Code sections from Title {args.title}")
    print(f"raw: {raw_zip.relative_to(REPO)}")
    print(f"manifest: {manifest_path.relative_to(REPO)}")
    print(f"checksums: {checksum_path.relative_to(REPO)}")


if __name__ == "__main__":
    main()
