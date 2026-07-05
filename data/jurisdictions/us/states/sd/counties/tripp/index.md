---
type: Jurisdiction
title: "Tripp County, SD"
classification: county
fips: "46123"
state: "SD"
demographics:
  population: 5611
  population_under_18: 1429
  population_18_64: 1375
  population_65_plus: 2807
  median_household_income: 58987
  poverty_rate: 18.45
  homeownership_rate: 68.42
  unemployment_rate: 1.82
  median_home_value: 132900
  gini_index: 0.4473
  vacancy_rate: 18.25
  race_white: 4485
  race_black: 44
  race_asian: 25
  race_native: 770
  hispanic: 107
  bachelors_plus: 863
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/sd/districts/senate/21"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/sd/districts/house/21"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Tripp County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5611 |
| Under 18 | 1429 |
| 18–64 | 1375 |
| 65+ | 2807 |
| Median household income | 58987 |
| Poverty rate | 18.45 |
| Homeownership rate | 68.42 |
| Unemployment rate | 1.82 |
| Median home value | 132900 |
| Gini index | 0.4473 |
| Vacancy rate | 18.25 |
| White | 4485 |
| Black | 44 |
| Asian | 25 |
| Native | 770 |
| Hispanic/Latino | 107 |
| Bachelor's or higher | 863 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 21](/us/states/sd/districts/senate/21.md) — 100% (state senate)
- [SD House District 21](/us/states/sd/districts/house/21.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
