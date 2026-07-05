---
type: Jurisdiction
title: "Steele County, ND"
classification: county
fips: "38091"
state: "ND"
demographics:
  population: 1804
  population_under_18: 393
  population_18_64: 870
  population_65_plus: 541
  median_household_income: 77500
  poverty_rate: 12.86
  homeownership_rate: 77.79
  unemployment_rate: 3.27
  median_home_value: 130700
  gini_index: 0.4429
  vacancy_rate: 27.97
  race_white: 1705
  race_black: 3
  race_asian: 0
  race_native: 11
  hispanic: 35
  bachelors_plus: 422
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/senate/29"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/nd/districts/house/29"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Steele County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1804 |
| Under 18 | 393 |
| 18–64 | 870 |
| 65+ | 541 |
| Median household income | 77500 |
| Poverty rate | 12.86 |
| Homeownership rate | 77.79 |
| Unemployment rate | 3.27 |
| Median home value | 130700 |
| Gini index | 0.4429 |
| Vacancy rate | 27.97 |
| White | 1705 |
| Black | 3 |
| Asian | 0 |
| Native | 11 |
| Hispanic/Latino | 35 |
| Bachelor's or higher | 422 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 29](/us/states/nd/districts/senate/29.md) — 100% (state senate)
- [ND House District 29](/us/states/nd/districts/house/29.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
