---
type: Jurisdiction
title: "Renville County, ND"
classification: county
fips: "38075"
state: "ND"
demographics:
  population: 2304
  population_under_18: 489
  population_18_64: 1330
  population_65_plus: 485
  median_household_income: 74301
  poverty_rate: 9.07
  homeownership_rate: 78.74
  unemployment_rate: 0.97
  median_home_value: 166000
  gini_index: 0.3908
  vacancy_rate: 27.63
  race_white: 2175
  race_black: 5
  race_asian: 13
  race_native: 5
  hispanic: 18
  bachelors_plus: 377
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nd/districts/senate/6"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nd/districts/house/6"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Renville County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2304 |
| Under 18 | 489 |
| 18–64 | 1330 |
| 65+ | 485 |
| Median household income | 74301 |
| Poverty rate | 9.07 |
| Homeownership rate | 78.74 |
| Unemployment rate | 0.97 |
| Median home value | 166000 |
| Gini index | 0.3908 |
| Vacancy rate | 27.63 |
| White | 2175 |
| Black | 5 |
| Asian | 13 |
| Native | 5 |
| Hispanic/Latino | 18 |
| Bachelor's or higher | 377 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 6](/us/states/nd/districts/senate/6.md) — 100% (state senate)
- [ND House District 6](/us/states/nd/districts/house/6.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
