---
type: Jurisdiction
title: "Roseau County, MN"
classification: county
fips: "27135"
state: "MN"
demographics:
  population: 15302
  population_under_18: 3643
  population_18_64: 8729
  population_65_plus: 2930
  median_household_income: 74474
  poverty_rate: 12.16
  homeownership_rate: 79.21
  unemployment_rate: 3.74
  median_home_value: 183700
  gini_index: 0.4294
  vacancy_rate: 12.85
  race_white: 13558
  race_black: 119
  race_asian: 396
  race_native: 149
  hispanic: 305
  bachelors_plus: 2740
districts:
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/mn/districts/senate/1"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mn/districts/house/1a"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Roseau County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15302 |
| Under 18 | 3643 |
| 18–64 | 8729 |
| 65+ | 2930 |
| Median household income | 74474 |
| Poverty rate | 12.16 |
| Homeownership rate | 79.21 |
| Unemployment rate | 3.74 |
| Median home value | 183700 |
| Gini index | 0.4294 |
| Vacancy rate | 12.85 |
| White | 13558 |
| Black | 119 |
| Asian | 396 |
| Native | 149 |
| Hispanic/Latino | 305 |
| Bachelor's or higher | 2740 |

## Districts

- [MN-07](/us/states/mn/districts/07.md) — 100% (congressional)
- [MN Senate District 1](/us/states/mn/districts/senate/1.md) — 100% (state senate)
- [MN House District 1A](/us/states/mn/districts/house/1a.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
