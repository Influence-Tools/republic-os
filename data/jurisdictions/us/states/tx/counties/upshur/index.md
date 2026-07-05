---
type: Jurisdiction
title: "Upshur County, TX"
classification: county
fips: "48459"
state: "TX"
demographics:
  population: 42567
  population_under_18: 10138
  population_18_64: 24566
  population_65_plus: 7863
  median_household_income: 66208
  poverty_rate: 12.36
  homeownership_rate: 80.66
  unemployment_rate: 5.8
  median_home_value: 167800
  gini_index: 0.4536
  vacancy_rate: 11.05
  race_white: 33744
  race_black: 3052
  race_asian: 251
  race_native: 87
  hispanic: 4434
  bachelors_plus: 6821
districts:
  - to: "us/states/tx/districts/05"
    rel: in-district
    area_weight: 0.5033
  - to: "us/states/tx/districts/01"
    rel: in-district
    area_weight: 0.4967
  - to: "us/states/tx/districts/senate/1"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/5"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Upshur County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 42567 |
| Under 18 | 10138 |
| 18–64 | 24566 |
| 65+ | 7863 |
| Median household income | 66208 |
| Poverty rate | 12.36 |
| Homeownership rate | 80.66 |
| Unemployment rate | 5.8 |
| Median home value | 167800 |
| Gini index | 0.4536 |
| Vacancy rate | 11.05 |
| White | 33744 |
| Black | 3052 |
| Asian | 251 |
| Native | 87 |
| Hispanic/Latino | 4434 |
| Bachelor's or higher | 6821 |

## Districts

- [TX-05](/us/states/tx/districts/05.md) — 50% (congressional)
- [TX-01](/us/states/tx/districts/01.md) — 50% (congressional)
- [TX Senate District 1](/us/states/tx/districts/senate/1.md) — 100% (state senate)
- [TX House District 5](/us/states/tx/districts/house/5.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
