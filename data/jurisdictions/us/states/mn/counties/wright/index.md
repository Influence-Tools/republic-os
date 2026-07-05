---
type: Jurisdiction
title: "Wright County, MN"
classification: county
fips: "27171"
state: "MN"
demographics:
  population: 148269
  population_under_18: 40305
  population_18_64: 87573
  population_65_plus: 20391
  median_household_income: 107209
  poverty_rate: 5.18
  homeownership_rate: 84.1
  unemployment_rate: 2.73
  median_home_value: 358900
  gini_index: 0.3901
  vacancy_rate: 5.93
  race_white: 131418
  race_black: 3463
  race_asian: 2701
  race_native: 390
  hispanic: 5389
  bachelors_plus: 42289
districts:
  - to: "us/states/mn/districts/06"
    rel: in-district
    area_weight: 0.9986
  - to: "us/states/mn/districts/senate/29"
    rel: in-district
    area_weight: 0.7462
  - to: "us/states/mn/districts/senate/30"
    rel: in-district
    area_weight: 0.1538
  - to: "us/states/mn/districts/senate/17"
    rel: in-district
    area_weight: 0.0997
  - to: "us/states/mn/districts/house/29a"
    rel: in-district
    area_weight: 0.5169
  - to: "us/states/mn/districts/house/29b"
    rel: in-district
    area_weight: 0.2293
  - to: "us/states/mn/districts/house/30a"
    rel: in-district
    area_weight: 0.1376
  - to: "us/states/mn/districts/house/17a"
    rel: in-district
    area_weight: 0.0996
  - to: "us/states/mn/districts/house/30b"
    rel: in-district
    area_weight: 0.0162
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Wright County, MN

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 148269 |
| Under 18 | 40305 |
| 18–64 | 87573 |
| 65+ | 20391 |
| Median household income | 107209 |
| Poverty rate | 5.18 |
| Homeownership rate | 84.1 |
| Unemployment rate | 2.73 |
| Median home value | 358900 |
| Gini index | 0.3901 |
| Vacancy rate | 5.93 |
| White | 131418 |
| Black | 3463 |
| Asian | 2701 |
| Native | 390 |
| Hispanic/Latino | 5389 |
| Bachelor's or higher | 42289 |

## Districts

- [MN-06](/us/states/mn/districts/06.md) — 100% (congressional)
- [MN Senate District 29](/us/states/mn/districts/senate/29.md) — 75% (state senate)
- [MN Senate District 30](/us/states/mn/districts/senate/30.md) — 15% (state senate)
- [MN Senate District 17](/us/states/mn/districts/senate/17.md) — 10% (state senate)
- [MN House District 29A](/us/states/mn/districts/house/29a.md) — 52% (state house)
- [MN House District 29B](/us/states/mn/districts/house/29b.md) — 23% (state house)
- [MN House District 30A](/us/states/mn/districts/house/30a.md) — 14% (state house)
- [MN House District 17A](/us/states/mn/districts/house/17a.md) — 10% (state house)
- [MN House District 30B](/us/states/mn/districts/house/30b.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
