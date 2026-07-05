---
type: Jurisdiction
title: "Cross County, AR"
classification: county
fips: "05037"
state: "AR"
demographics:
  population: 16543
  population_under_18: 3925
  population_18_64: 9495
  population_65_plus: 3123
  median_household_income: 50863
  poverty_rate: 19.72
  homeownership_rate: 67.53
  unemployment_rate: 10.71
  median_home_value: 117500
  gini_index: 0.4804
  vacancy_rate: 14.54
  race_white: 11902
  race_black: 2617
  race_asian: 479
  race_native: 43
  hispanic: 378
  bachelors_plus: 2720
districts:
  - to: "us/states/ar/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ar/districts/senate/10"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ar/districts/house/37"
    rel: in-district
    area_weight: 0.8584
  - to: "us/states/ar/districts/house/35"
    rel: in-district
    area_weight: 0.1414
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Cross County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16543 |
| Under 18 | 3925 |
| 18–64 | 9495 |
| 65+ | 3123 |
| Median household income | 50863 |
| Poverty rate | 19.72 |
| Homeownership rate | 67.53 |
| Unemployment rate | 10.71 |
| Median home value | 117500 |
| Gini index | 0.4804 |
| Vacancy rate | 14.54 |
| White | 11902 |
| Black | 2617 |
| Asian | 479 |
| Native | 43 |
| Hispanic/Latino | 378 |
| Bachelor's or higher | 2720 |

## Districts

- [AR-01](/us/states/ar/districts/01.md) — 100% (congressional)
- [AR Senate District 10](/us/states/ar/districts/senate/10.md) — 100% (state senate)
- [AR House District 37](/us/states/ar/districts/house/37.md) — 86% (state house)
- [AR House District 35](/us/states/ar/districts/house/35.md) — 14% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
