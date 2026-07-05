---
type: Jurisdiction
title: "Brown County, NE"
classification: county
fips: "31017"
state: "NE"
demographics:
  population: 2869
  population_under_18: 576
  population_18_64: 1504
  population_65_plus: 789
  median_household_income: 54676
  poverty_rate: 13.39
  homeownership_rate: 74.2
  unemployment_rate: 1.73
  median_home_value: 113900
  gini_index: 0.5085
  vacancy_rate: 23.01
  race_white: 2540
  race_black: 2
  race_asian: 1
  race_native: 15
  hispanic: 177
  bachelors_plus: 644
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

# Brown County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2869 |
| Under 18 | 576 |
| 18–64 | 1504 |
| 65+ | 789 |
| Median household income | 54676 |
| Poverty rate | 13.39 |
| Homeownership rate | 74.2 |
| Unemployment rate | 1.73 |
| Median home value | 113900 |
| Gini index | 0.5085 |
| Vacancy rate | 23.01 |
| White | 2540 |
| Black | 2 |
| Asian | 1 |
| Native | 15 |
| Hispanic/Latino | 177 |
| Bachelor's or higher | 644 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
