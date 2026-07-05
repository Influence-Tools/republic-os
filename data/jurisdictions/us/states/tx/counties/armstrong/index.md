---
type: Jurisdiction
title: "Armstrong County, TX"
classification: county
fips: "48011"
state: "TX"
demographics:
  population: 1822
  population_under_18: 351
  population_18_64: 1012
  population_65_plus: 459
  median_household_income: 72750
  poverty_rate: 5.19
  homeownership_rate: 80.18
  unemployment_rate: 1.24
  median_home_value: 171500
  gini_index: 0.3403
  vacancy_rate: 13.43
  race_white: 1638
  race_black: 11
  race_asian: 29
  race_native: 19
  hispanic: 218
  bachelors_plus: 486
districts:
  - to: "us/states/tx/districts/13"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/86"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Armstrong County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1822 |
| Under 18 | 351 |
| 18–64 | 1012 |
| 65+ | 459 |
| Median household income | 72750 |
| Poverty rate | 5.19 |
| Homeownership rate | 80.18 |
| Unemployment rate | 1.24 |
| Median home value | 171500 |
| Gini index | 0.3403 |
| Vacancy rate | 13.43 |
| White | 1638 |
| Black | 11 |
| Asian | 29 |
| Native | 19 |
| Hispanic/Latino | 218 |
| Bachelor's or higher | 486 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 86](/us/states/tx/districts/house/86.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
