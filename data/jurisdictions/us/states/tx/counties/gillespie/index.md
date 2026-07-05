---
type: Jurisdiction
title: "Gillespie County, TX"
classification: county
fips: "48171"
state: "TX"
demographics:
  population: 27524
  population_under_18: 5350
  population_18_64: 13873
  population_65_plus: 8301
  median_household_income: 76162
  poverty_rate: 9.23
  homeownership_rate: 74.91
  unemployment_rate: 2.72
  median_home_value: 460700
  gini_index: 0.4967
  vacancy_rate: 19.9
  race_white: 22545
  race_black: 86
  race_asian: 116
  race_native: 124
  hispanic: 6307
  bachelors_plus: 10571
districts:
  - to: "us/states/tx/districts/21"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/senate/24"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/house/19"
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

# Gillespie County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 27524 |
| Under 18 | 5350 |
| 18–64 | 13873 |
| 65+ | 8301 |
| Median household income | 76162 |
| Poverty rate | 9.23 |
| Homeownership rate | 74.91 |
| Unemployment rate | 2.72 |
| Median home value | 460700 |
| Gini index | 0.4967 |
| Vacancy rate | 19.9 |
| White | 22545 |
| Black | 86 |
| Asian | 116 |
| Native | 124 |
| Hispanic/Latino | 6307 |
| Bachelor's or higher | 10571 |

## Districts

- [TX-21](/us/states/tx/districts/21.md) — 100% (congressional)
- [TX Senate District 24](/us/states/tx/districts/senate/24.md) — 100% (state senate)
- [TX House District 19](/us/states/tx/districts/house/19.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
