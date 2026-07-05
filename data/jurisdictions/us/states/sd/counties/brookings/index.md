---
type: Jurisdiction
title: "Brookings County, SD"
classification: county
fips: "46011"
state: "SD"
demographics:
  population: 35353
  population_under_18: 7455
  population_18_64: 23162
  population_65_plus: 4736
  median_household_income: 70064
  poverty_rate: 13.16
  homeownership_rate: 57.23
  unemployment_rate: 3.75
  median_home_value: 264600
  gini_index: 0.4154
  vacancy_rate: 9.1
  race_white: 31063
  race_black: 401
  race_asian: 1160
  race_native: 460
  hispanic: 1609
  bachelors_plus: 10900
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/sd/districts/senate/8"
    rel: in-district
    area_weight: 0.865
  - to: "us/states/sd/districts/senate/7"
    rel: in-district
    area_weight: 0.1349
  - to: "us/states/sd/districts/house/8"
    rel: in-district
    area_weight: 0.865
  - to: "us/states/sd/districts/house/7"
    rel: in-district
    area_weight: 0.1349
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Brookings County, SD

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 35353 |
| Under 18 | 7455 |
| 18–64 | 23162 |
| 65+ | 4736 |
| Median household income | 70064 |
| Poverty rate | 13.16 |
| Homeownership rate | 57.23 |
| Unemployment rate | 3.75 |
| Median home value | 264600 |
| Gini index | 0.4154 |
| Vacancy rate | 9.1 |
| White | 31063 |
| Black | 401 |
| Asian | 1160 |
| Native | 460 |
| Hispanic/Latino | 1609 |
| Bachelor's or higher | 10900 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 8](/us/states/sd/districts/senate/8.md) — 86% (state senate)
- [SD Senate District 7](/us/states/sd/districts/senate/7.md) — 13% (state senate)
- [SD House District 8](/us/states/sd/districts/house/8.md) — 86% (state house)
- [SD House District 7](/us/states/sd/districts/house/7.md) — 13% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
