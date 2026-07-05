---
type: Jurisdiction
title: "Hamilton County, NE"
classification: county
fips: "31081"
state: "NE"
demographics:
  population: 9464
  population_under_18: 2282
  population_18_64: 5206
  population_65_plus: 1976
  median_household_income: 83994
  poverty_rate: 5.22
  homeownership_rate: 82.97
  unemployment_rate: 2.29
  median_home_value: 253700
  gini_index: 0.366
  vacancy_rate: 12.22
  race_white: 8724
  race_black: 20
  race_asian: 43
  race_native: 44
  hispanic: 408
  bachelors_plus: 2704
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

# Hamilton County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9464 |
| Under 18 | 2282 |
| 18–64 | 5206 |
| 65+ | 1976 |
| Median household income | 83994 |
| Poverty rate | 5.22 |
| Homeownership rate | 82.97 |
| Unemployment rate | 2.29 |
| Median home value | 253700 |
| Gini index | 0.366 |
| Vacancy rate | 12.22 |
| White | 8724 |
| Black | 20 |
| Asian | 43 |
| Native | 44 |
| Hispanic/Latino | 408 |
| Bachelor's or higher | 2704 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
