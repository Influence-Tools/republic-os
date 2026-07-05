---
type: Jurisdiction
title: "Stonewall County, TX"
classification: county
fips: "48433"
state: "TX"
demographics:
  population: 1227
  population_under_18: 308
  population_18_64: 576
  population_65_plus: 343
  median_household_income: 56875
  poverty_rate: 14.9
  homeownership_rate: 84.6
  unemployment_rate: 3.57
  median_home_value: 48600
  gini_index: 0.579
  vacancy_rate: 35.15
  race_white: 1088
  race_black: 5
  race_asian: 0
  race_native: 0
  hispanic: 245
  bachelors_plus: 203
districts:
  - to: "us/states/tx/districts/19"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/69"
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

# Stonewall County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1227 |
| Under 18 | 308 |
| 18–64 | 576 |
| 65+ | 343 |
| Median household income | 56875 |
| Poverty rate | 14.9 |
| Homeownership rate | 84.6 |
| Unemployment rate | 3.57 |
| Median home value | 48600 |
| Gini index | 0.579 |
| Vacancy rate | 35.15 |
| White | 1088 |
| Black | 5 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 245 |
| Bachelor's or higher | 203 |

## Districts

- [TX-19](/us/states/tx/districts/19.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 69](/us/states/tx/districts/house/69.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
