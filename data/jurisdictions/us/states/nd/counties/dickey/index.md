---
type: Jurisdiction
title: "Dickey County, ND"
classification: county
fips: "38021"
state: "ND"
demographics:
  population: 4935
  population_under_18: 1125
  population_18_64: 2830
  population_65_plus: 980
  median_household_income: 68654
  poverty_rate: 11.75
  homeownership_rate: 79.71
  unemployment_rate: 4.12
  median_home_value: 162400
  gini_index: 0.4806
  vacancy_rate: 18.05
  race_white: 4452
  race_black: 0
  race_asian: 71
  race_native: 51
  hispanic: 204
  bachelors_plus: 1213
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/nd/districts/senate/28"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/nd/districts/house/28"
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

# Dickey County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4935 |
| Under 18 | 1125 |
| 18–64 | 2830 |
| 65+ | 980 |
| Median household income | 68654 |
| Poverty rate | 11.75 |
| Homeownership rate | 79.71 |
| Unemployment rate | 4.12 |
| Median home value | 162400 |
| Gini index | 0.4806 |
| Vacancy rate | 18.05 |
| White | 4452 |
| Black | 0 |
| Asian | 71 |
| Native | 51 |
| Hispanic/Latino | 204 |
| Bachelor's or higher | 1213 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 28](/us/states/nd/districts/senate/28.md) — 100% (state senate)
- [ND House District 28](/us/states/nd/districts/house/28.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
