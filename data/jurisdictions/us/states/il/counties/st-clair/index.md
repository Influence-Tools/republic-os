---
type: Jurisdiction
title: "St. Clair County, IL"
classification: county
fips: "17163"
state: "IL"
demographics:
  population: 253694
  population_under_18: 58413
  population_18_64: 151274
  population_65_plus: 44007
  median_household_income: 73854
  poverty_rate: 13.58
  homeownership_rate: 68.44
  unemployment_rate: 5.96
  median_home_value: 180300
  gini_index: 0.452
  vacancy_rate: 12.79
  race_white: 152523
  race_black: 70726
  race_asian: 4174
  race_native: 642
  hispanic: 12858
  bachelors_plus: 79633
districts:
  - to: "us/states/il/districts/12"
    rel: in-district
    area_weight: 0.791
  - to: "us/states/il/districts/13"
    rel: in-district
    area_weight: 0.209
  - to: "us/states/il/districts/senate/57"
    rel: in-district
    area_weight: 0.7672
  - to: "us/states/il/districts/senate/58"
    rel: in-district
    area_weight: 0.0995
  - to: "us/states/il/districts/senate/55"
    rel: in-district
    area_weight: 0.08
  - to: "us/states/il/districts/senate/56"
    rel: in-district
    area_weight: 0.0532
  - to: "us/states/il/districts/house/114"
    rel: in-district
    area_weight: 0.6409
  - to: "us/states/il/districts/house/113"
    rel: in-district
    area_weight: 0.1263
  - to: "us/states/il/districts/house/115"
    rel: in-district
    area_weight: 0.0995
  - to: "us/states/il/districts/house/109"
    rel: in-district
    area_weight: 0.08
  - to: "us/states/il/districts/house/112"
    rel: in-district
    area_weight: 0.0532
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# St. Clair County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 253694 |
| Under 18 | 58413 |
| 18–64 | 151274 |
| 65+ | 44007 |
| Median household income | 73854 |
| Poverty rate | 13.58 |
| Homeownership rate | 68.44 |
| Unemployment rate | 5.96 |
| Median home value | 180300 |
| Gini index | 0.452 |
| Vacancy rate | 12.79 |
| White | 152523 |
| Black | 70726 |
| Asian | 4174 |
| Native | 642 |
| Hispanic/Latino | 12858 |
| Bachelor's or higher | 79633 |

## Districts

- [IL-12](/us/states/il/districts/12.md) — 79% (congressional)
- [IL-13](/us/states/il/districts/13.md) — 21% (congressional)
- [IL Senate District 57](/us/states/il/districts/senate/57.md) — 77% (state senate)
- [IL Senate District 58](/us/states/il/districts/senate/58.md) — 10% (state senate)
- [IL Senate District 55](/us/states/il/districts/senate/55.md) — 8% (state senate)
- [IL Senate District 56](/us/states/il/districts/senate/56.md) — 5% (state senate)
- [IL House District 114](/us/states/il/districts/house/114.md) — 64% (state house)
- [IL House District 113](/us/states/il/districts/house/113.md) — 13% (state house)
- [IL House District 115](/us/states/il/districts/house/115.md) — 10% (state house)
- [IL House District 109](/us/states/il/districts/house/109.md) — 8% (state house)
- [IL House District 112](/us/states/il/districts/house/112.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
