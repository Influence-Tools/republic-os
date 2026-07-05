---
type: Jurisdiction
title: "Waseca County, MN"
classification: county
fips: "27161"
state: "MN"
demographics:
  population: 18885
  population_under_18: 4296
  population_18_64: 10975
  population_65_plus: 3614
  median_household_income: 76261
  poverty_rate: 7.5
  homeownership_rate: 80.74
  unemployment_rate: 2.5
  median_home_value: 220800
  gini_index: 0.4009
  vacancy_rate: 5.62
  race_white: 17257
  race_black: 191
  race_asian: 354
  race_native: 106
  hispanic: 1380
  bachelors_plus: 3394
districts:
  - to: "us/states/mn/districts/01"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/mn/districts/senate/23"
    rel: in-district
    area_weight: 0.5004
  - to: "us/states/mn/districts/senate/19"
    rel: in-district
    area_weight: 0.4995
  - to: "us/states/mn/districts/house/23a"
    rel: in-district
    area_weight: 0.5004
  - to: "us/states/mn/districts/house/19a"
    rel: in-district
    area_weight: 0.3332
  - to: "us/states/mn/districts/house/19b"
    rel: in-district
    area_weight: 0.1663
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Waseca County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18885 |
| Under 18 | 4296 |
| 18–64 | 10975 |
| 65+ | 3614 |
| Median household income | 76261 |
| Poverty rate | 7.5 |
| Homeownership rate | 80.74 |
| Unemployment rate | 2.5 |
| Median home value | 220800 |
| Gini index | 0.4009 |
| Vacancy rate | 5.62 |
| White | 17257 |
| Black | 191 |
| Asian | 354 |
| Native | 106 |
| Hispanic/Latino | 1380 |
| Bachelor's or higher | 3394 |

## Districts

- [MN-01](/us/states/mn/districts/01.md) — 100% (congressional)
- [MN Senate District 23](/us/states/mn/districts/senate/23.md) — 50% (state senate)
- [MN Senate District 19](/us/states/mn/districts/senate/19.md) — 50% (state senate)
- [MN House District 23A](/us/states/mn/districts/house/23a.md) — 50% (state house)
- [MN House District 19A](/us/states/mn/districts/house/19a.md) — 33% (state house)
- [MN House District 19B](/us/states/mn/districts/house/19b.md) — 17% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
