---
type: Jurisdiction
title: "Rains County, TX"
classification: county
fips: "48379"
state: "TX"
demographics:
  population: 12775
  population_under_18: 2456
  population_18_64: 7169
  population_65_plus: 3150
  median_household_income: 65413
  poverty_rate: 9.99
  homeownership_rate: 82.58
  unemployment_rate: 3.26
  median_home_value: 241100
  gini_index: 0.4342
  vacancy_rate: 18.04
  race_white: 10773
  race_black: 319
  race_asian: 128
  race_native: 61
  hispanic: 1311
  bachelors_plus: 2415
districts:
  - to: "us/states/tx/districts/04"
    rel: in-district
    area_weight: 0.9969
  - to: "us/states/tx/districts/senate/8"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/tx/districts/house/5"
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

# Rains County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12775 |
| Under 18 | 2456 |
| 18–64 | 7169 |
| 65+ | 3150 |
| Median household income | 65413 |
| Poverty rate | 9.99 |
| Homeownership rate | 82.58 |
| Unemployment rate | 3.26 |
| Median home value | 241100 |
| Gini index | 0.4342 |
| Vacancy rate | 18.04 |
| White | 10773 |
| Black | 319 |
| Asian | 128 |
| Native | 61 |
| Hispanic/Latino | 1311 |
| Bachelor's or higher | 2415 |

## Districts

- [TX-04](/us/states/tx/districts/04.md) — 100% (congressional)
- [TX Senate District 8](/us/states/tx/districts/senate/8.md) — 100% (state senate)
- [TX House District 5](/us/states/tx/districts/house/5.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
