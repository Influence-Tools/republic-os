---
type: Jurisdiction
title: "Doniphan County, KS"
classification: county
fips: "20043"
state: "KS"
demographics:
  population: 7503
  population_under_18: 1583
  population_18_64: 4407
  population_65_plus: 1513
  median_household_income: 74028
  poverty_rate: 9.65
  homeownership_rate: 81.06
  unemployment_rate: 1.64
  median_home_value: 135200
  gini_index: 0.4132
  vacancy_rate: 19.24
  race_white: 6752
  race_black: 246
  race_asian: 8
  race_native: 25
  hispanic: 260
  bachelors_plus: 1591
districts:
  - to: "us/states/ks/districts/02"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/ks/districts/senate/1"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/ks/districts/house/63"
    rel: in-district
    area_weight: 0.9991
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Doniphan County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7503 |
| Under 18 | 1583 |
| 18–64 | 4407 |
| 65+ | 1513 |
| Median household income | 74028 |
| Poverty rate | 9.65 |
| Homeownership rate | 81.06 |
| Unemployment rate | 1.64 |
| Median home value | 135200 |
| Gini index | 0.4132 |
| Vacancy rate | 19.24 |
| White | 6752 |
| Black | 246 |
| Asian | 8 |
| Native | 25 |
| Hispanic/Latino | 260 |
| Bachelor's or higher | 1591 |

## Districts

- [KS-02](/us/states/ks/districts/02.md) — 100% (congressional)
- [KS Senate District 1](/us/states/ks/districts/senate/1.md) — 100% (state senate)
- [KS House District 63](/us/states/ks/districts/house/63.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
