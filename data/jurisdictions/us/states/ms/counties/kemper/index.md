---
type: Jurisdiction
title: "Kemper County, MS"
classification: county
fips: "28069"
state: "MS"
demographics:
  population: 8729
  population_under_18: 1610
  population_18_64: 5193
  population_65_plus: 1926
  median_household_income: 46431
  poverty_rate: 24.83
  homeownership_rate: 78.99
  unemployment_rate: 10.82
  median_home_value: 99600
  gini_index: 0.4649
  vacancy_rate: 18.36
  race_white: 2918
  race_black: 5187
  race_asian: 0
  race_native: 240
  hispanic: 106
  bachelors_plus: 1596
districts:
  - to: "us/states/ms/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ms/districts/senate/32"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ms/districts/house/45"
    rel: in-district
    area_weight: 0.6432
  - to: "us/states/ms/districts/house/42"
    rel: in-district
    area_weight: 0.2459
  - to: "us/states/ms/districts/house/83"
    rel: in-district
    area_weight: 0.1107
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Kemper County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8729 |
| Under 18 | 1610 |
| 18–64 | 5193 |
| 65+ | 1926 |
| Median household income | 46431 |
| Poverty rate | 24.83 |
| Homeownership rate | 78.99 |
| Unemployment rate | 10.82 |
| Median home value | 99600 |
| Gini index | 0.4649 |
| Vacancy rate | 18.36 |
| White | 2918 |
| Black | 5187 |
| Asian | 0 |
| Native | 240 |
| Hispanic/Latino | 106 |
| Bachelor's or higher | 1596 |

## Districts

- [MS-03](/us/states/ms/districts/03.md) — 100% (congressional)
- [MS Senate District 32](/us/states/ms/districts/senate/32.md) — 100% (state senate)
- [MS House District 45](/us/states/ms/districts/house/45.md) — 64% (state house)
- [MS House District 42](/us/states/ms/districts/house/42.md) — 25% (state house)
- [MS House District 83](/us/states/ms/districts/house/83.md) — 11% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
