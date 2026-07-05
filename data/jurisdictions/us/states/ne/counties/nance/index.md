---
type: Jurisdiction
title: "Nance County, NE"
classification: county
fips: "31125"
state: "NE"
demographics:
  population: 3324
  population_under_18: 792
  population_18_64: 1820
  population_65_plus: 712
  median_household_income: 65179
  poverty_rate: 16.63
  homeownership_rate: 72.88
  unemployment_rate: 3.62
  median_home_value: 132000
  gini_index: 0.42
  vacancy_rate: 16.44
  race_white: 3138
  race_black: 5
  race_asian: 5
  race_native: 19
  hispanic: 85
  bachelors_plus: 581
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

# Nance County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3324 |
| Under 18 | 792 |
| 18–64 | 1820 |
| 65+ | 712 |
| Median household income | 65179 |
| Poverty rate | 16.63 |
| Homeownership rate | 72.88 |
| Unemployment rate | 3.62 |
| Median home value | 132000 |
| Gini index | 0.42 |
| Vacancy rate | 16.44 |
| White | 3138 |
| Black | 5 |
| Asian | 5 |
| Native | 19 |
| Hispanic/Latino | 85 |
| Bachelor's or higher | 581 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
