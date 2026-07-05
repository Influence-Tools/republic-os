---
type: Jurisdiction
title: "Clearfield County, PA"
classification: county
fips: "42033"
state: "PA"
demographics:
  population: 78635
  population_under_18: 14337
  population_18_64: 47166
  population_65_plus: 17132
  median_household_income: 62152
  poverty_rate: 14.61
  homeownership_rate: 78.52
  unemployment_rate: 5.91
  median_home_value: 137000
  gini_index: 0.4386
  vacancy_rate: 14.87
  race_white: 73217
  race_black: 1556
  race_asian: 451
  race_native: 51
  hispanic: 2378
  bachelors_plus: 15723
districts:
  - to: "us/states/pa/districts/15"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/pa/districts/senate/35"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/pa/districts/house/73"
    rel: in-district
    area_weight: 0.6642
  - to: "us/states/pa/districts/house/75"
    rel: in-district
    area_weight: 0.3356
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Clearfield County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 78635 |
| Under 18 | 14337 |
| 18–64 | 47166 |
| 65+ | 17132 |
| Median household income | 62152 |
| Poverty rate | 14.61 |
| Homeownership rate | 78.52 |
| Unemployment rate | 5.91 |
| Median home value | 137000 |
| Gini index | 0.4386 |
| Vacancy rate | 14.87 |
| White | 73217 |
| Black | 1556 |
| Asian | 451 |
| Native | 51 |
| Hispanic/Latino | 2378 |
| Bachelor's or higher | 15723 |

## Districts

- [PA-15](/us/states/pa/districts/15.md) — 100% (congressional)
- [PA Senate District 35](/us/states/pa/districts/senate/35.md) — 100% (state senate)
- [PA House District 73](/us/states/pa/districts/house/73.md) — 66% (state house)
- [PA House District 75](/us/states/pa/districts/house/75.md) — 34% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
