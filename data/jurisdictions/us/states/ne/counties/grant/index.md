---
type: Jurisdiction
title: "Grant County, NE"
classification: county
fips: "31075"
state: "NE"
demographics:
  population: 626
  population_under_18: 148
  population_18_64: 342
  population_65_plus: 136
  median_household_income: 70147
  poverty_rate: 12.16
  homeownership_rate: 70.77
  unemployment_rate: 0.3
  median_home_value: 136700
  gini_index: 0.4464
  vacancy_rate: 30.22
  race_white: 601
  race_black: 1
  race_asian: 5
  race_native: 6
  hispanic: 1
  bachelors_plus: 150
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

# Grant County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 626 |
| Under 18 | 148 |
| 18–64 | 342 |
| 65+ | 136 |
| Median household income | 70147 |
| Poverty rate | 12.16 |
| Homeownership rate | 70.77 |
| Unemployment rate | 0.3 |
| Median home value | 136700 |
| Gini index | 0.4464 |
| Vacancy rate | 30.22 |
| White | 601 |
| Black | 1 |
| Asian | 5 |
| Native | 6 |
| Hispanic/Latino | 1 |
| Bachelor's or higher | 150 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
