---
type: Jurisdiction
title: "Otter Tail County, MN"
classification: county
fips: "27111"
state: "MN"
demographics:
  population: 60475
  population_under_18: 13137
  population_18_64: 31964
  population_65_plus: 15374
  median_household_income: 72255
  poverty_rate: 8.73
  homeownership_rate: 79.48
  unemployment_rate: 4.78
  median_home_value: 273000
  gini_index: 0.4329
  vacancy_rate: 31.45
  race_white: 55169
  race_black: 658
  race_asian: 349
  race_native: 140
  hispanic: 2397
  bachelors_plus: 16387
districts:
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mn/districts/senate/9"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mn/districts/house/9b"
    rel: in-district
    area_weight: 0.7105
  - to: "us/states/mn/districts/house/9a"
    rel: in-district
    area_weight: 0.2895
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Otter Tail County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 60475 |
| Under 18 | 13137 |
| 18–64 | 31964 |
| 65+ | 15374 |
| Median household income | 72255 |
| Poverty rate | 8.73 |
| Homeownership rate | 79.48 |
| Unemployment rate | 4.78 |
| Median home value | 273000 |
| Gini index | 0.4329 |
| Vacancy rate | 31.45 |
| White | 55169 |
| Black | 658 |
| Asian | 349 |
| Native | 140 |
| Hispanic/Latino | 2397 |
| Bachelor's or higher | 16387 |

## Districts

- [MN-07](/us/states/mn/districts/07.md) — 100% (congressional)
- [MN Senate District 9](/us/states/mn/districts/senate/9.md) — 100% (state senate)
- [MN House District 9B](/us/states/mn/districts/house/9b.md) — 71% (state house)
- [MN House District 9A](/us/states/mn/districts/house/9a.md) — 29% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
