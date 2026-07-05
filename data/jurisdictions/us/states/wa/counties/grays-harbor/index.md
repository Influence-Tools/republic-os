---
type: Jurisdiction
title: "Grays Harbor County, WA"
classification: county
fips: "53027"
state: "WA"
demographics:
  population: 77053
  population_under_18: 15217
  population_18_64: 43856
  population_65_plus: 17980
  median_household_income: 64414
  poverty_rate: 15.31
  homeownership_rate: 73.21
  unemployment_rate: 7.01
  median_home_value: 314000
  gini_index: 0.4358
  vacancy_rate: 17.15
  race_white: 60470
  race_black: 1137
  race_asian: 1037
  race_native: 3240
  hispanic: 8617
  bachelors_plus: 13656
districts:
  - to: "us/states/wa/districts/06"
    rel: in-district
    area_weight: 0.8706
  - to: "us/states/wa/districts/senate/24"
    rel: in-district
    area_weight: 0.613
  - to: "us/states/wa/districts/senate/19"
    rel: in-district
    area_weight: 0.2575
  - to: "us/states/wa/districts/house/24"
    rel: in-district
    area_weight: 0.613
  - to: "us/states/wa/districts/house/19"
    rel: in-district
    area_weight: 0.2575
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wa]
timestamp: "2026-07-03"
---

# Grays Harbor County, WA

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 77053 |
| Under 18 | 15217 |
| 18–64 | 43856 |
| 65+ | 17980 |
| Median household income | 64414 |
| Poverty rate | 15.31 |
| Homeownership rate | 73.21 |
| Unemployment rate | 7.01 |
| Median home value | 314000 |
| Gini index | 0.4358 |
| Vacancy rate | 17.15 |
| White | 60470 |
| Black | 1137 |
| Asian | 1037 |
| Native | 3240 |
| Hispanic/Latino | 8617 |
| Bachelor's or higher | 13656 |

## Districts

- [WA-06](/us/states/wa/districts/06.md) — 87% (congressional)
- [WA Senate District 24](/us/states/wa/districts/senate/24.md) — 61% (state senate)
- [WA Senate District 19](/us/states/wa/districts/senate/19.md) — 26% (state senate)
- [WA House District 24](/us/states/wa/districts/house/24.md) — 61% (state house)
- [WA House District 19](/us/states/wa/districts/house/19.md) — 26% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
