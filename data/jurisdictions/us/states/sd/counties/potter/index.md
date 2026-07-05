---
type: Jurisdiction
title: "Potter County, SD"
classification: county
fips: "46107"
state: "SD"
demographics:
  population: 2388
  population_under_18: 553
  population_18_64: 561
  population_65_plus: 1274
  median_household_income: 72045
  poverty_rate: 6.18
  homeownership_rate: 81.52
  unemployment_rate: 2.61
  median_home_value: 121300
  gini_index: 0.4089
  vacancy_rate: 31.97
  race_white: 2227
  race_black: 37
  race_asian: 15
  race_native: 21
  hispanic: 0
  bachelors_plus: 556
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/23"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/sd/districts/house/23"
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

# Potter County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2388 |
| Under 18 | 553 |
| 18–64 | 561 |
| 65+ | 1274 |
| Median household income | 72045 |
| Poverty rate | 6.18 |
| Homeownership rate | 81.52 |
| Unemployment rate | 2.61 |
| Median home value | 121300 |
| Gini index | 0.4089 |
| Vacancy rate | 31.97 |
| White | 2227 |
| Black | 37 |
| Asian | 15 |
| Native | 21 |
| Hispanic/Latino | 0 |
| Bachelor's or higher | 556 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 23](/us/states/sd/districts/senate/23.md) — 100% (state senate)
- [SD House District 23](/us/states/sd/districts/house/23.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
