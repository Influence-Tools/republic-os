---
type: Jurisdiction
title: "Hitchcock County, NE"
classification: county
fips: "31087"
state: "NE"
demographics:
  population: 2569
  population_under_18: 604
  population_18_64: 1287
  population_65_plus: 678
  median_household_income: 51567
  poverty_rate: 12.75
  homeownership_rate: 78.67
  unemployment_rate: 1.71
  median_home_value: 96700
  gini_index: 0.432
  vacancy_rate: 28.83
  race_white: 2422
  race_black: 1
  race_asian: 17
  race_native: 7
  hispanic: 108
  bachelors_plus: 467
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

# Hitchcock County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2569 |
| Under 18 | 604 |
| 18–64 | 1287 |
| 65+ | 678 |
| Median household income | 51567 |
| Poverty rate | 12.75 |
| Homeownership rate | 78.67 |
| Unemployment rate | 1.71 |
| Median home value | 96700 |
| Gini index | 0.432 |
| Vacancy rate | 28.83 |
| White | 2422 |
| Black | 1 |
| Asian | 17 |
| Native | 7 |
| Hispanic/Latino | 108 |
| Bachelor's or higher | 467 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
