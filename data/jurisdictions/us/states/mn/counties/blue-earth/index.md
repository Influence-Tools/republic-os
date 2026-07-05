---
type: Jurisdiction
title: "Blue Earth County, MN"
classification: county
fips: "27013"
state: "MN"
demographics:
  population: 69871
  population_under_18: 13786
  population_18_64: 45429
  population_65_plus: 10656
  median_household_income: 74477
  poverty_rate: 15.67
  homeownership_rate: 61.36
  unemployment_rate: 4.89
  median_home_value: 266700
  gini_index: 0.4333
  vacancy_rate: 7.56
  race_white: 59639
  race_black: 3360
  race_asian: 1621
  race_native: 192
  hispanic: 3369
  bachelors_plus: 18459
districts:
  - to: "us/states/mn/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mn/districts/senate/22"
    rel: in-district
    area_weight: 0.8197
  - to: "us/states/mn/districts/senate/15"
    rel: in-district
    area_weight: 0.1161
  - to: "us/states/mn/districts/senate/18"
    rel: in-district
    area_weight: 0.0642
  - to: "us/states/mn/districts/house/22a"
    rel: in-district
    area_weight: 0.685
  - to: "us/states/mn/districts/house/22b"
    rel: in-district
    area_weight: 0.1347
  - to: "us/states/mn/districts/house/15b"
    rel: in-district
    area_weight: 0.1161
  - to: "us/states/mn/districts/house/18a"
    rel: in-district
    area_weight: 0.038
  - to: "us/states/mn/districts/house/18b"
    rel: in-district
    area_weight: 0.0262
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Blue Earth County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 69871 |
| Under 18 | 13786 |
| 18–64 | 45429 |
| 65+ | 10656 |
| Median household income | 74477 |
| Poverty rate | 15.67 |
| Homeownership rate | 61.36 |
| Unemployment rate | 4.89 |
| Median home value | 266700 |
| Gini index | 0.4333 |
| Vacancy rate | 7.56 |
| White | 59639 |
| Black | 3360 |
| Asian | 1621 |
| Native | 192 |
| Hispanic/Latino | 3369 |
| Bachelor's or higher | 18459 |

## Districts

- [MN-01](/us/states/mn/districts/01.md) — 100% (congressional)
- [MN Senate District 22](/us/states/mn/districts/senate/22.md) — 82% (state senate)
- [MN Senate District 15](/us/states/mn/districts/senate/15.md) — 12% (state senate)
- [MN Senate District 18](/us/states/mn/districts/senate/18.md) — 6% (state senate)
- [MN House District 22A](/us/states/mn/districts/house/22a.md) — 68% (state house)
- [MN House District 22B](/us/states/mn/districts/house/22b.md) — 13% (state house)
- [MN House District 15B](/us/states/mn/districts/house/15b.md) — 12% (state house)
- [MN House District 18A](/us/states/mn/districts/house/18a.md) — 4% (state house)
- [MN House District 18B](/us/states/mn/districts/house/18b.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
