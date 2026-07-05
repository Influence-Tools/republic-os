---
type: Jurisdiction
title: "Sully County, SD"
classification: county
fips: "46119"
state: "SD"
demographics:
  population: 1526
  population_under_18: 362
  population_18_64: 343
  population_65_plus: 821
  median_household_income: 72578
  poverty_rate: 6.32
  homeownership_rate: 72.84
  unemployment_rate: 0.0
  median_home_value: 205400
  gini_index: 0.4466
  vacancy_rate: 31.8
  race_white: 1320
  race_black: 69
  race_asian: 0
  race_native: 60
  hispanic: 0
  bachelors_plus: 322
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/24"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/house/24"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Sully County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1526 |
| Under 18 | 362 |
| 18–64 | 343 |
| 65+ | 821 |
| Median household income | 72578 |
| Poverty rate | 6.32 |
| Homeownership rate | 72.84 |
| Unemployment rate | 0.0 |
| Median home value | 205400 |
| Gini index | 0.4466 |
| Vacancy rate | 31.8 |
| White | 1320 |
| Black | 69 |
| Asian | 0 |
| Native | 60 |
| Hispanic/Latino | 0 |
| Bachelor's or higher | 322 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 24](/us/states/sd/districts/senate/24.md) — 100% (state senate)
- [SD House District 24](/us/states/sd/districts/house/24.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
