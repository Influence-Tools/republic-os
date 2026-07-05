---
type: Jurisdiction
title: "Nodaway County, MO"
classification: county
fips: "29147"
state: "MO"
demographics:
  population: 20774
  population_under_18: 3530
  population_18_64: 13543
  population_65_plus: 3701
  median_household_income: 59315
  poverty_rate: 17.09
  homeownership_rate: 62.29
  unemployment_rate: 2.4
  median_home_value: 177500
  gini_index: 0.4305
  vacancy_rate: 11.28
  race_white: 19125
  race_black: 439
  race_asian: 341
  race_native: 58
  hispanic: 461
  bachelors_plus: 4937
districts:
  - to: "us/states/mo/districts/06"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/senate/12"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/1"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Nodaway County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20774 |
| Under 18 | 3530 |
| 18–64 | 13543 |
| 65+ | 3701 |
| Median household income | 59315 |
| Poverty rate | 17.09 |
| Homeownership rate | 62.29 |
| Unemployment rate | 2.4 |
| Median home value | 177500 |
| Gini index | 0.4305 |
| Vacancy rate | 11.28 |
| White | 19125 |
| Black | 439 |
| Asian | 341 |
| Native | 58 |
| Hispanic/Latino | 461 |
| Bachelor's or higher | 4937 |

## Districts

- [MO-06](/us/states/mo/districts/06.md) — 100% (congressional)
- [MO Senate District 12](/us/states/mo/districts/senate/12.md) — 100% (state senate)
- [MO House District 1](/us/states/mo/districts/house/1.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
