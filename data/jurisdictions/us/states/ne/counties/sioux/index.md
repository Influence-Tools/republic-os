---
type: Jurisdiction
title: "Sioux County, NE"
classification: county
fips: "31165"
state: "NE"
demographics:
  population: 1171
  population_under_18: 245
  population_18_64: 604
  population_65_plus: 322
  median_household_income: 53929
  poverty_rate: 14.94
  homeownership_rate: 59.59
  unemployment_rate: 1.75
  median_home_value: 99300
  gini_index: 0.4149
  vacancy_rate: 28.68
  race_white: 1128
  race_black: 1
  race_asian: 2
  race_native: 0
  hispanic: 25
  bachelors_plus: 241
districts:
  - to: "us/states/ne/districts/03"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ne]
timestamp: "2026-07-03"
---

# Sioux County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1171 |
| Under 18 | 245 |
| 18–64 | 604 |
| 65+ | 322 |
| Median household income | 53929 |
| Poverty rate | 14.94 |
| Homeownership rate | 59.59 |
| Unemployment rate | 1.75 |
| Median home value | 99300 |
| Gini index | 0.4149 |
| Vacancy rate | 28.68 |
| White | 1128 |
| Black | 1 |
| Asian | 2 |
| Native | 0 |
| Hispanic/Latino | 25 |
| Bachelor's or higher | 241 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
