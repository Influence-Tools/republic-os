---
type: Jurisdiction
title: "Mower County, MN"
classification: county
fips: "27099"
state: "MN"
demographics:
  population: 40343
  population_under_18: 10284
  population_18_64: 22554
  population_65_plus: 7505
  median_household_income: 73074
  poverty_rate: 10.39
  homeownership_rate: 77.58
  unemployment_rate: 3.93
  median_home_value: 185200
  gini_index: 0.4197
  vacancy_rate: 7.61
  race_white: 30390
  race_black: 1376
  race_asian: 2524
  race_native: 453
  hispanic: 5494
  bachelors_plus: 8608
districts:
  - to: "us/states/mn/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mn/districts/senate/23"
    rel: in-district
    area_weight: 0.8055
  - to: "us/states/mn/districts/senate/26"
    rel: in-district
    area_weight: 0.1945
  - to: "us/states/mn/districts/house/23b"
    rel: in-district
    area_weight: 0.8055
  - to: "us/states/mn/districts/house/26b"
    rel: in-district
    area_weight: 0.1945
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Mower County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 40343 |
| Under 18 | 10284 |
| 18–64 | 22554 |
| 65+ | 7505 |
| Median household income | 73074 |
| Poverty rate | 10.39 |
| Homeownership rate | 77.58 |
| Unemployment rate | 3.93 |
| Median home value | 185200 |
| Gini index | 0.4197 |
| Vacancy rate | 7.61 |
| White | 30390 |
| Black | 1376 |
| Asian | 2524 |
| Native | 453 |
| Hispanic/Latino | 5494 |
| Bachelor's or higher | 8608 |

## Districts

- [MN-01](/us/states/mn/districts/01.md) — 100% (congressional)
- [MN Senate District 23](/us/states/mn/districts/senate/23.md) — 81% (state senate)
- [MN Senate District 26](/us/states/mn/districts/senate/26.md) — 19% (state senate)
- [MN House District 23B](/us/states/mn/districts/house/23b.md) — 81% (state house)
- [MN House District 26B](/us/states/mn/districts/house/26b.md) — 19% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
