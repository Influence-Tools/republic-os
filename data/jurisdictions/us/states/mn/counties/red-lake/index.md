---
type: Jurisdiction
title: "Red Lake County, MN"
classification: county
fips: "27125"
state: "MN"
demographics:
  population: 3915
  population_under_18: 947
  population_18_64: 2076
  population_65_plus: 892
  median_household_income: 77188
  poverty_rate: 7.2
  homeownership_rate: 83.42
  unemployment_rate: 1.08
  median_home_value: 162000
  gini_index: 0.3838
  vacancy_rate: 11.02
  race_white: 3602
  race_black: 19
  race_asian: 14
  race_native: 68
  hispanic: 141
  bachelors_plus: 614
districts:
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mn/districts/senate/1"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mn/districts/house/1b"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Red Lake County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3915 |
| Under 18 | 947 |
| 18–64 | 2076 |
| 65+ | 892 |
| Median household income | 77188 |
| Poverty rate | 7.2 |
| Homeownership rate | 83.42 |
| Unemployment rate | 1.08 |
| Median home value | 162000 |
| Gini index | 0.3838 |
| Vacancy rate | 11.02 |
| White | 3602 |
| Black | 19 |
| Asian | 14 |
| Native | 68 |
| Hispanic/Latino | 141 |
| Bachelor's or higher | 614 |

## Districts

- [MN-07](/us/states/mn/districts/07.md) — 100% (congressional)
- [MN Senate District 1](/us/states/mn/districts/senate/1.md) — 100% (state senate)
- [MN House District 1B](/us/states/mn/districts/house/1b.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
