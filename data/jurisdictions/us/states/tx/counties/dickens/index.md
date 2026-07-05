---
type: Jurisdiction
title: "Dickens County, TX"
classification: county
fips: "48125"
state: "TX"
demographics:
  population: 1747
  population_under_18: 371
  population_18_64: 909
  population_65_plus: 467
  median_household_income: 49335
  poverty_rate: 17.98
  homeownership_rate: 79.5
  unemployment_rate: 9.24
  median_home_value: 65300
  gini_index: 0.4558
  vacancy_rate: 36.84
  race_white: 1303
  race_black: 24
  race_asian: 27
  race_native: 22
  hispanic: 573
  bachelors_plus: 291
districts:
  - to: "us/states/tx/districts/13"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/83"
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

# Dickens County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1747 |
| Under 18 | 371 |
| 18–64 | 909 |
| 65+ | 467 |
| Median household income | 49335 |
| Poverty rate | 17.98 |
| Homeownership rate | 79.5 |
| Unemployment rate | 9.24 |
| Median home value | 65300 |
| Gini index | 0.4558 |
| Vacancy rate | 36.84 |
| White | 1303 |
| Black | 24 |
| Asian | 27 |
| Native | 22 |
| Hispanic/Latino | 573 |
| Bachelor's or higher | 291 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 83](/us/states/tx/districts/house/83.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
