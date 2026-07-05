---
type: Jurisdiction
title: "Big Stone County, MN"
classification: county
fips: "27011"
state: "MN"
demographics:
  population: 5127
  population_under_18: 1127
  population_18_64: 2622
  population_65_plus: 1378
  median_household_income: 70400
  poverty_rate: 12.94
  homeownership_rate: 79.73
  unemployment_rate: 1.79
  median_home_value: 169100
  gini_index: 0.4629
  vacancy_rate: 28.82
  race_white: 4823
  race_black: 14
  race_asian: 38
  race_native: 12
  hispanic: 137
  bachelors_plus: 1315
districts:
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mn/districts/senate/12"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/mn/districts/house/12a"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Big Stone County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5127 |
| Under 18 | 1127 |
| 18–64 | 2622 |
| 65+ | 1378 |
| Median household income | 70400 |
| Poverty rate | 12.94 |
| Homeownership rate | 79.73 |
| Unemployment rate | 1.79 |
| Median home value | 169100 |
| Gini index | 0.4629 |
| Vacancy rate | 28.82 |
| White | 4823 |
| Black | 14 |
| Asian | 38 |
| Native | 12 |
| Hispanic/Latino | 137 |
| Bachelor's or higher | 1315 |

## Districts

- [MN-07](/us/states/mn/districts/07.md) — 100% (congressional)
- [MN Senate District 12](/us/states/mn/districts/senate/12.md) — 100% (state senate)
- [MN House District 12A](/us/states/mn/districts/house/12a.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
