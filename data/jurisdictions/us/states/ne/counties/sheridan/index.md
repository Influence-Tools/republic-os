---
type: Jurisdiction
title: "Sheridan County, NE"
classification: county
fips: "31161"
state: "NE"
demographics:
  population: 5014
  population_under_18: 1070
  population_18_64: 2554
  population_65_plus: 1390
  median_household_income: 60121
  poverty_rate: 11.27
  homeownership_rate: 74.15
  unemployment_rate: 1.96
  median_home_value: 113400
  gini_index: 0.4662
  vacancy_rate: 22.04
  race_white: 4075
  race_black: 40
  race_asian: 70
  race_native: 506
  hispanic: 270
  bachelors_plus: 1086
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

# Sheridan County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5014 |
| Under 18 | 1070 |
| 18–64 | 2554 |
| 65+ | 1390 |
| Median household income | 60121 |
| Poverty rate | 11.27 |
| Homeownership rate | 74.15 |
| Unemployment rate | 1.96 |
| Median home value | 113400 |
| Gini index | 0.4662 |
| Vacancy rate | 22.04 |
| White | 4075 |
| Black | 40 |
| Asian | 70 |
| Native | 506 |
| Hispanic/Latino | 270 |
| Bachelor's or higher | 1086 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
