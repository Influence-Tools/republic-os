---
type: Jurisdiction
title: "Allen Parish, LA"
classification: county
fips: "22003"
state: "LA"
demographics:
  population: 22477
  population_under_18: 5206
  population_18_64: 13960
  population_65_plus: 3311
  median_household_income: 46469
  poverty_rate: 23.07
  homeownership_rate: 73.99
  unemployment_rate: 9.79
  median_home_value: 104500
  gini_index: 0.459
  vacancy_rate: 18.08
  race_white: 15437
  race_black: 4756
  race_asian: 163
  race_native: 255
  hispanic: 1353
  bachelors_plus: 2517
districts:
  - to: "us/states/la/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/la/districts/senate/28"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/la/districts/house/32"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Allen Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 22477 |
| Under 18 | 5206 |
| 18–64 | 13960 |
| 65+ | 3311 |
| Median household income | 46469 |
| Poverty rate | 23.07 |
| Homeownership rate | 73.99 |
| Unemployment rate | 9.79 |
| Median home value | 104500 |
| Gini index | 0.459 |
| Vacancy rate | 18.08 |
| White | 15437 |
| Black | 4756 |
| Asian | 163 |
| Native | 255 |
| Hispanic/Latino | 1353 |
| Bachelor's or higher | 2517 |

## Districts

- [LA-04](/us/states/la/districts/04.md) — 100% (congressional)
- [LA Senate District 28](/us/states/la/districts/senate/28.md) — 100% (state senate)
- [LA House District 32](/us/states/la/districts/house/32.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
