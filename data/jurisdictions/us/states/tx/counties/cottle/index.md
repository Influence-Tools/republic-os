---
type: Jurisdiction
title: "Cottle County, TX"
classification: county
fips: "48101"
state: "TX"
demographics:
  population: 1368
  population_under_18: 250
  population_18_64: 801
  population_65_plus: 317
  median_household_income: 59063
  poverty_rate: 17.09
  homeownership_rate: 83.19
  unemployment_rate: 12.6
  median_home_value: 59300
  gini_index: 0.5533
  vacancy_rate: 37.96
  race_white: 694
  race_black: 32
  race_asian: 0
  race_native: 0
  hispanic: 574
  bachelors_plus: 248
districts:
  - to: "us/states/tx/districts/13"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/69"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Cottle County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1368 |
| Under 18 | 250 |
| 18–64 | 801 |
| 65+ | 317 |
| Median household income | 59063 |
| Poverty rate | 17.09 |
| Homeownership rate | 83.19 |
| Unemployment rate | 12.6 |
| Median home value | 59300 |
| Gini index | 0.5533 |
| Vacancy rate | 37.96 |
| White | 694 |
| Black | 32 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 574 |
| Bachelor's or higher | 248 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 69](/us/states/tx/districts/house/69.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
