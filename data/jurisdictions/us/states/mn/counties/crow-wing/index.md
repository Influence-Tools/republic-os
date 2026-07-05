---
type: Jurisdiction
title: "Crow Wing County, MN"
classification: county
fips: "27035"
state: "MN"
demographics:
  population: 67686
  population_under_18: 13843
  population_18_64: 37280
  population_65_plus: 16563
  median_household_income: 72589
  poverty_rate: 9.87
  homeownership_rate: 77.03
  unemployment_rate: 5.46
  median_home_value: 306800
  gini_index: 0.4366
  vacancy_rate: 31.12
  race_white: 63439
  race_black: 320
  race_asian: 272
  race_native: 456
  hispanic: 1089
  bachelors_plus: 19232
districts:
  - to: "us/states/mn/districts/08"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/mn/districts/senate/6"
    rel: in-district
    area_weight: 0.7915
  - to: "us/states/mn/districts/senate/10"
    rel: in-district
    area_weight: 0.2084
  - to: "us/states/mn/districts/house/6a"
    rel: in-district
    area_weight: 0.5699
  - to: "us/states/mn/districts/house/6b"
    rel: in-district
    area_weight: 0.2215
  - to: "us/states/mn/districts/house/10a"
    rel: in-district
    area_weight: 0.2084
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Crow Wing County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 67686 |
| Under 18 | 13843 |
| 18–64 | 37280 |
| 65+ | 16563 |
| Median household income | 72589 |
| Poverty rate | 9.87 |
| Homeownership rate | 77.03 |
| Unemployment rate | 5.46 |
| Median home value | 306800 |
| Gini index | 0.4366 |
| Vacancy rate | 31.12 |
| White | 63439 |
| Black | 320 |
| Asian | 272 |
| Native | 456 |
| Hispanic/Latino | 1089 |
| Bachelor's or higher | 19232 |

## Districts

- [MN-08](/us/states/mn/districts/08.md) — 100% (congressional)
- [MN Senate District 6](/us/states/mn/districts/senate/6.md) — 79% (state senate)
- [MN Senate District 10](/us/states/mn/districts/senate/10.md) — 21% (state senate)
- [MN House District 6A](/us/states/mn/districts/house/6a.md) — 57% (state house)
- [MN House District 6B](/us/states/mn/districts/house/6b.md) — 22% (state house)
- [MN House District 10A](/us/states/mn/districts/house/10a.md) — 21% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
