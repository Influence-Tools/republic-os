---
type: Jurisdiction
title: "Yellow Medicine County, MN"
classification: county
fips: "27173"
state: "MN"
demographics:
  population: 9451
  population_under_18: 2153
  population_18_64: 5263
  population_65_plus: 2035
  median_household_income: 74000
  poverty_rate: 8.56
  homeownership_rate: 84.0
  unemployment_rate: 3.54
  median_home_value: 154700
  gini_index: 0.4245
  vacancy_rate: 9.31
  race_white: 8251
  race_black: 79
  race_asian: 12
  race_native: 248
  hispanic: 517
  bachelors_plus: 1644
districts:
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mn/districts/senate/15"
    rel: in-district
    area_weight: 0.9999
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

# Yellow Medicine County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9451 |
| Under 18 | 2153 |
| 18–64 | 5263 |
| 65+ | 2035 |
| Median household income | 74000 |
| Poverty rate | 8.56 |
| Homeownership rate | 84.0 |
| Unemployment rate | 3.54 |
| Median home value | 154700 |
| Gini index | 0.4245 |
| Vacancy rate | 9.31 |
| White | 8251 |
| Black | 79 |
| Asian | 12 |
| Native | 248 |
| Hispanic/Latino | 517 |
| Bachelor's or higher | 1644 |

## Districts

- [MN-07](/us/states/mn/districts/07.md) — 100% (congressional)
- [MN Senate District 15](/us/states/mn/districts/senate/15.md) — 100% (state senate)
- [MN House District 15A](/us/states/mn/districts/house/15a.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
