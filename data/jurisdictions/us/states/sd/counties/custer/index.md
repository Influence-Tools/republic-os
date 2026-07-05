---
type: Jurisdiction
title: "Custer County, SD"
classification: county
fips: "46033"
state: "SD"
demographics:
  population: 8892
  population_under_18: 1225
  population_18_64: 4670
  population_65_plus: 2997
  median_household_income: 84112
  poverty_rate: 8.97
  homeownership_rate: 85.58
  unemployment_rate: 2.26
  median_home_value: 372100
  gini_index: 0.4708
  vacancy_rate: 15.88
  race_white: 7902
  race_black: 29
  race_asian: 39
  race_native: 177
  hispanic: 274
  bachelors_plus: 3235
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/30"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/sd/districts/house/30"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Custer County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8892 |
| Under 18 | 1225 |
| 18–64 | 4670 |
| 65+ | 2997 |
| Median household income | 84112 |
| Poverty rate | 8.97 |
| Homeownership rate | 85.58 |
| Unemployment rate | 2.26 |
| Median home value | 372100 |
| Gini index | 0.4708 |
| Vacancy rate | 15.88 |
| White | 7902 |
| Black | 29 |
| Asian | 39 |
| Native | 177 |
| Hispanic/Latino | 274 |
| Bachelor's or higher | 3235 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 30](/us/states/sd/districts/senate/30.md) — 100% (state senate)
- [SD House District 30](/us/states/sd/districts/house/30.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
