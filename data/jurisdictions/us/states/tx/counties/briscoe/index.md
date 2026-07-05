---
type: Jurisdiction
title: "Briscoe County, TX"
classification: county
fips: "48045"
state: "TX"
demographics:
  population: 1301
  population_under_18: 270
  population_18_64: 711
  population_65_plus: 320
  median_household_income: 45417
  poverty_rate: 16.8
  homeownership_rate: 82.82
  unemployment_rate: 1.02
  median_home_value: 90300
  gini_index: 0.5574
  vacancy_rate: 34.86
  race_white: 1089
  race_black: 79
  race_asian: 0
  race_native: 1
  hispanic: 339
  bachelors_plus: 263
districts:
  - to: "us/states/tx/districts/13"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/88"
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

# Briscoe County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1301 |
| Under 18 | 270 |
| 18–64 | 711 |
| 65+ | 320 |
| Median household income | 45417 |
| Poverty rate | 16.8 |
| Homeownership rate | 82.82 |
| Unemployment rate | 1.02 |
| Median home value | 90300 |
| Gini index | 0.5574 |
| Vacancy rate | 34.86 |
| White | 1089 |
| Black | 79 |
| Asian | 0 |
| Native | 1 |
| Hispanic/Latino | 339 |
| Bachelor's or higher | 263 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 88](/us/states/tx/districts/house/88.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
