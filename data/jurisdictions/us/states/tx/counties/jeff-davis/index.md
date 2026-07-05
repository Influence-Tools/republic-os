---
type: Jurisdiction
title: "Jeff Davis County, TX"
classification: county
fips: "48243"
state: "TX"
demographics:
  population: 1865
  population_under_18: 336
  population_18_64: 897
  population_65_plus: 632
  median_household_income: 59286
  poverty_rate: 23.89
  homeownership_rate: 87.99
  unemployment_rate: 0.0
  median_home_value: 226200
  gini_index: 0.5562
  vacancy_rate: 36.9
  race_white: 1280
  race_black: 0
  race_asian: 0
  race_native: 0
  hispanic: 562
  bachelors_plus: 776
districts:
  - to: "us/states/tx/districts/23"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/29"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/74"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Jeff Davis County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1865 |
| Under 18 | 336 |
| 18–64 | 897 |
| 65+ | 632 |
| Median household income | 59286 |
| Poverty rate | 23.89 |
| Homeownership rate | 87.99 |
| Unemployment rate | 0.0 |
| Median home value | 226200 |
| Gini index | 0.5562 |
| Vacancy rate | 36.9 |
| White | 1280 |
| Black | 0 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 562 |
| Bachelor's or higher | 776 |

## Districts

- [TX-23](/us/states/tx/districts/23.md) — 100% (congressional)
- [TX Senate District 29](/us/states/tx/districts/senate/29.md) — 100% (state senate)
- [TX House District 74](/us/states/tx/districts/house/74.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
