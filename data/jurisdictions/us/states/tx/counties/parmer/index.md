---
type: Jurisdiction
title: "Parmer County, TX"
classification: county
fips: "48369"
state: "TX"
demographics:
  population: 9731
  population_under_18: 2691
  population_18_64: 5518
  population_65_plus: 1522
  median_household_income: 69735
  poverty_rate: 10.17
  homeownership_rate: 72.08
  unemployment_rate: 2.65
  median_home_value: 146700
  gini_index: 0.3882
  vacancy_rate: 13.72
  race_white: 6231
  race_black: 28
  race_asian: 0
  race_native: 56
  hispanic: 6487
  bachelors_plus: 1268
districts:
  - to: "us/states/tx/districts/19"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 0.9998
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

# Parmer County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9731 |
| Under 18 | 2691 |
| 18–64 | 5518 |
| 65+ | 1522 |
| Median household income | 69735 |
| Poverty rate | 10.17 |
| Homeownership rate | 72.08 |
| Unemployment rate | 2.65 |
| Median home value | 146700 |
| Gini index | 0.3882 |
| Vacancy rate | 13.72 |
| White | 6231 |
| Black | 28 |
| Asian | 0 |
| Native | 56 |
| Hispanic/Latino | 6487 |
| Bachelor's or higher | 1268 |

## Districts

- [TX-19](/us/states/tx/districts/19.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 86](/us/states/tx/districts/house/86.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
