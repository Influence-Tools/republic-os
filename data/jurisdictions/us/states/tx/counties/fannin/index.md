---
type: Jurisdiction
title: "Fannin County, TX"
classification: county
fips: "48147"
state: "TX"
demographics:
  population: 37326
  population_under_18: 7868
  population_18_64: 22691
  population_65_plus: 6767
  median_household_income: 72295
  poverty_rate: 13.75
  homeownership_rate: 78.73
  unemployment_rate: 4.99
  median_home_value: 233700
  gini_index: 0.4626
  vacancy_rate: 13.82
  race_white: 30313
  race_black: 2200
  race_asian: 187
  race_native: 162
  hispanic: 4902
  bachelors_plus: 6910
districts:
  - to: "us/states/tx/districts/04"
    rel: in-district
    area_weight: 0.9984
  - to: "us/states/tx/districts/senate/1"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/tx/districts/house/62"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Fannin County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 37326 |
| Under 18 | 7868 |
| 18–64 | 22691 |
| 65+ | 6767 |
| Median household income | 72295 |
| Poverty rate | 13.75 |
| Homeownership rate | 78.73 |
| Unemployment rate | 4.99 |
| Median home value | 233700 |
| Gini index | 0.4626 |
| Vacancy rate | 13.82 |
| White | 30313 |
| Black | 2200 |
| Asian | 187 |
| Native | 162 |
| Hispanic/Latino | 4902 |
| Bachelor's or higher | 6910 |

## Districts

- [TX-04](/us/states/tx/districts/04.md) — 100% (congressional)
- [TX Senate District 1](/us/states/tx/districts/senate/1.md) — 100% (state senate)
- [TX House District 62](/us/states/tx/districts/house/62.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
