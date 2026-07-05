---
type: Jurisdiction
title: "Cass County, NE"
classification: county
fips: "31025"
state: "NE"
demographics:
  population: 27161
  population_under_18: 6234
  population_18_64: 15832
  population_65_plus: 5095
  median_household_income: 91836
  poverty_rate: 5.22
  homeownership_rate: 85.43
  unemployment_rate: 1.72
  median_home_value: 254900
  gini_index: 0.4031
  vacancy_rate: 8.78
  race_white: 24765
  race_black: 82
  race_asian: 77
  race_native: 68
  hispanic: 1110
  bachelors_plus: 8411
districts:
  - to: "us/states/ne/districts/01"
    rel: in-district
    area_weight: 0.9989
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ne]
timestamp: "2026-07-03"
---

# Cass County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 27161 |
| Under 18 | 6234 |
| 18–64 | 15832 |
| 65+ | 5095 |
| Median household income | 91836 |
| Poverty rate | 5.22 |
| Homeownership rate | 85.43 |
| Unemployment rate | 1.72 |
| Median home value | 254900 |
| Gini index | 0.4031 |
| Vacancy rate | 8.78 |
| White | 24765 |
| Black | 82 |
| Asian | 77 |
| Native | 68 |
| Hispanic/Latino | 1110 |
| Bachelor's or higher | 8411 |

## Districts

- [NE-01](/us/states/ne/districts/01.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
