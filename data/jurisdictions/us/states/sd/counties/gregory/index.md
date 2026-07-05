---
type: Jurisdiction
title: "Gregory County, SD"
classification: county
fips: "46053"
state: "SD"
demographics:
  population: 4016
  population_under_18: 979
  population_18_64: 1969
  population_65_plus: 1068
  median_household_income: 62917
  poverty_rate: 9.53
  homeownership_rate: 76.69
  unemployment_rate: 2.29
  median_home_value: 139900
  gini_index: 0.4318
  vacancy_rate: 26.46
  race_white: 3475
  race_black: 35
  race_asian: 43
  race_native: 162
  hispanic: 24
  bachelors_plus: 805
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/sd/districts/senate/21"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/sd/districts/house/21"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Gregory County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4016 |
| Under 18 | 979 |
| 18–64 | 1969 |
| 65+ | 1068 |
| Median household income | 62917 |
| Poverty rate | 9.53 |
| Homeownership rate | 76.69 |
| Unemployment rate | 2.29 |
| Median home value | 139900 |
| Gini index | 0.4318 |
| Vacancy rate | 26.46 |
| White | 3475 |
| Black | 35 |
| Asian | 43 |
| Native | 162 |
| Hispanic/Latino | 24 |
| Bachelor's or higher | 805 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 21](/us/states/sd/districts/senate/21.md) — 100% (state senate)
- [SD House District 21](/us/states/sd/districts/house/21.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
