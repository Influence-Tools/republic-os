---
type: Jurisdiction
title: "Franklin County, TX"
classification: county
fips: "48159"
state: "TX"
demographics:
  population: 10632
  population_under_18: 2374
  population_18_64: 5883
  population_65_plus: 2375
  median_household_income: 72360
  poverty_rate: 11.67
  homeownership_rate: 82.04
  unemployment_rate: 4.39
  median_home_value: 226300
  gini_index: 0.4947
  vacancy_rate: 23.9
  race_white: 8261
  race_black: 578
  race_asian: 33
  race_native: 18
  hispanic: 1567
  bachelors_plus: 2802
districts:
  - to: "us/states/tx/districts/01"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/tx/districts/senate/1"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/62"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Franklin County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10632 |
| Under 18 | 2374 |
| 18–64 | 5883 |
| 65+ | 2375 |
| Median household income | 72360 |
| Poverty rate | 11.67 |
| Homeownership rate | 82.04 |
| Unemployment rate | 4.39 |
| Median home value | 226300 |
| Gini index | 0.4947 |
| Vacancy rate | 23.9 |
| White | 8261 |
| Black | 578 |
| Asian | 33 |
| Native | 18 |
| Hispanic/Latino | 1567 |
| Bachelor's or higher | 2802 |

## Districts

- [TX-01](/us/states/tx/districts/01.md) — 100% (congressional)
- [TX Senate District 1](/us/states/tx/districts/senate/1.md) — 100% (state senate)
- [TX House District 62](/us/states/tx/districts/house/62.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
