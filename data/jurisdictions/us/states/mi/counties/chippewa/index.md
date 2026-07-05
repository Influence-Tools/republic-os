---
type: Jurisdiction
title: "Chippewa County, MI"
classification: county
fips: "26033"
state: "MI"
demographics:
  population: 36295
  population_under_18: 6399
  population_18_64: 22782
  population_65_plus: 7114
  median_household_income: 62217
  poverty_rate: 14.04
  homeownership_rate: 75.03
  unemployment_rate: 5.22
  median_home_value: 161900
  gini_index: 0.423
  vacancy_rate: 30.8
  race_white: 24576
  race_black: 2058
  race_asian: 262
  race_native: 4892
  hispanic: 825
  bachelors_plus: 8070
districts:
  - to: "us/states/mi/districts/01"
    rel: in-district
    area_weight: 0.6171
  - to: "us/states/mi/districts/senate/37"
    rel: in-district
    area_weight: 0.3444
  - to: "us/states/mi/districts/senate/38"
    rel: in-district
    area_weight: 0.2613
  - to: "us/states/mi/districts/house/108"
    rel: in-district
    area_weight: 0.3655
  - to: "us/states/mi/districts/house/107"
    rel: in-district
    area_weight: 0.2401
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Chippewa County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 36295 |
| Under 18 | 6399 |
| 18–64 | 22782 |
| 65+ | 7114 |
| Median household income | 62217 |
| Poverty rate | 14.04 |
| Homeownership rate | 75.03 |
| Unemployment rate | 5.22 |
| Median home value | 161900 |
| Gini index | 0.423 |
| Vacancy rate | 30.8 |
| White | 24576 |
| Black | 2058 |
| Asian | 262 |
| Native | 4892 |
| Hispanic/Latino | 825 |
| Bachelor's or higher | 8070 |

## Districts

- [MI-01](/us/states/mi/districts/01.md) — 62% (congressional)
- [MI Senate District 37](/us/states/mi/districts/senate/37.md) — 34% (state senate)
- [MI Senate District 38](/us/states/mi/districts/senate/38.md) — 26% (state senate)
- [MI House District 108](/us/states/mi/districts/house/108.md) — 37% (state house)
- [MI House District 107](/us/states/mi/districts/house/107.md) — 24% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
