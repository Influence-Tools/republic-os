---
type: Jurisdiction
title: "Pawnee County, NE"
classification: county
fips: "31133"
state: "NE"
demographics:
  population: 2530
  population_under_18: 621
  population_18_64: 1191
  population_65_plus: 718
  median_household_income: 62188
  poverty_rate: 13.55
  homeownership_rate: 80.18
  unemployment_rate: 2.23
  median_home_value: 79400
  gini_index: 0.442
  vacancy_rate: 22.64
  race_white: 2403
  race_black: 3
  race_asian: 0
  race_native: 0
  hispanic: 49
  bachelors_plus: 518
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

# Pawnee County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2530 |
| Under 18 | 621 |
| 18–64 | 1191 |
| 65+ | 718 |
| Median household income | 62188 |
| Poverty rate | 13.55 |
| Homeownership rate | 80.18 |
| Unemployment rate | 2.23 |
| Median home value | 79400 |
| Gini index | 0.442 |
| Vacancy rate | 22.64 |
| White | 2403 |
| Black | 3 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 49 |
| Bachelor's or higher | 518 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
