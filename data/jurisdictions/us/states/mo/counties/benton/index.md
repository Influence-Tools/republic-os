---
type: Jurisdiction
title: "Benton County, MO"
classification: county
fips: "29015"
state: "MO"
demographics:
  population: 20151
  population_under_18: 3486
  population_18_64: 10343
  population_65_plus: 6322
  median_household_income: 52567
  poverty_rate: 19.87
  homeownership_rate: 83.83
  unemployment_rate: 3.78
  median_home_value: 177900
  gini_index: 0.476
  vacancy_rate: 36.94
  race_white: 18542
  race_black: 193
  race_asian: 32
  race_native: 86
  hispanic: 411
  bachelors_plus: 3407
districts:
  - to: "us/states/mo/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/28"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/house/57"
    rel: in-district
    area_weight: 0.8342
  - to: "us/states/mo/districts/house/126"
    rel: in-district
    area_weight: 0.1657
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Benton County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20151 |
| Under 18 | 3486 |
| 18–64 | 10343 |
| 65+ | 6322 |
| Median household income | 52567 |
| Poverty rate | 19.87 |
| Homeownership rate | 83.83 |
| Unemployment rate | 3.78 |
| Median home value | 177900 |
| Gini index | 0.476 |
| Vacancy rate | 36.94 |
| White | 18542 |
| Black | 193 |
| Asian | 32 |
| Native | 86 |
| Hispanic/Latino | 411 |
| Bachelor's or higher | 3407 |

## Districts

- [MO-04](/us/states/mo/districts/04.md) — 100% (congressional)
- [MO Senate District 28](/us/states/mo/districts/senate/28.md) — 100% (state senate)
- [MO House District 57](/us/states/mo/districts/house/57.md) — 83% (state house)
- [MO House District 126](/us/states/mo/districts/house/126.md) — 17% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
