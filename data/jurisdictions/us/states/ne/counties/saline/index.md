---
type: Jurisdiction
title: "Saline County, NE"
classification: county
fips: "31151"
state: "NE"
demographics:
  population: 14650
  population_under_18: 3830
  population_18_64: 8558
  population_65_plus: 2262
  median_household_income: 79910
  poverty_rate: 8.9
  homeownership_rate: 75.89
  unemployment_rate: 2.91
  median_home_value: 197400
  gini_index: 0.3914
  vacancy_rate: 11.31
  race_white: 10335
  race_black: 61
  race_asian: 346
  race_native: 22
  hispanic: 4321
  bachelors_plus: 2498
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

# Saline County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14650 |
| Under 18 | 3830 |
| 18–64 | 8558 |
| 65+ | 2262 |
| Median household income | 79910 |
| Poverty rate | 8.9 |
| Homeownership rate | 75.89 |
| Unemployment rate | 2.91 |
| Median home value | 197400 |
| Gini index | 0.3914 |
| Vacancy rate | 11.31 |
| White | 10335 |
| Black | 61 |
| Asian | 346 |
| Native | 22 |
| Hispanic/Latino | 4321 |
| Bachelor's or higher | 2498 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
