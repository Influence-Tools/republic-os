---
type: Jurisdiction
title: "Blanco County, TX"
classification: county
fips: "48031"
state: "TX"
demographics:
  population: 12446
  population_under_18: 2182
  population_18_64: 6979
  population_65_plus: 3285
  median_household_income: 92425
  poverty_rate: 8.44
  homeownership_rate: 76.23
  unemployment_rate: 5.92
  median_home_value: 483500
  gini_index: 0.4222
  vacancy_rate: 15.71
  race_white: 10003
  race_black: 134
  race_asian: 12
  race_native: 25
  hispanic: 2316
  bachelors_plus: 4371
districts:
  - to: "us/states/tx/districts/21"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/senate/25"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/house/19"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Blanco County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12446 |
| Under 18 | 2182 |
| 18–64 | 6979 |
| 65+ | 3285 |
| Median household income | 92425 |
| Poverty rate | 8.44 |
| Homeownership rate | 76.23 |
| Unemployment rate | 5.92 |
| Median home value | 483500 |
| Gini index | 0.4222 |
| Vacancy rate | 15.71 |
| White | 10003 |
| Black | 134 |
| Asian | 12 |
| Native | 25 |
| Hispanic/Latino | 2316 |
| Bachelor's or higher | 4371 |

## Districts

- [TX-21](/us/states/tx/districts/21.md) — 100% (congressional)
- [TX Senate District 25](/us/states/tx/districts/senate/25.md) — 100% (state senate)
- [TX House District 19](/us/states/tx/districts/house/19.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
