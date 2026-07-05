---
type: Jurisdiction
title: "Washington County, NE"
classification: county
fips: "31177"
state: "NE"
demographics:
  population: 21106
  population_under_18: 5064
  population_18_64: 11995
  population_65_plus: 4047
  median_household_income: 94396
  poverty_rate: 6.4
  homeownership_rate: 83.17
  unemployment_rate: 1.81
  median_home_value: 297600
  gini_index: 0.4268
  vacancy_rate: 3.24
  race_white: 19814
  race_black: 56
  race_asian: 45
  race_native: 51
  hispanic: 702
  bachelors_plus: 6970
districts:
  - to: "us/states/ne/districts/03"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ne]
timestamp: "2026-07-03"
---

# Washington County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21106 |
| Under 18 | 5064 |
| 18–64 | 11995 |
| 65+ | 4047 |
| Median household income | 94396 |
| Poverty rate | 6.4 |
| Homeownership rate | 83.17 |
| Unemployment rate | 1.81 |
| Median home value | 297600 |
| Gini index | 0.4268 |
| Vacancy rate | 3.24 |
| White | 19814 |
| Black | 56 |
| Asian | 45 |
| Native | 51 |
| Hispanic/Latino | 702 |
| Bachelor's or higher | 6970 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
