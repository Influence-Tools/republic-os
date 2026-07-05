---
type: Jurisdiction
title: "Jones County, SD"
classification: county
fips: "46075"
state: "SD"
demographics:
  population: 1004
  population_under_18: 319
  population_18_64: 440
  population_65_plus: 245
  median_household_income: 65119
  poverty_rate: 18.31
  homeownership_rate: 76.32
  unemployment_rate: 2.13
  median_home_value: 139600
  gini_index: 0.42
  vacancy_rate: 28.6
  race_white: 805
  race_black: 0
  race_asian: 0
  race_native: 175
  hispanic: 10
  bachelors_plus: 235
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/26"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/sd/districts/house/26a"
    rel: in-district
    area_weight: 0.5724
  - to: "us/states/sd/districts/house/26b"
    rel: in-district
    area_weight: 0.4275
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Jones County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1004 |
| Under 18 | 319 |
| 18–64 | 440 |
| 65+ | 245 |
| Median household income | 65119 |
| Poverty rate | 18.31 |
| Homeownership rate | 76.32 |
| Unemployment rate | 2.13 |
| Median home value | 139600 |
| Gini index | 0.42 |
| Vacancy rate | 28.6 |
| White | 805 |
| Black | 0 |
| Asian | 0 |
| Native | 175 |
| Hispanic/Latino | 10 |
| Bachelor's or higher | 235 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 26](/us/states/sd/districts/senate/26.md) — 100% (state senate)
- [SD House District 26A](/us/states/sd/districts/house/26a.md) — 57% (state house)
- [SD House District 26B](/us/states/sd/districts/house/26b.md) — 43% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
