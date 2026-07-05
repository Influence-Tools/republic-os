---
type: Jurisdiction
title: "Phelps County, MO"
classification: county
fips: "29161"
state: "MO"
demographics:
  population: 45194
  population_under_18: 9537
  population_18_64: 27944
  population_65_plus: 7713
  median_household_income: 58396
  poverty_rate: 16.78
  homeownership_rate: 61.68
  unemployment_rate: 3.89
  median_home_value: 206500
  gini_index: 0.4564
  vacancy_rate: 14.61
  race_white: 39059
  race_black: 1100
  race_asian: 1744
  race_native: 197
  hispanic: 1390
  bachelors_plus: 13586
districts:
  - to: "us/states/mo/districts/08"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/mo/districts/senate/16"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/house/122"
    rel: in-district
    area_weight: 0.5062
  - to: "us/states/mo/districts/house/143"
    rel: in-district
    area_weight: 0.4935
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Phelps County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 45194 |
| Under 18 | 9537 |
| 18–64 | 27944 |
| 65+ | 7713 |
| Median household income | 58396 |
| Poverty rate | 16.78 |
| Homeownership rate | 61.68 |
| Unemployment rate | 3.89 |
| Median home value | 206500 |
| Gini index | 0.4564 |
| Vacancy rate | 14.61 |
| White | 39059 |
| Black | 1100 |
| Asian | 1744 |
| Native | 197 |
| Hispanic/Latino | 1390 |
| Bachelor's or higher | 13586 |

## Districts

- [MO-08](/us/states/mo/districts/08.md) — 100% (congressional)
- [MO Senate District 16](/us/states/mo/districts/senate/16.md) — 100% (state senate)
- [MO House District 122](/us/states/mo/districts/house/122.md) — 51% (state house)
- [MO House District 143](/us/states/mo/districts/house/143.md) — 49% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
