---
type: Jurisdiction
title: "Morrison County, MN"
classification: county
fips: "27097"
state: "MN"
demographics:
  population: 34249
  population_under_18: 7871
  population_18_64: 19092
  population_65_plus: 7286
  median_household_income: 69446
  poverty_rate: 10.95
  homeownership_rate: 80.6
  unemployment_rate: 3.99
  median_home_value: 248500
  gini_index: 0.4354
  vacancy_rate: 13.36
  race_white: 32447
  race_black: 164
  race_asian: 126
  race_native: 76
  hispanic: 658
  bachelors_plus: 5973
districts:
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/mn/districts/senate/10"
    rel: in-district
    area_weight: 0.8985
  - to: "us/states/mn/districts/senate/5"
    rel: in-district
    area_weight: 0.1015
  - to: "us/states/mn/districts/house/10a"
    rel: in-district
    area_weight: 0.5204
  - to: "us/states/mn/districts/house/10b"
    rel: in-district
    area_weight: 0.3781
  - to: "us/states/mn/districts/house/5b"
    rel: in-district
    area_weight: 0.1015
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Morrison County, MN

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 34249 |
| Under 18 | 7871 |
| 18–64 | 19092 |
| 65+ | 7286 |
| Median household income | 69446 |
| Poverty rate | 10.95 |
| Homeownership rate | 80.6 |
| Unemployment rate | 3.99 |
| Median home value | 248500 |
| Gini index | 0.4354 |
| Vacancy rate | 13.36 |
| White | 32447 |
| Black | 164 |
| Asian | 126 |
| Native | 76 |
| Hispanic/Latino | 658 |
| Bachelor's or higher | 5973 |

## Districts

- [MN-07](/us/states/mn/districts/07.md) — 100% (congressional)
- [MN Senate District 10](/us/states/mn/districts/senate/10.md) — 90% (state senate)
- [MN Senate District 5](/us/states/mn/districts/senate/5.md) — 10% (state senate)
- [MN House District 10A](/us/states/mn/districts/house/10a.md) — 52% (state house)
- [MN House District 10B](/us/states/mn/districts/house/10b.md) — 38% (state house)
- [MN House District 5B](/us/states/mn/districts/house/5b.md) — 10% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
