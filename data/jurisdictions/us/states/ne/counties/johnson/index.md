---
type: Jurisdiction
title: "Johnson County, NE"
classification: county
fips: "31097"
state: "NE"
demographics:
  population: 5261
  population_under_18: 1037
  population_18_64: 3241
  population_65_plus: 983
  median_household_income: 57632
  poverty_rate: 9.72
  homeownership_rate: 67.21
  unemployment_rate: 3.37
  median_home_value: 155500
  gini_index: 0.4737
  vacancy_rate: 18.59
  race_white: 4153
  race_black: 246
  race_asian: 44
  race_native: 129
  hispanic: 627
  bachelors_plus: 901
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

# Johnson County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5261 |
| Under 18 | 1037 |
| 18–64 | 3241 |
| 65+ | 983 |
| Median household income | 57632 |
| Poverty rate | 9.72 |
| Homeownership rate | 67.21 |
| Unemployment rate | 3.37 |
| Median home value | 155500 |
| Gini index | 0.4737 |
| Vacancy rate | 18.59 |
| White | 4153 |
| Black | 246 |
| Asian | 44 |
| Native | 129 |
| Hispanic/Latino | 627 |
| Bachelor's or higher | 901 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
