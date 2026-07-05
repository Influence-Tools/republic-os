---
type: Jurisdiction
title: "Itasca County, MN"
classification: county
fips: "27061"
state: "MN"
demographics:
  population: 45275
  population_under_18: 9125
  population_18_64: 24484
  population_65_plus: 11666
  median_household_income: 68603
  poverty_rate: 12.24
  homeownership_rate: 83.04
  unemployment_rate: 5.93
  median_home_value: 225200
  gini_index: 0.439
  vacancy_rate: 27.8
  race_white: 40183
  race_black: 360
  race_asian: 188
  race_native: 1162
  hispanic: 691
  bachelors_plus: 11694
districts:
  - to: "us/states/mn/districts/08"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mn/districts/senate/3"
    rel: in-district
    area_weight: 0.4163
  - to: "us/states/mn/districts/senate/7"
    rel: in-district
    area_weight: 0.2955
  - to: "us/states/mn/districts/senate/2"
    rel: in-district
    area_weight: 0.2017
  - to: "us/states/mn/districts/senate/6"
    rel: in-district
    area_weight: 0.0864
  - to: "us/states/mn/districts/house/3a"
    rel: in-district
    area_weight: 0.4163
  - to: "us/states/mn/districts/house/7a"
    rel: in-district
    area_weight: 0.2955
  - to: "us/states/mn/districts/house/2b"
    rel: in-district
    area_weight: 0.2017
  - to: "us/states/mn/districts/house/6a"
    rel: in-district
    area_weight: 0.0864
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Itasca County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 45275 |
| Under 18 | 9125 |
| 18–64 | 24484 |
| 65+ | 11666 |
| Median household income | 68603 |
| Poverty rate | 12.24 |
| Homeownership rate | 83.04 |
| Unemployment rate | 5.93 |
| Median home value | 225200 |
| Gini index | 0.439 |
| Vacancy rate | 27.8 |
| White | 40183 |
| Black | 360 |
| Asian | 188 |
| Native | 1162 |
| Hispanic/Latino | 691 |
| Bachelor's or higher | 11694 |

## Districts

- [MN-08](/us/states/mn/districts/08.md) — 100% (congressional)
- [MN Senate District 3](/us/states/mn/districts/senate/3.md) — 42% (state senate)
- [MN Senate District 7](/us/states/mn/districts/senate/7.md) — 30% (state senate)
- [MN Senate District 2](/us/states/mn/districts/senate/2.md) — 20% (state senate)
- [MN Senate District 6](/us/states/mn/districts/senate/6.md) — 9% (state senate)
- [MN House District 3A](/us/states/mn/districts/house/3a.md) — 42% (state house)
- [MN House District 7A](/us/states/mn/districts/house/7a.md) — 30% (state house)
- [MN House District 2B](/us/states/mn/districts/house/2b.md) — 20% (state house)
- [MN House District 6A](/us/states/mn/districts/house/6a.md) — 9% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
