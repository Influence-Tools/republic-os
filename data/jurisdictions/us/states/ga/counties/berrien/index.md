---
type: Jurisdiction
title: "Berrien County, GA"
classification: county
fips: "13019"
state: "GA"
demographics:
  population: 18352
  population_under_18: 4292
  population_18_64: 10838
  population_65_plus: 3222
  median_household_income: 52876
  poverty_rate: 20.58
  homeownership_rate: 70.96
  unemployment_rate: 3.67
  median_home_value: 131600
  gini_index: 0.465
  vacancy_rate: 13.01
  race_white: 14987
  race_black: 2054
  race_asian: 22
  race_native: 31
  hispanic: 1127
  bachelors_plus: 2643
districts:
  - to: "us/states/ga/districts/08"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/senate/13"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/ga/districts/house/170"
    rel: in-district
    area_weight: 0.9991
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Berrien County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18352 |
| Under 18 | 4292 |
| 18–64 | 10838 |
| 65+ | 3222 |
| Median household income | 52876 |
| Poverty rate | 20.58 |
| Homeownership rate | 70.96 |
| Unemployment rate | 3.67 |
| Median home value | 131600 |
| Gini index | 0.465 |
| Vacancy rate | 13.01 |
| White | 14987 |
| Black | 2054 |
| Asian | 22 |
| Native | 31 |
| Hispanic/Latino | 1127 |
| Bachelor's or higher | 2643 |

## Districts

- [GA-08](/us/states/ga/districts/08.md) — 100% (congressional)
- [GA Senate District 13](/us/states/ga/districts/senate/13.md) — 100% (state senate)
- [GA House District 170](/us/states/ga/districts/house/170.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
