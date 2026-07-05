---
type: Jurisdiction
title: "Hooker County, NE"
classification: county
fips: "31091"
state: "NE"
demographics:
  population: 647
  population_under_18: 123
  population_18_64: 386
  population_65_plus: 138
  median_household_income: 49464
  poverty_rate: 6.23
  homeownership_rate: 55.35
  unemployment_rate: 3.92
  median_home_value: 93800
  gini_index: 0.3714
  vacancy_rate: 23.6
  race_white: 575
  race_black: 10
  race_asian: 0
  race_native: 1
  hispanic: 0
  bachelors_plus: 113
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

# Hooker County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 647 |
| Under 18 | 123 |
| 18–64 | 386 |
| 65+ | 138 |
| Median household income | 49464 |
| Poverty rate | 6.23 |
| Homeownership rate | 55.35 |
| Unemployment rate | 3.92 |
| Median home value | 93800 |
| Gini index | 0.3714 |
| Vacancy rate | 23.6 |
| White | 575 |
| Black | 10 |
| Asian | 0 |
| Native | 1 |
| Hispanic/Latino | 0 |
| Bachelor's or higher | 113 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
