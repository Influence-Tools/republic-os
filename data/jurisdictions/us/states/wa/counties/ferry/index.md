---
type: Jurisdiction
title: "Ferry County, WA"
classification: county
fips: "53019"
state: "WA"
demographics:
  population: 7387
  population_under_18: 1228
  population_18_64: 3896
  population_65_plus: 2263
  median_household_income: 55614
  poverty_rate: 13.59
  homeownership_rate: 78.1
  unemployment_rate: 12.46
  median_home_value: 283400
  gini_index: 0.4281
  vacancy_rate: 23.03
  race_white: 5339
  race_black: 24
  race_asian: 52
  race_native: 997
  hispanic: 269
  bachelors_plus: 1213
districts:
  - to: "us/states/wa/districts/05"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/wa/districts/senate/7"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wa/districts/house/7"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wa]
timestamp: "2026-07-03"
---

# Ferry County, WA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7387 |
| Under 18 | 1228 |
| 18–64 | 3896 |
| 65+ | 2263 |
| Median household income | 55614 |
| Poverty rate | 13.59 |
| Homeownership rate | 78.1 |
| Unemployment rate | 12.46 |
| Median home value | 283400 |
| Gini index | 0.4281 |
| Vacancy rate | 23.03 |
| White | 5339 |
| Black | 24 |
| Asian | 52 |
| Native | 997 |
| Hispanic/Latino | 269 |
| Bachelor's or higher | 1213 |

## Districts

- [WA-05](/us/states/wa/districts/05.md) — 100% (congressional)
- [WA Senate District 7](/us/states/wa/districts/senate/7.md) — 100% (state senate)
- [WA House District 7](/us/states/wa/districts/house/7.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
