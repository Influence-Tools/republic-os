---
type: Jurisdiction
title: "Saline County, KS"
classification: county
fips: "20169"
state: "KS"
demographics:
  population: 53668
  population_under_18: 12185
  population_18_64: 31387
  population_65_plus: 10096
  median_household_income: 65422
  poverty_rate: 11.86
  homeownership_rate: 67.14
  unemployment_rate: 4.82
  median_home_value: 179600
  gini_index: 0.4664
  vacancy_rate: 6.76
  race_white: 44054
  race_black: 1960
  race_asian: 927
  race_native: 268
  hispanic: 6843
  bachelors_plus: 14243
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/24"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ks/districts/house/69"
    rel: in-district
    area_weight: 0.5348
  - to: "us/states/ks/districts/house/107"
    rel: in-district
    area_weight: 0.2513
  - to: "us/states/ks/districts/house/71"
    rel: in-district
    area_weight: 0.2137
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Saline County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 53668 |
| Under 18 | 12185 |
| 18–64 | 31387 |
| 65+ | 10096 |
| Median household income | 65422 |
| Poverty rate | 11.86 |
| Homeownership rate | 67.14 |
| Unemployment rate | 4.82 |
| Median home value | 179600 |
| Gini index | 0.4664 |
| Vacancy rate | 6.76 |
| White | 44054 |
| Black | 1960 |
| Asian | 927 |
| Native | 268 |
| Hispanic/Latino | 6843 |
| Bachelor's or higher | 14243 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 24](/us/states/ks/districts/senate/24.md) — 100% (state senate)
- [KS House District 69](/us/states/ks/districts/house/69.md) — 53% (state house)
- [KS House District 107](/us/states/ks/districts/house/107.md) — 25% (state house)
- [KS House District 71](/us/states/ks/districts/house/71.md) — 21% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
