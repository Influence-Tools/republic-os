---
type: Jurisdiction
title: "Hancock County, MS"
classification: county
fips: "28045"
state: "MS"
demographics:
  population: 46167
  population_under_18: 8875
  population_18_64: 26879
  population_65_plus: 10413
  median_household_income: 67708
  poverty_rate: 13.81
  homeownership_rate: 79.24
  unemployment_rate: 5.02
  median_home_value: 224200
  gini_index: 0.481
  vacancy_rate: 14.67
  race_white: 38845
  race_black: 3352
  race_asian: 464
  race_native: 185
  hispanic: 1943
  bachelors_plus: 12948
districts:
  - to: "us/states/ms/districts/04"
    rel: in-district
    area_weight: 0.8778
  - to: "us/states/ms/districts/senate/46"
    rel: in-district
    area_weight: 0.8607
  - to: "us/states/ms/districts/senate/48"
    rel: in-district
    area_weight: 0.0127
  - to: "us/states/ms/districts/house/122"
    rel: in-district
    area_weight: 0.5372
  - to: "us/states/ms/districts/house/93"
    rel: in-district
    area_weight: 0.2293
  - to: "us/states/ms/districts/house/95"
    rel: in-district
    area_weight: 0.107
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Hancock County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 46167 |
| Under 18 | 8875 |
| 18–64 | 26879 |
| 65+ | 10413 |
| Median household income | 67708 |
| Poverty rate | 13.81 |
| Homeownership rate | 79.24 |
| Unemployment rate | 5.02 |
| Median home value | 224200 |
| Gini index | 0.481 |
| Vacancy rate | 14.67 |
| White | 38845 |
| Black | 3352 |
| Asian | 464 |
| Native | 185 |
| Hispanic/Latino | 1943 |
| Bachelor's or higher | 12948 |

## Districts

- [MS-04](/us/states/ms/districts/04.md) — 88% (congressional)
- [MS Senate District 46](/us/states/ms/districts/senate/46.md) — 86% (state senate)
- [MS Senate District 48](/us/states/ms/districts/senate/48.md) — 1% (state senate)
- [MS House District 122](/us/states/ms/districts/house/122.md) — 54% (state house)
- [MS House District 93](/us/states/ms/districts/house/93.md) — 23% (state house)
- [MS House District 95](/us/states/ms/districts/house/95.md) — 11% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
