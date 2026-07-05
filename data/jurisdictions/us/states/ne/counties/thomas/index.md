---
type: Jurisdiction
title: "Thomas County, NE"
classification: county
fips: "31171"
state: "NE"
demographics:
  population: 564
  population_under_18: 63
  population_18_64: 281
  population_65_plus: 220
  median_household_income: 65000
  poverty_rate: 8.87
  homeownership_rate: 68.09
  unemployment_rate: 2.1
  median_home_value: 109200
  gini_index: 0.3199
  vacancy_rate: 14.85
  race_white: 503
  race_black: 11
  race_asian: 0
  race_native: 0
  hispanic: 28
  bachelors_plus: 167
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

# Thomas County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 564 |
| Under 18 | 63 |
| 18–64 | 281 |
| 65+ | 220 |
| Median household income | 65000 |
| Poverty rate | 8.87 |
| Homeownership rate | 68.09 |
| Unemployment rate | 2.1 |
| Median home value | 109200 |
| Gini index | 0.3199 |
| Vacancy rate | 14.85 |
| White | 503 |
| Black | 11 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 28 |
| Bachelor's or higher | 167 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
