---
type: Jurisdiction
title: "Irion County, TX"
classification: county
fips: "48235"
state: "TX"
demographics:
  population: 1409
  population_under_18: 330
  population_18_64: 770
  population_65_plus: 309
  median_household_income: 70357
  poverty_rate: 10.79
  homeownership_rate: 82.82
  unemployment_rate: 0.43
  median_home_value: 204400
  gini_index: 0.4443
  vacancy_rate: 23.74
  race_white: 1022
  race_black: 1
  race_asian: 0
  race_native: 40
  hispanic: 388
  bachelors_plus: 351
districts:
  - to: "us/states/tx/districts/11"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/tx/districts/house/72"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Irion County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1409 |
| Under 18 | 330 |
| 18–64 | 770 |
| 65+ | 309 |
| Median household income | 70357 |
| Poverty rate | 10.79 |
| Homeownership rate | 82.82 |
| Unemployment rate | 0.43 |
| Median home value | 204400 |
| Gini index | 0.4443 |
| Vacancy rate | 23.74 |
| White | 1022 |
| Black | 1 |
| Asian | 0 |
| Native | 40 |
| Hispanic/Latino | 388 |
| Bachelor's or higher | 351 |

## Districts

- [TX-11](/us/states/tx/districts/11.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 72](/us/states/tx/districts/house/72.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
