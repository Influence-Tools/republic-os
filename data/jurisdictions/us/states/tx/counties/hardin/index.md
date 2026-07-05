---
type: Jurisdiction
title: "Hardin County, TX"
classification: county
fips: "48199"
state: "TX"
demographics:
  population: 57642
  population_under_18: 14263
  population_18_64: 33170
  population_65_plus: 10209
  median_household_income: 75808
  poverty_rate: 12.09
  homeownership_rate: 82.32
  unemployment_rate: 5.43
  median_home_value: 205700
  gini_index: 0.4199
  vacancy_rate: 11.47
  race_white: 48357
  race_black: 3304
  race_asian: 317
  race_native: 147
  hispanic: 3936
  bachelors_plus: 10308
districts:
  - to: "us/states/tx/districts/36"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/tx/districts/senate/3"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/house/18"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Hardin County, TX

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 57642 |
| Under 18 | 14263 |
| 18–64 | 33170 |
| 65+ | 10209 |
| Median household income | 75808 |
| Poverty rate | 12.09 |
| Homeownership rate | 82.32 |
| Unemployment rate | 5.43 |
| Median home value | 205700 |
| Gini index | 0.4199 |
| Vacancy rate | 11.47 |
| White | 48357 |
| Black | 3304 |
| Asian | 317 |
| Native | 147 |
| Hispanic/Latino | 3936 |
| Bachelor's or higher | 10308 |

## Districts

- [TX-36](/us/states/tx/districts/36.md) — 100% (congressional)
- [TX Senate District 3](/us/states/tx/districts/senate/3.md) — 100% (state senate)
- [TX House District 18](/us/states/tx/districts/house/18.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
