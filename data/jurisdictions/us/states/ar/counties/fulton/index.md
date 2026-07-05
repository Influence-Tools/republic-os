---
type: Jurisdiction
title: "Fulton County, AR"
classification: county
fips: "05049"
state: "AR"
demographics:
  population: 12302
  population_under_18: 2541
  population_18_64: 6561
  population_65_plus: 3200
  median_household_income: 42241
  poverty_rate: 18.01
  homeownership_rate: 84.7
  unemployment_rate: 4.6
  median_home_value: 113800
  gini_index: 0.4286
  vacancy_rate: 23.58
  race_white: 11369
  race_black: 42
  race_asian: 29
  race_native: 89
  hispanic: 238
  bachelors_plus: 2021
districts:
  - to: "us/states/ar/districts/01"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ar/districts/senate/23"
    rel: in-district
    area_weight: 0.8622
  - to: "us/states/ar/districts/senate/22"
    rel: in-district
    area_weight: 0.1375
  - to: "us/states/ar/districts/house/2"
    rel: in-district
    area_weight: 0.6618
  - to: "us/states/ar/districts/house/3"
    rel: in-district
    area_weight: 0.3378
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Fulton County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12302 |
| Under 18 | 2541 |
| 18–64 | 6561 |
| 65+ | 3200 |
| Median household income | 42241 |
| Poverty rate | 18.01 |
| Homeownership rate | 84.7 |
| Unemployment rate | 4.6 |
| Median home value | 113800 |
| Gini index | 0.4286 |
| Vacancy rate | 23.58 |
| White | 11369 |
| Black | 42 |
| Asian | 29 |
| Native | 89 |
| Hispanic/Latino | 238 |
| Bachelor's or higher | 2021 |

## Districts

- [AR-01](/us/states/ar/districts/01.md) — 100% (congressional)
- [AR Senate District 23](/us/states/ar/districts/senate/23.md) — 86% (state senate)
- [AR Senate District 22](/us/states/ar/districts/senate/22.md) — 14% (state senate)
- [AR House District 2](/us/states/ar/districts/house/2.md) — 66% (state house)
- [AR House District 3](/us/states/ar/districts/house/3.md) — 34% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
