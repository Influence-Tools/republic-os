---
type: Jurisdiction
title: "Walworth County, SD"
classification: county
fips: "46129"
state: "SD"
demographics:
  population: 5271
  population_under_18: 1278
  population_18_64: 1589
  population_65_plus: 2404
  median_household_income: 65026
  poverty_rate: 14.92
  homeownership_rate: 76.23
  unemployment_rate: 3.48
  median_home_value: 136600
  gini_index: 0.4489
  vacancy_rate: 17.63
  race_white: 4142
  race_black: 18
  race_asian: 32
  race_native: 561
  hispanic: 29
  bachelors_plus: 1488
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/23"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/house/23"
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

# Walworth County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5271 |
| Under 18 | 1278 |
| 18–64 | 1589 |
| 65+ | 2404 |
| Median household income | 65026 |
| Poverty rate | 14.92 |
| Homeownership rate | 76.23 |
| Unemployment rate | 3.48 |
| Median home value | 136600 |
| Gini index | 0.4489 |
| Vacancy rate | 17.63 |
| White | 4142 |
| Black | 18 |
| Asian | 32 |
| Native | 561 |
| Hispanic/Latino | 29 |
| Bachelor's or higher | 1488 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 23](/us/states/sd/districts/senate/23.md) — 100% (state senate)
- [SD House District 23](/us/states/sd/districts/house/23.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
