---
type: Jurisdiction
title: "Claiborne County, MS"
classification: county
fips: "28021"
state: "MS"
demographics:
  population: 8582
  population_under_18: 1869
  population_18_64: 5045
  population_65_plus: 1668
  median_household_income: 31897
  poverty_rate: 30.67
  homeownership_rate: 76.53
  unemployment_rate: 6.91
  median_home_value: 82700
  gini_index: 0.5522
  vacancy_rate: 24.02
  race_white: 953
  race_black: 7389
  race_asian: 12
  race_native: 10
  hispanic: 25
  bachelors_plus: 1411
districts:
  - to: "us/states/ms/districts/02"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ms/districts/senate/37"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ms/districts/house/85"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Claiborne County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8582 |
| Under 18 | 1869 |
| 18–64 | 5045 |
| 65+ | 1668 |
| Median household income | 31897 |
| Poverty rate | 30.67 |
| Homeownership rate | 76.53 |
| Unemployment rate | 6.91 |
| Median home value | 82700 |
| Gini index | 0.5522 |
| Vacancy rate | 24.02 |
| White | 953 |
| Black | 7389 |
| Asian | 12 |
| Native | 10 |
| Hispanic/Latino | 25 |
| Bachelor's or higher | 1411 |

## Districts

- [MS-02](/us/states/ms/districts/02.md) — 100% (congressional)
- [MS Senate District 37](/us/states/ms/districts/senate/37.md) — 100% (state senate)
- [MS House District 85](/us/states/ms/districts/house/85.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
