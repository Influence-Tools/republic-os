---
type: Jurisdiction
title: "Nemaha County, NE"
classification: county
fips: "31127"
state: "NE"
demographics:
  population: 7046
  population_under_18: 1569
  population_18_64: 4057
  population_65_plus: 1420
  median_household_income: 60924
  poverty_rate: 13.29
  homeownership_rate: 65.86
  unemployment_rate: 6.01
  median_home_value: 131700
  gini_index: 0.4652
  vacancy_rate: 14.14
  race_white: 6321
  race_black: 88
  race_asian: 10
  race_native: 59
  hispanic: 229
  bachelors_plus: 1823
districts:
  - to: "us/states/ne/districts/03"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ne]
timestamp: "2026-07-03"
---

# Nemaha County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7046 |
| Under 18 | 1569 |
| 18–64 | 4057 |
| 65+ | 1420 |
| Median household income | 60924 |
| Poverty rate | 13.29 |
| Homeownership rate | 65.86 |
| Unemployment rate | 6.01 |
| Median home value | 131700 |
| Gini index | 0.4652 |
| Vacancy rate | 14.14 |
| White | 6321 |
| Black | 88 |
| Asian | 10 |
| Native | 59 |
| Hispanic/Latino | 229 |
| Bachelor's or higher | 1823 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
