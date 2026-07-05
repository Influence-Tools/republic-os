---
type: Jurisdiction
title: "Furnas County, NE"
classification: county
fips: "31065"
state: "NE"
demographics:
  population: 4568
  population_under_18: 991
  population_18_64: 2390
  population_65_plus: 1187
  median_household_income: 61048
  poverty_rate: 12.97
  homeownership_rate: 76.32
  unemployment_rate: 1.04
  median_home_value: 98400
  gini_index: 0.4407
  vacancy_rate: 20.11
  race_white: 4248
  race_black: 17
  race_asian: 7
  race_native: 46
  hispanic: 232
  bachelors_plus: 1049
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

# Furnas County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4568 |
| Under 18 | 991 |
| 18–64 | 2390 |
| 65+ | 1187 |
| Median household income | 61048 |
| Poverty rate | 12.97 |
| Homeownership rate | 76.32 |
| Unemployment rate | 1.04 |
| Median home value | 98400 |
| Gini index | 0.4407 |
| Vacancy rate | 20.11 |
| White | 4248 |
| Black | 17 |
| Asian | 7 |
| Native | 46 |
| Hispanic/Latino | 232 |
| Bachelor's or higher | 1049 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
