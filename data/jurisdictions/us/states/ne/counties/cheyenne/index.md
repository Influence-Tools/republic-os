---
type: Jurisdiction
title: "Cheyenne County, NE"
classification: county
fips: "31033"
state: "NE"
demographics:
  population: 9533
  population_under_18: 2080
  population_18_64: 5357
  population_65_plus: 2096
  median_household_income: 60348
  poverty_rate: 14.27
  homeownership_rate: 66.73
  unemployment_rate: 3.39
  median_home_value: 139700
  gini_index: 0.4427
  vacancy_rate: 8.67
  race_white: 8674
  race_black: 79
  race_asian: 127
  race_native: 35
  hispanic: 827
  bachelors_plus: 2125
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

# Cheyenne County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9533 |
| Under 18 | 2080 |
| 18–64 | 5357 |
| 65+ | 2096 |
| Median household income | 60348 |
| Poverty rate | 14.27 |
| Homeownership rate | 66.73 |
| Unemployment rate | 3.39 |
| Median home value | 139700 |
| Gini index | 0.4427 |
| Vacancy rate | 8.67 |
| White | 8674 |
| Black | 79 |
| Asian | 127 |
| Native | 35 |
| Hispanic/Latino | 827 |
| Bachelor's or higher | 2125 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
