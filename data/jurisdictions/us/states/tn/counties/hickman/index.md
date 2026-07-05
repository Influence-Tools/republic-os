---
type: Jurisdiction
title: "Hickman County, TN"
classification: county
fips: "47081"
state: "TN"
demographics:
  population: 25436
  population_under_18: 5358
  population_18_64: 15551
  population_65_plus: 4527
  median_household_income: 68247
  poverty_rate: 10.64
  homeownership_rate: 79.23
  unemployment_rate: 2.42
  median_home_value: 224100
  gini_index: 0.4286
  vacancy_rate: 11.91
  race_white: 22754
  race_black: 806
  race_asian: 139
  race_native: 104
  hispanic: 858
  bachelors_plus: 3370
districts:
  - to: "us/states/tn/districts/07"
    rel: in-district
    area_weight: 0.9976
  - to: "us/states/tn/districts/senate/23"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tn/districts/house/69"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Hickman County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25436 |
| Under 18 | 5358 |
| 18–64 | 15551 |
| 65+ | 4527 |
| Median household income | 68247 |
| Poverty rate | 10.64 |
| Homeownership rate | 79.23 |
| Unemployment rate | 2.42 |
| Median home value | 224100 |
| Gini index | 0.4286 |
| Vacancy rate | 11.91 |
| White | 22754 |
| Black | 806 |
| Asian | 139 |
| Native | 104 |
| Hispanic/Latino | 858 |
| Bachelor's or higher | 3370 |

## Districts

- [TN-07](/us/states/tn/districts/07.md) — 100% (congressional)
- [TN Senate District 23](/us/states/tn/districts/senate/23.md) — 100% (state senate)
- [TN House District 69](/us/states/tn/districts/house/69.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
