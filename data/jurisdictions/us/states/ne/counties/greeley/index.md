---
type: Jurisdiction
title: "Greeley County, NE"
classification: county
fips: "31077"
state: "NE"
demographics:
  population: 2202
  population_under_18: 509
  population_18_64: 1122
  population_65_plus: 571
  median_household_income: 63929
  poverty_rate: 13.08
  homeownership_rate: 81.73
  unemployment_rate: 3.52
  median_home_value: 120000
  gini_index: 0.4174
  vacancy_rate: 21.15
  race_white: 2037
  race_black: 13
  race_asian: 0
  race_native: 9
  hispanic: 68
  bachelors_plus: 433
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

# Greeley County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2202 |
| Under 18 | 509 |
| 18–64 | 1122 |
| 65+ | 571 |
| Median household income | 63929 |
| Poverty rate | 13.08 |
| Homeownership rate | 81.73 |
| Unemployment rate | 3.52 |
| Median home value | 120000 |
| Gini index | 0.4174 |
| Vacancy rate | 21.15 |
| White | 2037 |
| Black | 13 |
| Asian | 0 |
| Native | 9 |
| Hispanic/Latino | 68 |
| Bachelor's or higher | 433 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
