---
type: Jurisdiction
title: "Thurston County, NE"
classification: county
fips: "31173"
state: "NE"
demographics:
  population: 6627
  population_under_18: 2273
  population_18_64: 3520
  population_65_plus: 834
  median_household_income: 69177
  poverty_rate: 13.89
  homeownership_rate: 61.01
  unemployment_rate: 9.97
  median_home_value: 114600
  gini_index: 0.4219
  vacancy_rate: 13.1
  race_white: 2418
  race_black: 18
  race_asian: 93
  race_native: 3630
  hispanic: 322
  bachelors_plus: 1057
districts:
  - to: "us/states/ne/districts/03"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ne]
timestamp: "2026-07-03"
---

# Thurston County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6627 |
| Under 18 | 2273 |
| 18–64 | 3520 |
| 65+ | 834 |
| Median household income | 69177 |
| Poverty rate | 13.89 |
| Homeownership rate | 61.01 |
| Unemployment rate | 9.97 |
| Median home value | 114600 |
| Gini index | 0.4219 |
| Vacancy rate | 13.1 |
| White | 2418 |
| Black | 18 |
| Asian | 93 |
| Native | 3630 |
| Hispanic/Latino | 322 |
| Bachelor's or higher | 1057 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
