---
type: Jurisdiction
title: "Sioux County, ND"
classification: county
fips: "38085"
state: "ND"
demographics:
  population: 3740
  population_under_18: 1273
  population_18_64: 2107
  population_65_plus: 360
  median_household_income: 42083
  poverty_rate: 43.29
  homeownership_rate: 46.58
  unemployment_rate: 17.02
  median_home_value: 85400
  gini_index: 0.5313
  vacancy_rate: 13.12
  race_white: 465
  race_black: 14
  race_asian: 25
  race_native: 3098
  hispanic: 56
  bachelors_plus: 430
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/nd/districts/senate/31"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/nd/districts/house/31"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Sioux County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3740 |
| Under 18 | 1273 |
| 18–64 | 2107 |
| 65+ | 360 |
| Median household income | 42083 |
| Poverty rate | 43.29 |
| Homeownership rate | 46.58 |
| Unemployment rate | 17.02 |
| Median home value | 85400 |
| Gini index | 0.5313 |
| Vacancy rate | 13.12 |
| White | 465 |
| Black | 14 |
| Asian | 25 |
| Native | 3098 |
| Hispanic/Latino | 56 |
| Bachelor's or higher | 430 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 31](/us/states/nd/districts/senate/31.md) — 100% (state senate)
- [ND House District 31](/us/states/nd/districts/house/31.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
