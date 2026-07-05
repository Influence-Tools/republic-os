---
type: Jurisdiction
title: "Cooke County, TX"
classification: county
fips: "48097"
state: "TX"
demographics:
  population: 43046
  population_under_18: 9987
  population_18_64: 24923
  population_65_plus: 8136
  median_household_income: 73932
  poverty_rate: 13.53
  homeownership_rate: 71.84
  unemployment_rate: 4.48
  median_home_value: 240400
  gini_index: 0.4499
  vacancy_rate: 7.89
  race_white: 33253
  race_black: 1378
  race_asian: 313
  race_native: 156
  hispanic: 8999
  bachelors_plus: 9237
districts:
  - to: "us/states/tx/districts/26"
    rel: in-district
    area_weight: 0.9982
  - to: "us/states/tx/districts/senate/30"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/tx/districts/house/68"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Cooke County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 43046 |
| Under 18 | 9987 |
| 18–64 | 24923 |
| 65+ | 8136 |
| Median household income | 73932 |
| Poverty rate | 13.53 |
| Homeownership rate | 71.84 |
| Unemployment rate | 4.48 |
| Median home value | 240400 |
| Gini index | 0.4499 |
| Vacancy rate | 7.89 |
| White | 33253 |
| Black | 1378 |
| Asian | 313 |
| Native | 156 |
| Hispanic/Latino | 8999 |
| Bachelor's or higher | 9237 |

## Districts

- [TX-26](/us/states/tx/districts/26.md) — 100% (congressional)
- [TX Senate District 30](/us/states/tx/districts/senate/30.md) — 100% (state senate)
- [TX House District 68](/us/states/tx/districts/house/68.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
