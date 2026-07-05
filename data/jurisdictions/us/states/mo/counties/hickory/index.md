---
type: Jurisdiction
title: "Hickory County, MO"
classification: county
fips: "29085"
state: "MO"
demographics:
  population: 8585
  population_under_18: 1488
  population_18_64: 4320
  population_65_plus: 2777
  median_household_income: 39390
  poverty_rate: 19.76
  homeownership_rate: 82.45
  unemployment_rate: 13.81
  median_home_value: 176100
  gini_index: 0.4749
  vacancy_rate: 34.29
  race_white: 8108
  race_black: 16
  race_asian: 39
  race_native: 3
  hispanic: 157
  bachelors_plus: 1116
districts:
  - to: "us/states/mo/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/28"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/house/126"
    rel: in-district
    area_weight: 0.5651
  - to: "us/states/mo/districts/house/128"
    rel: in-district
    area_weight: 0.4348
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Hickory County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8585 |
| Under 18 | 1488 |
| 18–64 | 4320 |
| 65+ | 2777 |
| Median household income | 39390 |
| Poverty rate | 19.76 |
| Homeownership rate | 82.45 |
| Unemployment rate | 13.81 |
| Median home value | 176100 |
| Gini index | 0.4749 |
| Vacancy rate | 34.29 |
| White | 8108 |
| Black | 16 |
| Asian | 39 |
| Native | 3 |
| Hispanic/Latino | 157 |
| Bachelor's or higher | 1116 |

## Districts

- [MO-04](/us/states/mo/districts/04.md) — 100% (congressional)
- [MO Senate District 28](/us/states/mo/districts/senate/28.md) — 100% (state senate)
- [MO House District 126](/us/states/mo/districts/house/126.md) — 57% (state house)
- [MO House District 128](/us/states/mo/districts/house/128.md) — 43% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
