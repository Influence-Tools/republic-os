---
type: Jurisdiction
title: "Wood County, TX"
classification: county
fips: "48499"
state: "TX"
demographics:
  population: 46961
  population_under_18: 8752
  population_18_64: 25255
  population_65_plus: 12954
  median_household_income: 60300
  poverty_rate: 12.5
  homeownership_rate: 80.15
  unemployment_rate: 6.26
  median_home_value: 216500
  gini_index: 0.4764
  vacancy_rate: 16.6
  race_white: 38481
  race_black: 1792
  race_asian: 256
  race_native: 15
  hispanic: 5433
  bachelors_plus: 10199
districts:
  - to: "us/states/tx/districts/05"
    rel: in-district
    area_weight: 0.9962
  - to: "us/states/tx/districts/senate/1"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/5"
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

# Wood County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 46961 |
| Under 18 | 8752 |
| 18–64 | 25255 |
| 65+ | 12954 |
| Median household income | 60300 |
| Poverty rate | 12.5 |
| Homeownership rate | 80.15 |
| Unemployment rate | 6.26 |
| Median home value | 216500 |
| Gini index | 0.4764 |
| Vacancy rate | 16.6 |
| White | 38481 |
| Black | 1792 |
| Asian | 256 |
| Native | 15 |
| Hispanic/Latino | 5433 |
| Bachelor's or higher | 10199 |

## Districts

- [TX-05](/us/states/tx/districts/05.md) — 100% (congressional)
- [TX Senate District 1](/us/states/tx/districts/senate/1.md) — 100% (state senate)
- [TX House District 5](/us/states/tx/districts/house/5.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
