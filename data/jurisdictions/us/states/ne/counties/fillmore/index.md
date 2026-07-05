---
type: Jurisdiction
title: "Fillmore County, NE"
classification: county
fips: "31059"
state: "NE"
demographics:
  population: 5541
  population_under_18: 1094
  population_18_64: 3127
  population_65_plus: 1320
  median_household_income: 76295
  poverty_rate: 8.83
  homeownership_rate: 80.4
  unemployment_rate: 0.4
  median_home_value: 151000
  gini_index: 0.4611
  vacancy_rate: 13.47
  race_white: 5197
  race_black: 34
  race_asian: 7
  race_native: 33
  hispanic: 209
  bachelors_plus: 1277
districts:
  - to: "us/states/ne/districts/03"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ne]
timestamp: "2026-07-03"
---

# Fillmore County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5541 |
| Under 18 | 1094 |
| 18–64 | 3127 |
| 65+ | 1320 |
| Median household income | 76295 |
| Poverty rate | 8.83 |
| Homeownership rate | 80.4 |
| Unemployment rate | 0.4 |
| Median home value | 151000 |
| Gini index | 0.4611 |
| Vacancy rate | 13.47 |
| White | 5197 |
| Black | 34 |
| Asian | 7 |
| Native | 33 |
| Hispanic/Latino | 209 |
| Bachelor's or higher | 1277 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
