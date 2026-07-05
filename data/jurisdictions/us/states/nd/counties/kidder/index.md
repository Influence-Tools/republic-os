---
type: Jurisdiction
title: "Kidder County, ND"
classification: county
fips: "38043"
state: "ND"
demographics:
  population: 2377
  population_under_18: 524
  population_18_64: 1198
  population_65_plus: 655
  median_household_income: 65610
  poverty_rate: 10.22
  homeownership_rate: 76.07
  unemployment_rate: 1.47
  median_home_value: 156600
  gini_index: 0.4313
  vacancy_rate: 29.52
  race_white: 2283
  race_black: 5
  race_asian: 8
  race_native: 0
  hispanic: 71
  bachelors_plus: 515
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/senate/14"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/house/14"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Kidder County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2377 |
| Under 18 | 524 |
| 18–64 | 1198 |
| 65+ | 655 |
| Median household income | 65610 |
| Poverty rate | 10.22 |
| Homeownership rate | 76.07 |
| Unemployment rate | 1.47 |
| Median home value | 156600 |
| Gini index | 0.4313 |
| Vacancy rate | 29.52 |
| White | 2283 |
| Black | 5 |
| Asian | 8 |
| Native | 0 |
| Hispanic/Latino | 71 |
| Bachelor's or higher | 515 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 14](/us/states/nd/districts/senate/14.md) — 100% (state senate)
- [ND House District 14](/us/states/nd/districts/house/14.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
