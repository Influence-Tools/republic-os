---
type: Jurisdiction
title: "Wayne County, NE"
classification: county
fips: "31179"
state: "NE"
demographics:
  population: 9844
  population_under_18: 2001
  population_18_64: 6193
  population_65_plus: 1650
  median_household_income: 66215
  poverty_rate: 13.18
  homeownership_rate: 61.26
  unemployment_rate: 4.34
  median_home_value: 221600
  gini_index: 0.4437
  vacancy_rate: 5.96
  race_white: 8496
  race_black: 101
  race_asian: 30
  race_native: 90
  hispanic: 1012
  bachelors_plus: 2255
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

# Wayne County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9844 |
| Under 18 | 2001 |
| 18–64 | 6193 |
| 65+ | 1650 |
| Median household income | 66215 |
| Poverty rate | 13.18 |
| Homeownership rate | 61.26 |
| Unemployment rate | 4.34 |
| Median home value | 221600 |
| Gini index | 0.4437 |
| Vacancy rate | 5.96 |
| White | 8496 |
| Black | 101 |
| Asian | 30 |
| Native | 90 |
| Hispanic/Latino | 1012 |
| Bachelor's or higher | 2255 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
