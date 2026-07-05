---
type: Jurisdiction
title: "Holt County, NE"
classification: county
fips: "31089"
state: "NE"
demographics:
  population: 10102
  population_under_18: 2603
  population_18_64: 5187
  population_65_plus: 2312
  median_household_income: 68513
  poverty_rate: 11.69
  homeownership_rate: 72.27
  unemployment_rate: 0.85
  median_home_value: 165100
  gini_index: 0.4905
  vacancy_rate: 17.35
  race_white: 9279
  race_black: 42
  race_asian: 17
  race_native: 22
  hispanic: 576
  bachelors_plus: 2603
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

# Holt County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10102 |
| Under 18 | 2603 |
| 18–64 | 5187 |
| 65+ | 2312 |
| Median household income | 68513 |
| Poverty rate | 11.69 |
| Homeownership rate | 72.27 |
| Unemployment rate | 0.85 |
| Median home value | 165100 |
| Gini index | 0.4905 |
| Vacancy rate | 17.35 |
| White | 9279 |
| Black | 42 |
| Asian | 17 |
| Native | 22 |
| Hispanic/Latino | 576 |
| Bachelor's or higher | 2603 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
