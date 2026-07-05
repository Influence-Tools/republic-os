---
type: Jurisdiction
title: "West Carroll Parish, LA"
classification: county
fips: "22123"
state: "LA"
demographics:
  population: 9464
  population_under_18: 2132
  population_18_64: 5303
  population_65_plus: 2029
  median_household_income: 49134
  poverty_rate: 16.24
  homeownership_rate: 76.1
  unemployment_rate: 5.74
  median_home_value: 94400
  gini_index: 0.4537
  vacancy_rate: 18.35
  race_white: 7568
  race_black: 1387
  race_asian: 23
  race_native: 21
  hispanic: 353
  bachelors_plus: 1375
districts:
  - to: "us/states/la/districts/05"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/la/districts/senate/33"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/la/districts/house/19"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# West Carroll Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9464 |
| Under 18 | 2132 |
| 18–64 | 5303 |
| 65+ | 2029 |
| Median household income | 49134 |
| Poverty rate | 16.24 |
| Homeownership rate | 76.1 |
| Unemployment rate | 5.74 |
| Median home value | 94400 |
| Gini index | 0.4537 |
| Vacancy rate | 18.35 |
| White | 7568 |
| Black | 1387 |
| Asian | 23 |
| Native | 21 |
| Hispanic/Latino | 353 |
| Bachelor's or higher | 1375 |

## Districts

- [LA-05](/us/states/la/districts/05.md) — 100% (congressional)
- [LA Senate District 33](/us/states/la/districts/senate/33.md) — 100% (state senate)
- [LA House District 19](/us/states/la/districts/house/19.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
