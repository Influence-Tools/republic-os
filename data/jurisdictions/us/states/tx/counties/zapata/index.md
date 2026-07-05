---
type: Jurisdiction
title: "Zapata County, TX"
classification: county
fips: "48505"
state: "TX"
demographics:
  population: 13841
  population_under_18: 4379
  population_18_64: 7512
  population_65_plus: 1950
  median_household_income: 39239
  poverty_rate: 38.39
  homeownership_rate: 71.96
  unemployment_rate: 7.35
  median_home_value: 97100
  gini_index: 0.4977
  vacancy_rate: 27.02
  race_white: 2924
  race_black: 20
  race_asian: 84
  race_native: 0
  hispanic: 12999
  bachelors_plus: 1638
districts:
  - to: "us/states/tx/districts/28"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/tx/districts/senate/21"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/31"
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

# Zapata County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13841 |
| Under 18 | 4379 |
| 18–64 | 7512 |
| 65+ | 1950 |
| Median household income | 39239 |
| Poverty rate | 38.39 |
| Homeownership rate | 71.96 |
| Unemployment rate | 7.35 |
| Median home value | 97100 |
| Gini index | 0.4977 |
| Vacancy rate | 27.02 |
| White | 2924 |
| Black | 20 |
| Asian | 84 |
| Native | 0 |
| Hispanic/Latino | 12999 |
| Bachelor's or higher | 1638 |

## Districts

- [TX-28](/us/states/tx/districts/28.md) — 100% (congressional)
- [TX Senate District 21](/us/states/tx/districts/senate/21.md) — 100% (state senate)
- [TX House District 31](/us/states/tx/districts/house/31.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
