---
type: Jurisdiction
title: "Gilpin County, CO"
classification: county
fips: "08047"
state: "CO"
demographics:
  population: 5901
  population_under_18: 967
  population_18_64: 3619
  population_65_plus: 1315
  median_household_income: 95361
  poverty_rate: 11.18
  homeownership_rate: 87.51
  unemployment_rate: 3.1
  median_home_value: 573900
  gini_index: 0.4297
  vacancy_rate: 16.66
  race_white: 5179
  race_black: 152
  race_asian: 62
  race_native: 65
  hispanic: 436
  bachelors_plus: 3765
districts:
  - to: "us/states/co/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/co/districts/senate/8"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/co/districts/house/49"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Gilpin County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5901 |
| Under 18 | 967 |
| 18–64 | 3619 |
| 65+ | 1315 |
| Median household income | 95361 |
| Poverty rate | 11.18 |
| Homeownership rate | 87.51 |
| Unemployment rate | 3.1 |
| Median home value | 573900 |
| Gini index | 0.4297 |
| Vacancy rate | 16.66 |
| White | 5179 |
| Black | 152 |
| Asian | 62 |
| Native | 65 |
| Hispanic/Latino | 436 |
| Bachelor's or higher | 3765 |

## Districts

- [CO-02](/us/states/co/districts/02.md) — 100% (congressional)
- [CO Senate District 8](/us/states/co/districts/senate/8.md) — 100% (state senate)
- [CO House District 49](/us/states/co/districts/house/49.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
