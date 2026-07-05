---
type: Jurisdiction
title: "Marshall County, MN"
classification: county
fips: "27089"
state: "MN"
demographics:
  population: 8909
  population_under_18: 2080
  population_18_64: 4778
  population_65_plus: 2051
  median_household_income: 72543
  poverty_rate: 8.3
  homeownership_rate: 83.02
  unemployment_rate: 3.47
  median_home_value: 164500
  gini_index: 0.3876
  vacancy_rate: 13.99
  race_white: 8176
  race_black: 33
  race_asian: 30
  race_native: 22
  hispanic: 431
  bachelors_plus: 1397
districts:
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 0.9969
  - to: "us/states/mn/districts/senate/1"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mn/districts/house/1a"
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

# Marshall County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8909 |
| Under 18 | 2080 |
| 18–64 | 4778 |
| 65+ | 2051 |
| Median household income | 72543 |
| Poverty rate | 8.3 |
| Homeownership rate | 83.02 |
| Unemployment rate | 3.47 |
| Median home value | 164500 |
| Gini index | 0.3876 |
| Vacancy rate | 13.99 |
| White | 8176 |
| Black | 33 |
| Asian | 30 |
| Native | 22 |
| Hispanic/Latino | 431 |
| Bachelor's or higher | 1397 |

## Districts

- [MN-07](/us/states/mn/districts/07.md) — 100% (congressional)
- [MN Senate District 1](/us/states/mn/districts/senate/1.md) — 100% (state senate)
- [MN House District 1A](/us/states/mn/districts/house/1a.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
