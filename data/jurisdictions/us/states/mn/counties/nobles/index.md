---
type: Jurisdiction
title: "Nobles County, MN"
classification: county
fips: "27105"
state: "MN"
demographics:
  population: 22041
  population_under_18: 6383
  population_18_64: 11869
  population_65_plus: 3789
  median_household_income: 66101
  poverty_rate: 14.0
  homeownership_rate: 74.17
  unemployment_rate: 3.24
  median_home_value: 197200
  gini_index: 0.4292
  vacancy_rate: 8.6
  race_white: 12383
  race_black: 1148
  race_asian: 934
  race_native: 695
  hispanic: 7594
  bachelors_plus: 3115
districts:
  - to: "us/states/mn/districts/01"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mn/districts/senate/21"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mn/districts/house/21b"
    rel: in-district
    area_weight: 0.5999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Nobles County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 22041 |
| Under 18 | 6383 |
| 18–64 | 11869 |
| 65+ | 3789 |
| Median household income | 66101 |
| Poverty rate | 14.0 |
| Homeownership rate | 74.17 |
| Unemployment rate | 3.24 |
| Median home value | 197200 |
| Gini index | 0.4292 |
| Vacancy rate | 8.6 |
| White | 12383 |
| Black | 1148 |
| Asian | 934 |
| Native | 695 |
| Hispanic/Latino | 7594 |
| Bachelor's or higher | 3115 |

## Districts

- [MN-01](/us/states/mn/districts/01.md) — 100% (congressional)
- [MN Senate District 21](/us/states/mn/districts/senate/21.md) — 100% (state senate)
- [MN House District 21B](/us/states/mn/districts/house/21b.md) — 60% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
