---
type: Jurisdiction
title: "Echols County, GA"
classification: county
fips: "13101"
state: "GA"
demographics:
  population: 3709
  population_under_18: 1123
  population_18_64: 2130
  population_65_plus: 456
  median_household_income: 59489
  poverty_rate: 14.21
  homeownership_rate: 75.9
  unemployment_rate: 1.71
  median_home_value: 124100
  gini_index: 0.4488
  vacancy_rate: 15.5
  race_white: 2363
  race_black: 232
  race_asian: 294
  race_native: 4
  hispanic: 782
  bachelors_plus: 476
districts:
  - to: "us/states/ga/districts/08"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ga/districts/senate/8"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ga/districts/house/174"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Echols County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3709 |
| Under 18 | 1123 |
| 18–64 | 2130 |
| 65+ | 456 |
| Median household income | 59489 |
| Poverty rate | 14.21 |
| Homeownership rate | 75.9 |
| Unemployment rate | 1.71 |
| Median home value | 124100 |
| Gini index | 0.4488 |
| Vacancy rate | 15.5 |
| White | 2363 |
| Black | 232 |
| Asian | 294 |
| Native | 4 |
| Hispanic/Latino | 782 |
| Bachelor's or higher | 476 |

## Districts

- [GA-08](/us/states/ga/districts/08.md) — 100% (congressional)
- [GA Senate District 8](/us/states/ga/districts/senate/8.md) — 100% (state senate)
- [GA House District 174](/us/states/ga/districts/house/174.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
