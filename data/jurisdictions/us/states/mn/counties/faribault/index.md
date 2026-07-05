---
type: Jurisdiction
title: "Faribault County, MN"
classification: county
fips: "27043"
state: "MN"
demographics:
  population: 13914
  population_under_18: 3075
  population_18_64: 7536
  population_65_plus: 3303
  median_household_income: 66815
  poverty_rate: 10.37
  homeownership_rate: 79.19
  unemployment_rate: 3.36
  median_home_value: 135300
  gini_index: 0.4319
  vacancy_rate: 11.86
  race_white: 12369
  race_black: 90
  race_asian: 90
  race_native: 27
  hispanic: 1128
  bachelors_plus: 2699
districts:
  - to: "us/states/mn/districts/01"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mn/districts/senate/23"
    rel: in-district
    area_weight: 0.6494
  - to: "us/states/mn/districts/senate/22"
    rel: in-district
    area_weight: 0.3506
  - to: "us/states/mn/districts/house/23a"
    rel: in-district
    area_weight: 0.6494
  - to: "us/states/mn/districts/house/22a"
    rel: in-district
    area_weight: 0.3506
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Faribault County, MN

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13914 |
| Under 18 | 3075 |
| 18–64 | 7536 |
| 65+ | 3303 |
| Median household income | 66815 |
| Poverty rate | 10.37 |
| Homeownership rate | 79.19 |
| Unemployment rate | 3.36 |
| Median home value | 135300 |
| Gini index | 0.4319 |
| Vacancy rate | 11.86 |
| White | 12369 |
| Black | 90 |
| Asian | 90 |
| Native | 27 |
| Hispanic/Latino | 1128 |
| Bachelor's or higher | 2699 |

## Districts

- [MN-01](/us/states/mn/districts/01.md) — 100% (congressional)
- [MN Senate District 23](/us/states/mn/districts/senate/23.md) — 65% (state senate)
- [MN Senate District 22](/us/states/mn/districts/senate/22.md) — 35% (state senate)
- [MN House District 23A](/us/states/mn/districts/house/23a.md) — 65% (state house)
- [MN House District 22A](/us/states/mn/districts/house/22a.md) — 35% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
