---
type: Jurisdiction
title: "Wilkin County, MN"
classification: county
fips: "27167"
state: "MN"
demographics:
  population: 6371
  population_under_18: 1448
  population_18_64: 3652
  population_65_plus: 1271
  median_household_income: 71410
  poverty_rate: 14.08
  homeownership_rate: 79.66
  unemployment_rate: 4.8
  median_home_value: 182200
  gini_index: 0.409
  vacancy_rate: 11.0
  race_white: 5869
  race_black: 28
  race_asian: 2
  race_native: 51
  hispanic: 254
  bachelors_plus: 1212
districts:
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 0.9975
  - to: "us/states/mn/districts/senate/9"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/mn/districts/house/9a"
    rel: in-district
    area_weight: 0.9992
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Wilkin County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6371 |
| Under 18 | 1448 |
| 18–64 | 3652 |
| 65+ | 1271 |
| Median household income | 71410 |
| Poverty rate | 14.08 |
| Homeownership rate | 79.66 |
| Unemployment rate | 4.8 |
| Median home value | 182200 |
| Gini index | 0.409 |
| Vacancy rate | 11.0 |
| White | 5869 |
| Black | 28 |
| Asian | 2 |
| Native | 51 |
| Hispanic/Latino | 254 |
| Bachelor's or higher | 1212 |

## Districts

- [MN-07](/us/states/mn/districts/07.md) — 100% (congressional)
- [MN Senate District 9](/us/states/mn/districts/senate/9.md) — 100% (state senate)
- [MN House District 9A](/us/states/mn/districts/house/9a.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
