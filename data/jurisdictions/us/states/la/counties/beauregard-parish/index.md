---
type: Jurisdiction
title: "Beauregard Parish, LA"
classification: county
fips: "22011"
state: "LA"
demographics:
  population: 36676
  population_under_18: 9261
  population_18_64: 21439
  population_65_plus: 5976
  median_household_income: 65944
  poverty_rate: 14.35
  homeownership_rate: 84.82
  unemployment_rate: 6.82
  median_home_value: 161700
  gini_index: 0.4295
  vacancy_rate: 14.75
  race_white: 29325
  race_black: 4064
  race_asian: 270
  race_native: 60
  hispanic: 1438
  bachelors_plus: 5524
districts:
  - to: "us/states/la/districts/04"
    rel: in-district
    area_weight: 0.9978
  - to: "us/states/la/districts/senate/30"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/la/districts/house/24"
    rel: in-district
    area_weight: 0.441
  - to: "us/states/la/districts/house/32"
    rel: in-district
    area_weight: 0.3251
  - to: "us/states/la/districts/house/30"
    rel: in-district
    area_weight: 0.1341
  - to: "us/states/la/districts/house/35"
    rel: in-district
    area_weight: 0.0996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Beauregard Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 36676 |
| Under 18 | 9261 |
| 18–64 | 21439 |
| 65+ | 5976 |
| Median household income | 65944 |
| Poverty rate | 14.35 |
| Homeownership rate | 84.82 |
| Unemployment rate | 6.82 |
| Median home value | 161700 |
| Gini index | 0.4295 |
| Vacancy rate | 14.75 |
| White | 29325 |
| Black | 4064 |
| Asian | 270 |
| Native | 60 |
| Hispanic/Latino | 1438 |
| Bachelor's or higher | 5524 |

## Districts

- [LA-04](/us/states/la/districts/04.md) — 100% (congressional)
- [LA Senate District 30](/us/states/la/districts/senate/30.md) — 100% (state senate)
- [LA House District 24](/us/states/la/districts/house/24.md) — 44% (state house)
- [LA House District 32](/us/states/la/districts/house/32.md) — 33% (state house)
- [LA House District 30](/us/states/la/districts/house/30.md) — 13% (state house)
- [LA House District 35](/us/states/la/districts/house/35.md) — 10% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
