---
type: Jurisdiction
title: "Lincoln County, NE"
classification: county
fips: "31111"
state: "NE"
demographics:
  population: 33802
  population_under_18: 7738
  population_18_64: 18938
  population_65_plus: 7126
  median_household_income: 65148
  poverty_rate: 12.36
  homeownership_rate: 65.63
  unemployment_rate: 3.63
  median_home_value: 189500
  gini_index: 0.4078
  vacancy_rate: 10.43
  race_white: 29842
  race_black: 281
  race_asian: 249
  race_native: 628
  hispanic: 3136
  bachelors_plus: 7045
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

# Lincoln County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 33802 |
| Under 18 | 7738 |
| 18–64 | 18938 |
| 65+ | 7126 |
| Median household income | 65148 |
| Poverty rate | 12.36 |
| Homeownership rate | 65.63 |
| Unemployment rate | 3.63 |
| Median home value | 189500 |
| Gini index | 0.4078 |
| Vacancy rate | 10.43 |
| White | 29842 |
| Black | 281 |
| Asian | 249 |
| Native | 628 |
| Hispanic/Latino | 3136 |
| Bachelor's or higher | 7045 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
