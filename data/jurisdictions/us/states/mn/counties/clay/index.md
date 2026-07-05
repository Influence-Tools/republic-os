---
type: Jurisdiction
title: "Clay County, MN"
classification: county
fips: "27027"
state: "MN"
demographics:
  population: 66059
  population_under_18: 16315
  population_18_64: 40496
  population_65_plus: 9248
  median_household_income: 81172
  poverty_rate: 13.26
  homeownership_rate: 65.9
  unemployment_rate: 4.12
  median_home_value: 265500
  gini_index: 0.4432
  vacancy_rate: 4.05
  race_white: 56092
  race_black: 3217
  race_asian: 1059
  race_native: 551
  hispanic: 3290
  bachelors_plus: 21016
districts:
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 0.9981
  - to: "us/states/mn/districts/senate/4"
    rel: in-district
    area_weight: 0.8994
  - to: "us/states/mn/districts/senate/1"
    rel: in-district
    area_weight: 0.1002
  - to: "us/states/mn/districts/house/4b"
    rel: in-district
    area_weight: 0.8832
  - to: "us/states/mn/districts/house/1b"
    rel: in-district
    area_weight: 0.1002
  - to: "us/states/mn/districts/house/4a"
    rel: in-district
    area_weight: 0.0161
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Clay County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 66059 |
| Under 18 | 16315 |
| 18–64 | 40496 |
| 65+ | 9248 |
| Median household income | 81172 |
| Poverty rate | 13.26 |
| Homeownership rate | 65.9 |
| Unemployment rate | 4.12 |
| Median home value | 265500 |
| Gini index | 0.4432 |
| Vacancy rate | 4.05 |
| White | 56092 |
| Black | 3217 |
| Asian | 1059 |
| Native | 551 |
| Hispanic/Latino | 3290 |
| Bachelor's or higher | 21016 |

## Districts

- [MN-07](/us/states/mn/districts/07.md) — 100% (congressional)
- [MN Senate District 4](/us/states/mn/districts/senate/4.md) — 90% (state senate)
- [MN Senate District 1](/us/states/mn/districts/senate/1.md) — 10% (state senate)
- [MN House District 4B](/us/states/mn/districts/house/4b.md) — 88% (state house)
- [MN House District 1B](/us/states/mn/districts/house/1b.md) — 10% (state house)
- [MN House District 4A](/us/states/mn/districts/house/4a.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
