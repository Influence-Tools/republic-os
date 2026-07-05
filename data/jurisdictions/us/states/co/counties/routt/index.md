---
type: Jurisdiction
title: "Routt County, CO"
classification: county
fips: "08107"
state: "CO"
demographics:
  population: 25084
  population_under_18: 4312
  population_18_64: 16135
  population_65_plus: 4637
  median_household_income: 106489
  poverty_rate: 5.15
  homeownership_rate: 76.0
  unemployment_rate: 2.41
  median_home_value: 854700
  gini_index: 0.4725
  vacancy_rate: 34.29
  race_white: 20356
  race_black: 78
  race_asian: 152
  race_native: 165
  hispanic: 2267
  bachelors_plus: 14253
districts:
  - to: "us/states/co/districts/02"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/co/districts/senate/8"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/co/districts/house/26"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Routt County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25084 |
| Under 18 | 4312 |
| 18–64 | 16135 |
| 65+ | 4637 |
| Median household income | 106489 |
| Poverty rate | 5.15 |
| Homeownership rate | 76.0 |
| Unemployment rate | 2.41 |
| Median home value | 854700 |
| Gini index | 0.4725 |
| Vacancy rate | 34.29 |
| White | 20356 |
| Black | 78 |
| Asian | 152 |
| Native | 165 |
| Hispanic/Latino | 2267 |
| Bachelor's or higher | 14253 |

## Districts

- [CO-02](/us/states/co/districts/02.md) — 100% (congressional)
- [CO Senate District 8](/us/states/co/districts/senate/8.md) — 100% (state senate)
- [CO House District 26](/us/states/co/districts/house/26.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
