---
type: Jurisdiction
title: "Garfield County, NE"
classification: county
fips: "31071"
state: "NE"
demographics:
  population: 1718
  population_under_18: 351
  population_18_64: 862
  population_65_plus: 505
  median_household_income: 62804
  poverty_rate: 8.82
  homeownership_rate: 76.03
  unemployment_rate: 2.73
  median_home_value: 176600
  gini_index: 0.4344
  vacancy_rate: 29.19
  race_white: 1691
  race_black: 4
  race_asian: 0
  race_native: 2
  hispanic: 29
  bachelors_plus: 481
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

# Garfield County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1718 |
| Under 18 | 351 |
| 18–64 | 862 |
| 65+ | 505 |
| Median household income | 62804 |
| Poverty rate | 8.82 |
| Homeownership rate | 76.03 |
| Unemployment rate | 2.73 |
| Median home value | 176600 |
| Gini index | 0.4344 |
| Vacancy rate | 29.19 |
| White | 1691 |
| Black | 4 |
| Asian | 0 |
| Native | 2 |
| Hispanic/Latino | 29 |
| Bachelor's or higher | 481 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
