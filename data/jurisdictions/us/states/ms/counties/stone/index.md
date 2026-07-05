---
type: Jurisdiction
title: "Stone County, MS"
classification: county
fips: "28131"
state: "MS"
demographics:
  population: 18894
  population_under_18: 4007
  population_18_64: 11602
  population_65_plus: 3285
  median_household_income: 61413
  poverty_rate: 16.87
  homeownership_rate: 80.67
  unemployment_rate: 9.32
  median_home_value: 161100
  gini_index: 0.3945
  vacancy_rate: 12.58
  race_white: 14342
  race_black: 3271
  race_asian: 91
  race_native: 26
  hispanic: 496
  bachelors_plus: 2921
districts:
  - to: "us/states/ms/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ms/districts/senate/47"
    rel: in-district
    area_weight: 0.7433
  - to: "us/states/ms/districts/senate/40"
    rel: in-district
    area_weight: 0.2566
  - to: "us/states/ms/districts/house/107"
    rel: in-district
    area_weight: 0.5544
  - to: "us/states/ms/districts/house/93"
    rel: in-district
    area_weight: 0.4455
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Stone County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18894 |
| Under 18 | 4007 |
| 18–64 | 11602 |
| 65+ | 3285 |
| Median household income | 61413 |
| Poverty rate | 16.87 |
| Homeownership rate | 80.67 |
| Unemployment rate | 9.32 |
| Median home value | 161100 |
| Gini index | 0.3945 |
| Vacancy rate | 12.58 |
| White | 14342 |
| Black | 3271 |
| Asian | 91 |
| Native | 26 |
| Hispanic/Latino | 496 |
| Bachelor's or higher | 2921 |

## Districts

- [MS-04](/us/states/ms/districts/04.md) — 100% (congressional)
- [MS Senate District 47](/us/states/ms/districts/senate/47.md) — 74% (state senate)
- [MS Senate District 40](/us/states/ms/districts/senate/40.md) — 26% (state senate)
- [MS House District 107](/us/states/ms/districts/house/107.md) — 55% (state house)
- [MS House District 93](/us/states/ms/districts/house/93.md) — 45% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
