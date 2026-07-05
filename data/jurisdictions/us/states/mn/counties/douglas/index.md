---
type: Jurisdiction
title: "Douglas County, MN"
classification: county
fips: "27041"
state: "MN"
demographics:
  population: 39575
  population_under_18: 8482
  population_18_64: 21449
  population_65_plus: 9644
  median_household_income: 79043
  poverty_rate: 8.98
  homeownership_rate: 76.45
  unemployment_rate: 2.92
  median_home_value: 321400
  gini_index: 0.4416
  vacancy_rate: 21.55
  race_white: 37434
  race_black: 218
  race_asian: 220
  race_native: 81
  hispanic: 897
  bachelors_plus: 11162
districts:
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mn/districts/senate/9"
    rel: in-district
    area_weight: 0.5503
  - to: "us/states/mn/districts/senate/12"
    rel: in-district
    area_weight: 0.4497
  - to: "us/states/mn/districts/house/9b"
    rel: in-district
    area_weight: 0.5502
  - to: "us/states/mn/districts/house/12b"
    rel: in-district
    area_weight: 0.4497
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Douglas County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 39575 |
| Under 18 | 8482 |
| 18–64 | 21449 |
| 65+ | 9644 |
| Median household income | 79043 |
| Poverty rate | 8.98 |
| Homeownership rate | 76.45 |
| Unemployment rate | 2.92 |
| Median home value | 321400 |
| Gini index | 0.4416 |
| Vacancy rate | 21.55 |
| White | 37434 |
| Black | 218 |
| Asian | 220 |
| Native | 81 |
| Hispanic/Latino | 897 |
| Bachelor's or higher | 11162 |

## Districts

- [MN-07](/us/states/mn/districts/07.md) — 100% (congressional)
- [MN Senate District 9](/us/states/mn/districts/senate/9.md) — 55% (state senate)
- [MN Senate District 12](/us/states/mn/districts/senate/12.md) — 45% (state senate)
- [MN House District 9B](/us/states/mn/districts/house/9b.md) — 55% (state house)
- [MN House District 12B](/us/states/mn/districts/house/12b.md) — 45% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
