---
type: Jurisdiction
title: "Emmons County, ND"
classification: county
fips: "38029"
state: "ND"
demographics:
  population: 3254
  population_under_18: 658
  population_18_64: 1631
  population_65_plus: 965
  median_household_income: 66538
  poverty_rate: 9.08
  homeownership_rate: 79.78
  unemployment_rate: 2.27
  median_home_value: 117200
  gini_index: 0.4624
  vacancy_rate: 25.5
  race_white: 3037
  race_black: 4
  race_asian: 7
  race_native: 38
  hispanic: 39
  bachelors_plus: 695
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nd/districts/senate/8"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/nd/districts/house/8"
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

# Emmons County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3254 |
| Under 18 | 658 |
| 18–64 | 1631 |
| 65+ | 965 |
| Median household income | 66538 |
| Poverty rate | 9.08 |
| Homeownership rate | 79.78 |
| Unemployment rate | 2.27 |
| Median home value | 117200 |
| Gini index | 0.4624 |
| Vacancy rate | 25.5 |
| White | 3037 |
| Black | 4 |
| Asian | 7 |
| Native | 38 |
| Hispanic/Latino | 39 |
| Bachelor's or higher | 695 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 8](/us/states/nd/districts/senate/8.md) — 100% (state senate)
- [ND House District 8](/us/states/nd/districts/house/8.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
