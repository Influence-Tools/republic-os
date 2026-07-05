---
type: Jurisdiction
title: "Jack County, TX"
classification: county
fips: "48237"
state: "TX"
demographics:
  population: 8882
  population_under_18: 2002
  population_18_64: 5383
  population_65_plus: 1497
  median_household_income: 68079
  poverty_rate: 12.95
  homeownership_rate: 72.2
  unemployment_rate: 9.58
  median_home_value: 251200
  gini_index: 0.4744
  vacancy_rate: 21.65
  race_white: 7598
  race_black: 259
  race_asian: 42
  race_native: 4
  hispanic: 1660
  bachelors_plus: 1133
districts:
  - to: "us/states/tx/districts/25"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/senate/30"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/68"
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

# Jack County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8882 |
| Under 18 | 2002 |
| 18–64 | 5383 |
| 65+ | 1497 |
| Median household income | 68079 |
| Poverty rate | 12.95 |
| Homeownership rate | 72.2 |
| Unemployment rate | 9.58 |
| Median home value | 251200 |
| Gini index | 0.4744 |
| Vacancy rate | 21.65 |
| White | 7598 |
| Black | 259 |
| Asian | 42 |
| Native | 4 |
| Hispanic/Latino | 1660 |
| Bachelor's or higher | 1133 |

## Districts

- [TX-25](/us/states/tx/districts/25.md) — 100% (congressional)
- [TX Senate District 30](/us/states/tx/districts/senate/30.md) — 100% (state senate)
- [TX House District 68](/us/states/tx/districts/house/68.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
