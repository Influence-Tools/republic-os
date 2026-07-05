---
type: Jurisdiction
title: "Treutlen County, GA"
classification: county
fips: "13283"
state: "GA"
demographics:
  population: 6376
  population_under_18: 1393
  population_18_64: 3791
  population_65_plus: 1192
  median_household_income: 55518
  poverty_rate: 13.79
  homeownership_rate: 65.33
  unemployment_rate: 7.73
  median_home_value: 100100
  gini_index: 0.4329
  vacancy_rate: 16.78
  race_white: 4018
  race_black: 1952
  race_asian: 9
  race_native: 95
  hispanic: 93
  bachelors_plus: 583
districts:
  - to: "us/states/ga/districts/12"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/senate/20"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ga/districts/house/158"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Treutlen County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6376 |
| Under 18 | 1393 |
| 18–64 | 3791 |
| 65+ | 1192 |
| Median household income | 55518 |
| Poverty rate | 13.79 |
| Homeownership rate | 65.33 |
| Unemployment rate | 7.73 |
| Median home value | 100100 |
| Gini index | 0.4329 |
| Vacancy rate | 16.78 |
| White | 4018 |
| Black | 1952 |
| Asian | 9 |
| Native | 95 |
| Hispanic/Latino | 93 |
| Bachelor's or higher | 583 |

## Districts

- [GA-12](/us/states/ga/districts/12.md) — 100% (congressional)
- [GA Senate District 20](/us/states/ga/districts/senate/20.md) — 100% (state senate)
- [GA House District 158](/us/states/ga/districts/house/158.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
