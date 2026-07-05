---
type: Jurisdiction
title: "Nuckolls County, NE"
classification: county
fips: "31129"
state: "NE"
demographics:
  population: 4087
  population_under_18: 751
  population_18_64: 2138
  population_65_plus: 1198
  median_household_income: 73976
  poverty_rate: 5.7
  homeownership_rate: 83.48
  unemployment_rate: 0.6
  median_home_value: 96500
  gini_index: 0.4051
  vacancy_rate: 13.56
  race_white: 3835
  race_black: 6
  race_asian: 0
  race_native: 17
  hispanic: 146
  bachelors_plus: 974
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

# Nuckolls County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4087 |
| Under 18 | 751 |
| 18–64 | 2138 |
| 65+ | 1198 |
| Median household income | 73976 |
| Poverty rate | 5.7 |
| Homeownership rate | 83.48 |
| Unemployment rate | 0.6 |
| Median home value | 96500 |
| Gini index | 0.4051 |
| Vacancy rate | 13.56 |
| White | 3835 |
| Black | 6 |
| Asian | 0 |
| Native | 17 |
| Hispanic/Latino | 146 |
| Bachelor's or higher | 974 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
