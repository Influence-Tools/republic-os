---
type: Jurisdiction
title: "Wheeler County, NE"
classification: county
fips: "31183"
state: "NE"
demographics:
  population: 847
  population_under_18: 161
  population_18_64: 438
  population_65_plus: 248
  median_household_income: 70250
  poverty_rate: 5.19
  homeownership_rate: 77.72
  unemployment_rate: 2.31
  median_home_value: 146500
  gini_index: 0.5077
  vacancy_rate: 38.95
  race_white: 809
  race_black: 0
  race_asian: 0
  race_native: 0
  hispanic: 32
  bachelors_plus: 262
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

# Wheeler County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 847 |
| Under 18 | 161 |
| 18–64 | 438 |
| 65+ | 248 |
| Median household income | 70250 |
| Poverty rate | 5.19 |
| Homeownership rate | 77.72 |
| Unemployment rate | 2.31 |
| Median home value | 146500 |
| Gini index | 0.5077 |
| Vacancy rate | 38.95 |
| White | 809 |
| Black | 0 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 32 |
| Bachelor's or higher | 262 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
