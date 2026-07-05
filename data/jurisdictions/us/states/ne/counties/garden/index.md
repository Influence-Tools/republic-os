---
type: Jurisdiction
title: "Garden County, NE"
classification: county
fips: "31069"
state: "NE"
demographics:
  population: 1761
  population_under_18: 360
  population_18_64: 879
  population_65_plus: 522
  median_household_income: 41882
  poverty_rate: 16.54
  homeownership_rate: 78.67
  unemployment_rate: 5.42
  median_home_value: 110400
  gini_index: 0.414
  vacancy_rate: 26.85
  race_white: 1650
  race_black: 1
  race_asian: 8
  race_native: 9
  hispanic: 76
  bachelors_plus: 361
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

# Garden County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1761 |
| Under 18 | 360 |
| 18–64 | 879 |
| 65+ | 522 |
| Median household income | 41882 |
| Poverty rate | 16.54 |
| Homeownership rate | 78.67 |
| Unemployment rate | 5.42 |
| Median home value | 110400 |
| Gini index | 0.414 |
| Vacancy rate | 26.85 |
| White | 1650 |
| Black | 1 |
| Asian | 8 |
| Native | 9 |
| Hispanic/Latino | 76 |
| Bachelor's or higher | 361 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
