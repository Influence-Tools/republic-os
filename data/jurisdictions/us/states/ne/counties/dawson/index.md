---
type: Jurisdiction
title: "Dawson County, NE"
classification: county
fips: "31047"
state: "NE"
demographics:
  population: 24202
  population_under_18: 6723
  population_18_64: 13476
  population_65_plus: 4003
  median_household_income: 69880
  poverty_rate: 10.82
  homeownership_rate: 66.35
  unemployment_rate: 1.4
  median_home_value: 166200
  gini_index: 0.4357
  vacancy_rate: 8.16
  race_white: 14319
  race_black: 1754
  race_asian: 198
  race_native: 135
  hispanic: 9045
  bachelors_plus: 3398
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

# Dawson County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 24202 |
| Under 18 | 6723 |
| 18–64 | 13476 |
| 65+ | 4003 |
| Median household income | 69880 |
| Poverty rate | 10.82 |
| Homeownership rate | 66.35 |
| Unemployment rate | 1.4 |
| Median home value | 166200 |
| Gini index | 0.4357 |
| Vacancy rate | 8.16 |
| White | 14319 |
| Black | 1754 |
| Asian | 198 |
| Native | 135 |
| Hispanic/Latino | 9045 |
| Bachelor's or higher | 3398 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
