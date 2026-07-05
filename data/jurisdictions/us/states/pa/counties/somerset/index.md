---
type: Jurisdiction
title: "Somerset County, PA"
classification: county
fips: "42111"
state: "PA"
demographics:
  population: 72799
  population_under_18: 13227
  population_18_64: 42168
  population_65_plus: 17404
  median_household_income: 61446
  poverty_rate: 10.99
  homeownership_rate: 80.4
  unemployment_rate: 4.92
  median_home_value: 150600
  gini_index: 0.424
  vacancy_rate: 22.5
  race_white: 68331
  race_black: 1909
  race_asian: 415
  race_native: 13
  hispanic: 1127
  bachelors_plus: 13240
districts:
  - to: "us/states/pa/districts/14"
    rel: in-district
    area_weight: 0.9829
  - to: "us/states/pa/districts/13"
    rel: in-district
    area_weight: 0.0169
  - to: "us/states/pa/districts/senate/32"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/pa/districts/house/69"
    rel: in-district
    area_weight: 0.9352
  - to: "us/states/pa/districts/house/71"
    rel: in-district
    area_weight: 0.0645
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Somerset County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 72799 |
| Under 18 | 13227 |
| 18–64 | 42168 |
| 65+ | 17404 |
| Median household income | 61446 |
| Poverty rate | 10.99 |
| Homeownership rate | 80.4 |
| Unemployment rate | 4.92 |
| Median home value | 150600 |
| Gini index | 0.424 |
| Vacancy rate | 22.5 |
| White | 68331 |
| Black | 1909 |
| Asian | 415 |
| Native | 13 |
| Hispanic/Latino | 1127 |
| Bachelor's or higher | 13240 |

## Districts

- [PA-14](/us/states/pa/districts/14.md) — 98% (congressional)
- [PA-13](/us/states/pa/districts/13.md) — 2% (congressional)
- [PA Senate District 32](/us/states/pa/districts/senate/32.md) — 100% (state senate)
- [PA House District 69](/us/states/pa/districts/house/69.md) — 94% (state house)
- [PA House District 71](/us/states/pa/districts/house/71.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
