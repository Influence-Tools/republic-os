---
type: Jurisdiction
title: "Brown County, MN"
classification: county
fips: "27015"
state: "MN"
demographics:
  population: 25800
  population_under_18: 5639
  population_18_64: 14431
  population_65_plus: 5730
  median_household_income: 69378
  poverty_rate: 8.47
  homeownership_rate: 78.9
  unemployment_rate: 2.89
  median_home_value: 191200
  gini_index: 0.4083
  vacancy_rate: 6.76
  race_white: 23916
  race_black: 249
  race_asian: 132
  race_native: 72
  hispanic: 1327
  bachelors_plus: 5782
districts:
  - to: "us/states/mn/districts/01"
    rel: in-district
    area_weight: 0.623
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 0.377
  - to: "us/states/mn/districts/senate/15"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/mn/districts/house/15b"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Brown County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25800 |
| Under 18 | 5639 |
| 18–64 | 14431 |
| 65+ | 5730 |
| Median household income | 69378 |
| Poverty rate | 8.47 |
| Homeownership rate | 78.9 |
| Unemployment rate | 2.89 |
| Median home value | 191200 |
| Gini index | 0.4083 |
| Vacancy rate | 6.76 |
| White | 23916 |
| Black | 249 |
| Asian | 132 |
| Native | 72 |
| Hispanic/Latino | 1327 |
| Bachelor's or higher | 5782 |

## Districts

- [MN-01](/us/states/mn/districts/01.md) — 62% (congressional)
- [MN-07](/us/states/mn/districts/07.md) — 38% (congressional)
- [MN Senate District 15](/us/states/mn/districts/senate/15.md) — 100% (state senate)
- [MN House District 15B](/us/states/mn/districts/house/15b.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
