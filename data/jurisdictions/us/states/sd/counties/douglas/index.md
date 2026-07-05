---
type: Jurisdiction
title: "Douglas County, SD"
classification: county
fips: "46043"
state: "SD"
demographics:
  population: 2828
  population_under_18: 722
  population_18_64: 1413
  population_65_plus: 693
  median_household_income: 86442
  poverty_rate: 11.05
  homeownership_rate: 76.71
  unemployment_rate: 0.47
  median_home_value: 166900
  gini_index: 0.4554
  vacancy_rate: 14.95
  race_white: 2608
  race_black: 18
  race_asian: 0
  race_native: 64
  hispanic: 84
  bachelors_plus: 585
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/21"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/sd/districts/house/21"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Douglas County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2828 |
| Under 18 | 722 |
| 18–64 | 1413 |
| 65+ | 693 |
| Median household income | 86442 |
| Poverty rate | 11.05 |
| Homeownership rate | 76.71 |
| Unemployment rate | 0.47 |
| Median home value | 166900 |
| Gini index | 0.4554 |
| Vacancy rate | 14.95 |
| White | 2608 |
| Black | 18 |
| Asian | 0 |
| Native | 64 |
| Hispanic/Latino | 84 |
| Bachelor's or higher | 585 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 21](/us/states/sd/districts/senate/21.md) — 100% (state senate)
- [SD House District 21](/us/states/sd/districts/house/21.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
