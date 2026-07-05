---
type: Jurisdiction
title: "Atkinson County, GA"
classification: county
fips: "13003"
state: "GA"
demographics:
  population: 8337
  population_under_18: 2110
  population_18_64: 5041
  population_65_plus: 1186
  median_household_income: 42347
  poverty_rate: 24.97
  homeownership_rate: 61.89
  unemployment_rate: 4.78
  median_home_value: 79000
  gini_index: 0.4363
  vacancy_rate: 8.73
  race_white: 5269
  race_black: 1136
  race_asian: 0
  race_native: 0
  hispanic: 2295
  bachelors_plus: 710
districts:
  - to: "us/states/ga/districts/08"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/ga/districts/senate/8"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ga/districts/house/176"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Atkinson County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8337 |
| Under 18 | 2110 |
| 18–64 | 5041 |
| 65+ | 1186 |
| Median household income | 42347 |
| Poverty rate | 24.97 |
| Homeownership rate | 61.89 |
| Unemployment rate | 4.78 |
| Median home value | 79000 |
| Gini index | 0.4363 |
| Vacancy rate | 8.73 |
| White | 5269 |
| Black | 1136 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 2295 |
| Bachelor's or higher | 710 |

## Districts

- [GA-08](/us/states/ga/districts/08.md) — 100% (congressional)
- [GA Senate District 8](/us/states/ga/districts/senate/8.md) — 100% (state senate)
- [GA House District 176](/us/states/ga/districts/house/176.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
