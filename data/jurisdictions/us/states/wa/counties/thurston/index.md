---
type: Jurisdiction
title: "Thurston County, WA"
classification: county
fips: "53067"
state: "WA"
demographics:
  population: 299067
  population_under_18: 62380
  population_18_64: 180615
  population_65_plus: 56072
  median_household_income: 96563
  poverty_rate: 9.55
  homeownership_rate: 67.69
  unemployment_rate: 5.15
  median_home_value: 480300
  gini_index: 0.4025
  vacancy_rate: 5.0
  race_white: 215637
  race_black: 9947
  race_asian: 18347
  race_native: 3375
  hispanic: 31748
  bachelors_plus: 114273
districts:
  - to: "us/states/wa/districts/10"
    rel: in-district
    area_weight: 0.6149
  - to: "us/states/wa/districts/03"
    rel: in-district
    area_weight: 0.3683
  - to: "us/states/wa/districts/senate/35"
    rel: in-district
    area_weight: 0.3994
  - to: "us/states/wa/districts/senate/2"
    rel: in-district
    area_weight: 0.3422
  - to: "us/states/wa/districts/senate/22"
    rel: in-district
    area_weight: 0.155
  - to: "us/states/wa/districts/senate/20"
    rel: in-district
    area_weight: 0.0474
  - to: "us/states/wa/districts/senate/19"
    rel: in-district
    area_weight: 0.0373
  - to: "us/states/wa/districts/house/35"
    rel: in-district
    area_weight: 0.3994
  - to: "us/states/wa/districts/house/2"
    rel: in-district
    area_weight: 0.3422
  - to: "us/states/wa/districts/house/22"
    rel: in-district
    area_weight: 0.155
  - to: "us/states/wa/districts/house/20"
    rel: in-district
    area_weight: 0.0474
  - to: "us/states/wa/districts/house/19"
    rel: in-district
    area_weight: 0.0373
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wa]
timestamp: "2026-07-03"
---

# Thurston County, WA

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 299067 |
| Under 18 | 62380 |
| 18–64 | 180615 |
| 65+ | 56072 |
| Median household income | 96563 |
| Poverty rate | 9.55 |
| Homeownership rate | 67.69 |
| Unemployment rate | 5.15 |
| Median home value | 480300 |
| Gini index | 0.4025 |
| Vacancy rate | 5.0 |
| White | 215637 |
| Black | 9947 |
| Asian | 18347 |
| Native | 3375 |
| Hispanic/Latino | 31748 |
| Bachelor's or higher | 114273 |

## Districts

- [WA-10](/us/states/wa/districts/10.md) — 61% (congressional)
- [WA-03](/us/states/wa/districts/03.md) — 37% (congressional)
- [WA Senate District 35](/us/states/wa/districts/senate/35.md) — 40% (state senate)
- [WA Senate District 2](/us/states/wa/districts/senate/2.md) — 34% (state senate)
- [WA Senate District 22](/us/states/wa/districts/senate/22.md) — 16% (state senate)
- [WA Senate District 20](/us/states/wa/districts/senate/20.md) — 5% (state senate)
- [WA Senate District 19](/us/states/wa/districts/senate/19.md) — 4% (state senate)
- [WA House District 35](/us/states/wa/districts/house/35.md) — 40% (state house)
- [WA House District 2](/us/states/wa/districts/house/2.md) — 34% (state house)
- [WA House District 22](/us/states/wa/districts/house/22.md) — 16% (state house)
- [WA House District 20](/us/states/wa/districts/house/20.md) — 5% (state house)
- [WA House District 19](/us/states/wa/districts/house/19.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
