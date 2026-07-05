---
type: Jurisdiction
title: "Pembina County, ND"
classification: county
fips: "38067"
state: "ND"
demographics:
  population: 6727
  population_under_18: 1418
  population_18_64: 3565
  population_65_plus: 1744
  median_household_income: 68393
  poverty_rate: 9.25
  homeownership_rate: 74.57
  unemployment_rate: 3.36
  median_home_value: 119200
  gini_index: 0.4553
  vacancy_rate: 15.13
  race_white: 6030
  race_black: 65
  race_asian: 32
  race_native: 102
  hispanic: 286
  bachelors_plus: 1462
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 0.9983
  - to: "us/states/nd/districts/senate/19"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/nd/districts/house/19"
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

# Pembina County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6727 |
| Under 18 | 1418 |
| 18–64 | 3565 |
| 65+ | 1744 |
| Median household income | 68393 |
| Poverty rate | 9.25 |
| Homeownership rate | 74.57 |
| Unemployment rate | 3.36 |
| Median home value | 119200 |
| Gini index | 0.4553 |
| Vacancy rate | 15.13 |
| White | 6030 |
| Black | 65 |
| Asian | 32 |
| Native | 102 |
| Hispanic/Latino | 286 |
| Bachelor's or higher | 1462 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 19](/us/states/nd/districts/senate/19.md) — 100% (state senate)
- [ND House District 19](/us/states/nd/districts/house/19.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
