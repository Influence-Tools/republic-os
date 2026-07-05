---
type: Jurisdiction
title: "Jones County, TX"
classification: county
fips: "48253"
state: "TX"
demographics:
  population: 20304
  population_under_18: 3438
  population_18_64: 13611
  population_65_plus: 3255
  median_household_income: 59464
  poverty_rate: 14.05
  homeownership_rate: 80.39
  unemployment_rate: 5.53
  median_home_value: 96500
  gini_index: 0.4508
  vacancy_rate: 16.24
  race_white: 12860
  race_black: 2059
  race_asian: 116
  race_native: 164
  hispanic: 5816
  bachelors_plus: 2229
districts:
  - to: "us/states/tx/districts/19"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/71"
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

# Jones County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20304 |
| Under 18 | 3438 |
| 18–64 | 13611 |
| 65+ | 3255 |
| Median household income | 59464 |
| Poverty rate | 14.05 |
| Homeownership rate | 80.39 |
| Unemployment rate | 5.53 |
| Median home value | 96500 |
| Gini index | 0.4508 |
| Vacancy rate | 16.24 |
| White | 12860 |
| Black | 2059 |
| Asian | 116 |
| Native | 164 |
| Hispanic/Latino | 5816 |
| Bachelor's or higher | 2229 |

## Districts

- [TX-19](/us/states/tx/districts/19.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 71](/us/states/tx/districts/house/71.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
