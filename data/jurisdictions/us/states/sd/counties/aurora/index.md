---
type: Jurisdiction
title: "Aurora County, SD"
classification: county
fips: "46003"
state: "SD"
demographics:
  population: 2642
  population_under_18: 674
  population_18_64: 1448
  population_65_plus: 520
  median_household_income: 72885
  poverty_rate: 10.6
  homeownership_rate: 72.74
  unemployment_rate: 1.24
  median_home_value: 151900
  gini_index: 0.4322
  vacancy_rate: 15.62
  race_white: 2296
  race_black: 15
  race_asian: 6
  race_native: 11
  hispanic: 184
  bachelors_plus: 441
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/21"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/sd/districts/house/21"
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

# Aurora County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2642 |
| Under 18 | 674 |
| 18–64 | 1448 |
| 65+ | 520 |
| Median household income | 72885 |
| Poverty rate | 10.6 |
| Homeownership rate | 72.74 |
| Unemployment rate | 1.24 |
| Median home value | 151900 |
| Gini index | 0.4322 |
| Vacancy rate | 15.62 |
| White | 2296 |
| Black | 15 |
| Asian | 6 |
| Native | 11 |
| Hispanic/Latino | 184 |
| Bachelor's or higher | 441 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 21](/us/states/sd/districts/senate/21.md) — 100% (state senate)
- [SD House District 21](/us/states/sd/districts/house/21.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
