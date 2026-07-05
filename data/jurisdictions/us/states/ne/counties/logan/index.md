---
type: Jurisdiction
title: "Logan County, NE"
classification: county
fips: "31113"
state: "NE"
demographics:
  population: 773
  population_under_18: 216
  population_18_64: 374
  population_65_plus: 183
  median_household_income: 74271
  poverty_rate: 5.61
  homeownership_rate: 78.93
  unemployment_rate: 0.25
  median_home_value: 175000
  gini_index: 0.489
  vacancy_rate: 9.39
  race_white: 693
  race_black: 13
  race_asian: 0
  race_native: 5
  hispanic: 15
  bachelors_plus: 149
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

# Logan County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 773 |
| Under 18 | 216 |
| 18–64 | 374 |
| 65+ | 183 |
| Median household income | 74271 |
| Poverty rate | 5.61 |
| Homeownership rate | 78.93 |
| Unemployment rate | 0.25 |
| Median home value | 175000 |
| Gini index | 0.489 |
| Vacancy rate | 9.39 |
| White | 693 |
| Black | 13 |
| Asian | 0 |
| Native | 5 |
| Hispanic/Latino | 15 |
| Bachelor's or higher | 149 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
