---
type: Jurisdiction
title: "Knox County, NE"
classification: county
fips: "31107"
state: "NE"
demographics:
  population: 8363
  population_under_18: 2013
  population_18_64: 4191
  population_65_plus: 2159
  median_household_income: 64636
  poverty_rate: 13.68
  homeownership_rate: 78.43
  unemployment_rate: 3.6
  median_home_value: 127700
  gini_index: 0.4233
  vacancy_rate: 24.31
  race_white: 7173
  race_black: 56
  race_asian: 36
  race_native: 780
  hispanic: 246
  bachelors_plus: 1455
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

# Knox County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8363 |
| Under 18 | 2013 |
| 18–64 | 4191 |
| 65+ | 2159 |
| Median household income | 64636 |
| Poverty rate | 13.68 |
| Homeownership rate | 78.43 |
| Unemployment rate | 3.6 |
| Median home value | 127700 |
| Gini index | 0.4233 |
| Vacancy rate | 24.31 |
| White | 7173 |
| Black | 56 |
| Asian | 36 |
| Native | 780 |
| Hispanic/Latino | 246 |
| Bachelor's or higher | 1455 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
