---
type: Jurisdiction
title: "Dixon County, NE"
classification: county
fips: "31051"
state: "NE"
demographics:
  population: 5545
  population_under_18: 1402
  population_18_64: 2917
  population_65_plus: 1226
  median_household_income: 72454
  poverty_rate: 7.34
  homeownership_rate: 76.51
  unemployment_rate: 2.37
  median_home_value: 155900
  gini_index: 0.4751
  vacancy_rate: 13.0
  race_white: 4583
  race_black: 18
  race_asian: 4
  race_native: 26
  hispanic: 876
  bachelors_plus: 1075
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

# Dixon County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5545 |
| Under 18 | 1402 |
| 18–64 | 2917 |
| 65+ | 1226 |
| Median household income | 72454 |
| Poverty rate | 7.34 |
| Homeownership rate | 76.51 |
| Unemployment rate | 2.37 |
| Median home value | 155900 |
| Gini index | 0.4751 |
| Vacancy rate | 13.0 |
| White | 4583 |
| Black | 18 |
| Asian | 4 |
| Native | 26 |
| Hispanic/Latino | 876 |
| Bachelor's or higher | 1075 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
