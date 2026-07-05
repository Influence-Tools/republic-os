---
type: Jurisdiction
title: "Adams County, WA"
classification: county
fips: "53001"
state: "WA"
demographics:
  population: 20800
  population_under_18: 7223
  population_18_64: 11048
  population_65_plus: 2529
  median_household_income: 66136
  poverty_rate: 19.55
  homeownership_rate: 69.31
  unemployment_rate: 3.59
  median_home_value: 273300
  gini_index: 0.4788
  vacancy_rate: 9.21
  race_white: 8932
  race_black: 40
  race_asian: 119
  race_native: 483
  hispanic: 13423
  bachelors_plus: 2398
districts:
  - to: "us/states/wa/districts/05"
    rel: in-district
    area_weight: 0.9293
  - to: "us/states/wa/districts/04"
    rel: in-district
    area_weight: 0.0707
  - to: "us/states/wa/districts/senate/9"
    rel: in-district
    area_weight: 0.9318
  - to: "us/states/wa/districts/senate/13"
    rel: in-district
    area_weight: 0.0681
  - to: "us/states/wa/districts/house/9"
    rel: in-district
    area_weight: 0.9318
  - to: "us/states/wa/districts/house/13"
    rel: in-district
    area_weight: 0.0681
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wa]
timestamp: "2026-07-03"
---

# Adams County, WA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20800 |
| Under 18 | 7223 |
| 18–64 | 11048 |
| 65+ | 2529 |
| Median household income | 66136 |
| Poverty rate | 19.55 |
| Homeownership rate | 69.31 |
| Unemployment rate | 3.59 |
| Median home value | 273300 |
| Gini index | 0.4788 |
| Vacancy rate | 9.21 |
| White | 8932 |
| Black | 40 |
| Asian | 119 |
| Native | 483 |
| Hispanic/Latino | 13423 |
| Bachelor's or higher | 2398 |

## Districts

- [WA-05](/us/states/wa/districts/05.md) — 93% (congressional)
- [WA-04](/us/states/wa/districts/04.md) — 7% (congressional)
- [WA Senate District 9](/us/states/wa/districts/senate/9.md) — 93% (state senate)
- [WA Senate District 13](/us/states/wa/districts/senate/13.md) — 7% (state senate)
- [WA House District 9](/us/states/wa/districts/house/9.md) — 93% (state house)
- [WA House District 13](/us/states/wa/districts/house/13.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
