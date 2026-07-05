---
type: Jurisdiction
title: "Franklin Parish, LA"
classification: county
fips: "22041"
state: "LA"
demographics:
  population: 19408
  population_under_18: 4813
  population_18_64: 10770
  population_65_plus: 3825
  median_household_income: 47020
  poverty_rate: 24.08
  homeownership_rate: 73.17
  unemployment_rate: 8.15
  median_home_value: 113000
  gini_index: 0.4839
  vacancy_rate: 15.7
  race_white: 12858
  race_black: 5432
  race_asian: 32
  race_native: 9
  hispanic: 325
  bachelors_plus: 3016
districts:
  - to: "us/states/la/districts/05"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/la/districts/senate/32"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/la/districts/house/20"
    rel: in-district
    area_weight: 0.8718
  - to: "us/states/la/districts/house/21"
    rel: in-district
    area_weight: 0.1278
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Franklin Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19408 |
| Under 18 | 4813 |
| 18–64 | 10770 |
| 65+ | 3825 |
| Median household income | 47020 |
| Poverty rate | 24.08 |
| Homeownership rate | 73.17 |
| Unemployment rate | 8.15 |
| Median home value | 113000 |
| Gini index | 0.4839 |
| Vacancy rate | 15.7 |
| White | 12858 |
| Black | 5432 |
| Asian | 32 |
| Native | 9 |
| Hispanic/Latino | 325 |
| Bachelor's or higher | 3016 |

## Districts

- [LA-05](/us/states/la/districts/05.md) — 100% (congressional)
- [LA Senate District 32](/us/states/la/districts/senate/32.md) — 100% (state senate)
- [LA House District 20](/us/states/la/districts/house/20.md) — 87% (state house)
- [LA House District 21](/us/states/la/districts/house/21.md) — 13% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
