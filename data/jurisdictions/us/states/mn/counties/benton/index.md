---
type: Jurisdiction
title: "Benton County, MN"
classification: county
fips: "27009"
state: "MN"
demographics:
  population: 41593
  population_under_18: 10527
  population_18_64: 25239
  population_65_plus: 5827
  median_household_income: 74410
  poverty_rate: 9.87
  homeownership_rate: 66.73
  unemployment_rate: 3.94
  median_home_value: 271000
  gini_index: 0.4057
  vacancy_rate: 5.05
  race_white: 36110
  race_black: 2296
  race_asian: 445
  race_native: 115
  hispanic: 1460
  bachelors_plus: 9264
districts:
  - to: "us/states/mn/districts/06"
    rel: in-district
    area_weight: 0.9977
  - to: "us/states/mn/districts/senate/10"
    rel: in-district
    area_weight: 0.873
  - to: "us/states/mn/districts/senate/14"
    rel: in-district
    area_weight: 0.0903
  - to: "us/states/mn/districts/senate/13"
    rel: in-district
    area_weight: 0.0367
  - to: "us/states/mn/districts/house/10b"
    rel: in-district
    area_weight: 0.873
  - to: "us/states/mn/districts/house/14b"
    rel: in-district
    area_weight: 0.0903
  - to: "us/states/mn/districts/house/13b"
    rel: in-district
    area_weight: 0.0367
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Benton County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 41593 |
| Under 18 | 10527 |
| 18–64 | 25239 |
| 65+ | 5827 |
| Median household income | 74410 |
| Poverty rate | 9.87 |
| Homeownership rate | 66.73 |
| Unemployment rate | 3.94 |
| Median home value | 271000 |
| Gini index | 0.4057 |
| Vacancy rate | 5.05 |
| White | 36110 |
| Black | 2296 |
| Asian | 445 |
| Native | 115 |
| Hispanic/Latino | 1460 |
| Bachelor's or higher | 9264 |

## Districts

- [MN-06](/us/states/mn/districts/06.md) — 100% (congressional)
- [MN Senate District 10](/us/states/mn/districts/senate/10.md) — 87% (state senate)
- [MN Senate District 14](/us/states/mn/districts/senate/14.md) — 9% (state senate)
- [MN Senate District 13](/us/states/mn/districts/senate/13.md) — 4% (state senate)
- [MN House District 10B](/us/states/mn/districts/house/10b.md) — 87% (state house)
- [MN House District 14B](/us/states/mn/districts/house/14b.md) — 9% (state house)
- [MN House District 13B](/us/states/mn/districts/house/13b.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
