---
type: Jurisdiction
title: "Cass County, MN"
classification: county
fips: "27021"
state: "MN"
demographics:
  population: 30992
  population_under_18: 6190
  population_18_64: 16294
  population_65_plus: 8508
  median_household_income: 68874
  poverty_rate: 12.81
  homeownership_rate: 86.19
  unemployment_rate: 6.56
  median_home_value: 288300
  gini_index: 0.4456
  vacancy_rate: 47.39
  race_white: 25081
  race_black: 114
  race_asian: 150
  race_native: 2857
  hispanic: 565
  bachelors_plus: 7663
districts:
  - to: "us/states/mn/districts/08"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/mn/districts/senate/2"
    rel: in-district
    area_weight: 0.4303
  - to: "us/states/mn/districts/senate/5"
    rel: in-district
    area_weight: 0.3467
  - to: "us/states/mn/districts/senate/6"
    rel: in-district
    area_weight: 0.223
  - to: "us/states/mn/districts/house/2b"
    rel: in-district
    area_weight: 0.4303
  - to: "us/states/mn/districts/house/5a"
    rel: in-district
    area_weight: 0.2614
  - to: "us/states/mn/districts/house/6a"
    rel: in-district
    area_weight: 0.223
  - to: "us/states/mn/districts/house/5b"
    rel: in-district
    area_weight: 0.0853
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Cass County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 30992 |
| Under 18 | 6190 |
| 18–64 | 16294 |
| 65+ | 8508 |
| Median household income | 68874 |
| Poverty rate | 12.81 |
| Homeownership rate | 86.19 |
| Unemployment rate | 6.56 |
| Median home value | 288300 |
| Gini index | 0.4456 |
| Vacancy rate | 47.39 |
| White | 25081 |
| Black | 114 |
| Asian | 150 |
| Native | 2857 |
| Hispanic/Latino | 565 |
| Bachelor's or higher | 7663 |

## Districts

- [MN-08](/us/states/mn/districts/08.md) — 100% (congressional)
- [MN Senate District 2](/us/states/mn/districts/senate/2.md) — 43% (state senate)
- [MN Senate District 5](/us/states/mn/districts/senate/5.md) — 35% (state senate)
- [MN Senate District 6](/us/states/mn/districts/senate/6.md) — 22% (state senate)
- [MN House District 2B](/us/states/mn/districts/house/2b.md) — 43% (state house)
- [MN House District 5A](/us/states/mn/districts/house/5a.md) — 26% (state house)
- [MN House District 6A](/us/states/mn/districts/house/6a.md) — 22% (state house)
- [MN House District 5B](/us/states/mn/districts/house/5b.md) — 9% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
