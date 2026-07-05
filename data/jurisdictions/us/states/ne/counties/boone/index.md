---
type: Jurisdiction
title: "Boone County, NE"
classification: county
fips: "31011"
state: "NE"
demographics:
  population: 5356
  population_under_18: 1313
  population_18_64: 2767
  population_65_plus: 1276
  median_household_income: 74947
  poverty_rate: 9.64
  homeownership_rate: 81.88
  unemployment_rate: 1.21
  median_home_value: 173700
  gini_index: 0.4326
  vacancy_rate: 14.25
  race_white: 5039
  race_black: 1
  race_asian: 10
  race_native: 46
  hispanic: 229
  bachelors_plus: 934
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

# Boone County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5356 |
| Under 18 | 1313 |
| 18–64 | 2767 |
| 65+ | 1276 |
| Median household income | 74947 |
| Poverty rate | 9.64 |
| Homeownership rate | 81.88 |
| Unemployment rate | 1.21 |
| Median home value | 173700 |
| Gini index | 0.4326 |
| Vacancy rate | 14.25 |
| White | 5039 |
| Black | 1 |
| Asian | 10 |
| Native | 46 |
| Hispanic/Latino | 229 |
| Bachelor's or higher | 934 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
