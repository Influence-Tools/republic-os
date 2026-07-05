---
type: Jurisdiction
title: "Kanabec County, MN"
classification: county
fips: "27065"
state: "MN"
demographics:
  population: 16390
  population_under_18: 3490
  population_18_64: 9284
  population_65_plus: 3616
  median_household_income: 71460
  poverty_rate: 10.02
  homeownership_rate: 84.54
  unemployment_rate: 4.59
  median_home_value: 228100
  gini_index: 0.41
  vacancy_rate: 16.26
  race_white: 15337
  race_black: 143
  race_asian: 88
  race_native: 106
  hispanic: 296
  bachelors_plus: 2496
districts:
  - to: "us/states/mn/districts/08"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mn/districts/senate/11"
    rel: in-district
    area_weight: 0.5241
  - to: "us/states/mn/districts/senate/10"
    rel: in-district
    area_weight: 0.4759
  - to: "us/states/mn/districts/house/11b"
    rel: in-district
    area_weight: 0.5241
  - to: "us/states/mn/districts/house/10a"
    rel: in-district
    area_weight: 0.3381
  - to: "us/states/mn/districts/house/10b"
    rel: in-district
    area_weight: 0.1377
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Kanabec County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16390 |
| Under 18 | 3490 |
| 18–64 | 9284 |
| 65+ | 3616 |
| Median household income | 71460 |
| Poverty rate | 10.02 |
| Homeownership rate | 84.54 |
| Unemployment rate | 4.59 |
| Median home value | 228100 |
| Gini index | 0.41 |
| Vacancy rate | 16.26 |
| White | 15337 |
| Black | 143 |
| Asian | 88 |
| Native | 106 |
| Hispanic/Latino | 296 |
| Bachelor's or higher | 2496 |

## Districts

- [MN-08](/us/states/mn/districts/08.md) — 100% (congressional)
- [MN Senate District 11](/us/states/mn/districts/senate/11.md) — 52% (state senate)
- [MN Senate District 10](/us/states/mn/districts/senate/10.md) — 48% (state senate)
- [MN House District 11B](/us/states/mn/districts/house/11b.md) — 52% (state house)
- [MN House District 10A](/us/states/mn/districts/house/10a.md) — 34% (state house)
- [MN House District 10B](/us/states/mn/districts/house/10b.md) — 14% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
