---
type: Jurisdiction
title: "St. Louis County, MN"
classification: county
fips: "27137"
state: "MN"
demographics:
  population: 200123
  population_under_18: 37130
  population_18_64: 120242
  population_65_plus: 42751
  median_household_income: 70069
  poverty_rate: 13.21
  homeownership_rate: 71.19
  unemployment_rate: 4.62
  median_home_value: 221400
  gini_index: 0.4608
  vacancy_rate: 16.45
  race_white: 180247
  race_black: 3301
  race_asian: 2076
  race_native: 3129
  hispanic: 3896
  bachelors_plus: 63372
districts:
  - to: "us/states/mn/districts/08"
    rel: in-district
    area_weight: 0.9831
  - to: "us/states/mn/districts/senate/3"
    rel: in-district
    area_weight: 0.6012
  - to: "us/states/mn/districts/senate/7"
    rel: in-district
    area_weight: 0.3455
  - to: "us/states/mn/districts/senate/11"
    rel: in-district
    area_weight: 0.0257
  - to: "us/states/mn/districts/senate/8"
    rel: in-district
    area_weight: 0.0106
  - to: "us/states/mn/districts/house/3a"
    rel: in-district
    area_weight: 0.4511
  - to: "us/states/mn/districts/house/7b"
    rel: in-district
    area_weight: 0.2461
  - to: "us/states/mn/districts/house/3b"
    rel: in-district
    area_weight: 0.1501
  - to: "us/states/mn/districts/house/7a"
    rel: in-district
    area_weight: 0.0994
  - to: "us/states/mn/districts/house/11a"
    rel: in-district
    area_weight: 0.0257
  - to: "us/states/mn/districts/house/8a"
    rel: in-district
    area_weight: 0.0058
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# St. Louis County, MN

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 200123 |
| Under 18 | 37130 |
| 18–64 | 120242 |
| 65+ | 42751 |
| Median household income | 70069 |
| Poverty rate | 13.21 |
| Homeownership rate | 71.19 |
| Unemployment rate | 4.62 |
| Median home value | 221400 |
| Gini index | 0.4608 |
| Vacancy rate | 16.45 |
| White | 180247 |
| Black | 3301 |
| Asian | 2076 |
| Native | 3129 |
| Hispanic/Latino | 3896 |
| Bachelor's or higher | 63372 |

## Districts

- [MN-08](/us/states/mn/districts/08.md) — 98% (congressional)
- [MN Senate District 3](/us/states/mn/districts/senate/3.md) — 60% (state senate)
- [MN Senate District 7](/us/states/mn/districts/senate/7.md) — 35% (state senate)
- [MN Senate District 11](/us/states/mn/districts/senate/11.md) — 3% (state senate)
- [MN Senate District 8](/us/states/mn/districts/senate/8.md) — 1% (state senate)
- [MN House District 3A](/us/states/mn/districts/house/3a.md) — 45% (state house)
- [MN House District 7B](/us/states/mn/districts/house/7b.md) — 25% (state house)
- [MN House District 3B](/us/states/mn/districts/house/3b.md) — 15% (state house)
- [MN House District 7A](/us/states/mn/districts/house/7a.md) — 10% (state house)
- [MN House District 11A](/us/states/mn/districts/house/11a.md) — 3% (state house)
- [MN House District 8A](/us/states/mn/districts/house/8a.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
