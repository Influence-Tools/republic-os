---
type: Jurisdiction
title: "Richland County, ND"
classification: county
fips: "38077"
state: "ND"
demographics:
  population: 16584
  population_under_18: 3595
  population_18_64: 9633
  population_65_plus: 3356
  median_household_income: 75432
  poverty_rate: 9.68
  homeownership_rate: 68.11
  unemployment_rate: 1.67
  median_home_value: 183600
  gini_index: 0.4474
  vacancy_rate: 9.04
  race_white: 14911
  race_black: 144
  race_asian: 135
  race_native: 297
  hispanic: 624
  bachelors_plus: 3296
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/nd/districts/senate/25"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/nd/districts/house/25"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Richland County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16584 |
| Under 18 | 3595 |
| 18–64 | 9633 |
| 65+ | 3356 |
| Median household income | 75432 |
| Poverty rate | 9.68 |
| Homeownership rate | 68.11 |
| Unemployment rate | 1.67 |
| Median home value | 183600 |
| Gini index | 0.4474 |
| Vacancy rate | 9.04 |
| White | 14911 |
| Black | 144 |
| Asian | 135 |
| Native | 297 |
| Hispanic/Latino | 624 |
| Bachelor's or higher | 3296 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 25](/us/states/nd/districts/senate/25.md) — 100% (state senate)
- [ND House District 25](/us/states/nd/districts/house/25.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
