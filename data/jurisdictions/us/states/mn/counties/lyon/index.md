---
type: Jurisdiction
title: "Lyon County, MN"
classification: county
fips: "27083"
state: "MN"
demographics:
  population: 25503
  population_under_18: 6632
  population_18_64: 14389
  population_65_plus: 4482
  median_household_income: 75303
  poverty_rate: 12.17
  homeownership_rate: 72.5
  unemployment_rate: 3.2
  median_home_value: 200700
  gini_index: 0.4532
  vacancy_rate: 10.3
  race_white: 20844
  race_black: 672
  race_asian: 1148
  race_native: 171
  hispanic: 2014
  bachelors_plus: 6650
districts:
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mn/districts/senate/15"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mn/districts/house/15a"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Lyon County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25503 |
| Under 18 | 6632 |
| 18–64 | 14389 |
| 65+ | 4482 |
| Median household income | 75303 |
| Poverty rate | 12.17 |
| Homeownership rate | 72.5 |
| Unemployment rate | 3.2 |
| Median home value | 200700 |
| Gini index | 0.4532 |
| Vacancy rate | 10.3 |
| White | 20844 |
| Black | 672 |
| Asian | 1148 |
| Native | 171 |
| Hispanic/Latino | 2014 |
| Bachelor's or higher | 6650 |

## Districts

- [MN-07](/us/states/mn/districts/07.md) — 100% (congressional)
- [MN Senate District 15](/us/states/mn/districts/senate/15.md) — 100% (state senate)
- [MN House District 15A](/us/states/mn/districts/house/15a.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
