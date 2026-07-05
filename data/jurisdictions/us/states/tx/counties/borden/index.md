---
type: Jurisdiction
title: "Borden County, TX"
classification: county
fips: "48033"
state: "TX"
demographics:
  population: 713
  population_under_18: 251
  population_18_64: 339
  population_65_plus: 123
  median_household_income: 65625
  poverty_rate: 7.43
  homeownership_rate: 66.26
  unemployment_rate: 0.33
  median_home_value: 108900
  gini_index: 0.5261
  vacancy_rate: 33.97
  race_white: 645
  race_black: 4
  race_asian: 0
  race_native: 0
  hispanic: 60
  bachelors_plus: 201
districts:
  - to: "us/states/tx/districts/19"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/83"
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

# Borden County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 713 |
| Under 18 | 251 |
| 18–64 | 339 |
| 65+ | 123 |
| Median household income | 65625 |
| Poverty rate | 7.43 |
| Homeownership rate | 66.26 |
| Unemployment rate | 0.33 |
| Median home value | 108900 |
| Gini index | 0.5261 |
| Vacancy rate | 33.97 |
| White | 645 |
| Black | 4 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 60 |
| Bachelor's or higher | 201 |

## Districts

- [TX-19](/us/states/tx/districts/19.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 83](/us/states/tx/districts/house/83.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
