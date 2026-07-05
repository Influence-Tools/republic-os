---
type: Jurisdiction
title: "Holt County, MO"
classification: county
fips: "29087"
state: "MO"
demographics:
  population: 4240
  population_under_18: 882
  population_18_64: 2269
  population_65_plus: 1089
  median_household_income: 61187
  poverty_rate: 10.23
  homeownership_rate: 77.24
  unemployment_rate: 1.83
  median_home_value: 138200
  gini_index: 0.4433
  vacancy_rate: 27.48
  race_white: 4000
  race_black: 18
  race_asian: 16
  race_native: 0
  hispanic: 79
  bachelors_plus: 789
districts:
  - to: "us/states/mo/districts/06"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/mo/districts/senate/12"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/mo/districts/house/1"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Holt County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4240 |
| Under 18 | 882 |
| 18–64 | 2269 |
| 65+ | 1089 |
| Median household income | 61187 |
| Poverty rate | 10.23 |
| Homeownership rate | 77.24 |
| Unemployment rate | 1.83 |
| Median home value | 138200 |
| Gini index | 0.4433 |
| Vacancy rate | 27.48 |
| White | 4000 |
| Black | 18 |
| Asian | 16 |
| Native | 0 |
| Hispanic/Latino | 79 |
| Bachelor's or higher | 789 |

## Districts

- [MO-06](/us/states/mo/districts/06.md) — 100% (congressional)
- [MO Senate District 12](/us/states/mo/districts/senate/12.md) — 100% (state senate)
- [MO House District 1](/us/states/mo/districts/house/1.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
