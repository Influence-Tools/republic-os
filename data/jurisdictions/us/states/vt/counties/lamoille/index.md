---
type: Jurisdiction
title: "Lamoille County, VT"
classification: county
fips: "50015"
state: "VT"
demographics:
  population: 26148
  population_under_18: 5176
  population_18_64: 16079
  population_65_plus: 4893
  median_household_income: 74908
  poverty_rate: 8.51
  homeownership_rate: 72.86
  unemployment_rate: 3.28
  median_home_value: 304700
  gini_index: 0.4591
  vacancy_rate: 16.74
  race_white: 24169
  race_black: 233
  race_asian: 261
  race_native: 58
  hispanic: 661
  bachelors_plus: 11320
districts:
  - to: "us/states/vt/districts/00"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, vt]
timestamp: "2026-07-03"
---

# Lamoille County, VT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 26148 |
| Under 18 | 5176 |
| 18–64 | 16079 |
| 65+ | 4893 |
| Median household income | 74908 |
| Poverty rate | 8.51 |
| Homeownership rate | 72.86 |
| Unemployment rate | 3.28 |
| Median home value | 304700 |
| Gini index | 0.4591 |
| Vacancy rate | 16.74 |
| White | 24169 |
| Black | 233 |
| Asian | 261 |
| Native | 58 |
| Hispanic/Latino | 661 |
| Bachelor's or higher | 11320 |

## Districts

- [VT-00](/us/states/vt/districts/00.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
