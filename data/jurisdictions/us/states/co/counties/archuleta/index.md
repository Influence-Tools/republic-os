---
type: Jurisdiction
title: "Archuleta County, CO"
classification: county
fips: "08007"
state: "CO"
demographics:
  population: 13900
  population_under_18: 2321
  population_18_64: 7582
  population_65_plus: 3997
  median_household_income: 83065
  poverty_rate: 8.19
  homeownership_rate: 80.07
  unemployment_rate: 1.34
  median_home_value: 478100
  gini_index: 0.4312
  vacancy_rate: 39.94
  race_white: 11118
  race_black: 3
  race_asian: 102
  race_native: 332
  hispanic: 2304
  bachelors_plus: 6465
districts:
  - to: "us/states/co/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/co/districts/senate/6"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/co/districts/house/59"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Archuleta County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13900 |
| Under 18 | 2321 |
| 18–64 | 7582 |
| 65+ | 3997 |
| Median household income | 83065 |
| Poverty rate | 8.19 |
| Homeownership rate | 80.07 |
| Unemployment rate | 1.34 |
| Median home value | 478100 |
| Gini index | 0.4312 |
| Vacancy rate | 39.94 |
| White | 11118 |
| Black | 3 |
| Asian | 102 |
| Native | 332 |
| Hispanic/Latino | 2304 |
| Bachelor's or higher | 6465 |

## Districts

- [CO-03](/us/states/co/districts/03.md) — 100% (congressional)
- [CO Senate District 6](/us/states/co/districts/senate/6.md) — 100% (state senate)
- [CO House District 59](/us/states/co/districts/house/59.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
