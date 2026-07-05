---
type: Jurisdiction
title: "Hughes County, SD"
classification: county
fips: "46065"
state: "SD"
demographics:
  population: 17664
  population_under_18: 4312
  population_18_64: 10164
  population_65_plus: 3188
  median_household_income: 81395
  poverty_rate: 9.16
  homeownership_rate: 71.98
  unemployment_rate: 0.96
  median_home_value: 242000
  gini_index: 0.4196
  vacancy_rate: 9.3
  race_white: 14252
  race_black: 9
  race_asian: 116
  race_native: 1941
  hispanic: 580
  bachelors_plus: 6532
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/24"
    rel: in-district
    area_weight: 0.8499
  - to: "us/states/sd/districts/senate/26"
    rel: in-district
    area_weight: 0.1501
  - to: "us/states/sd/districts/house/24"
    rel: in-district
    area_weight: 0.8499
  - to: "us/states/sd/districts/house/26b"
    rel: in-district
    area_weight: 0.1501
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Hughes County, SD

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17664 |
| Under 18 | 4312 |
| 18–64 | 10164 |
| 65+ | 3188 |
| Median household income | 81395 |
| Poverty rate | 9.16 |
| Homeownership rate | 71.98 |
| Unemployment rate | 0.96 |
| Median home value | 242000 |
| Gini index | 0.4196 |
| Vacancy rate | 9.3 |
| White | 14252 |
| Black | 9 |
| Asian | 116 |
| Native | 1941 |
| Hispanic/Latino | 580 |
| Bachelor's or higher | 6532 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 24](/us/states/sd/districts/senate/24.md) — 85% (state senate)
- [SD Senate District 26](/us/states/sd/districts/senate/26.md) — 15% (state senate)
- [SD House District 24](/us/states/sd/districts/house/24.md) — 85% (state house)
- [SD House District 26B](/us/states/sd/districts/house/26b.md) — 15% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
