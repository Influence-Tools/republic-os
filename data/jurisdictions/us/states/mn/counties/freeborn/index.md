---
type: Jurisdiction
title: "Freeborn County, MN"
classification: county
fips: "27047"
state: "MN"
demographics:
  population: 30623
  population_under_18: 6664
  population_18_64: 16802
  population_65_plus: 7157
  median_household_income: 71023
  poverty_rate: 10.63
  homeownership_rate: 79.5
  unemployment_rate: 4.61
  median_home_value: 171100
  gini_index: 0.4573
  vacancy_rate: 9.0
  race_white: 25699
  race_black: 479
  race_asian: 1086
  race_native: 91
  hispanic: 3302
  bachelors_plus: 5254
districts:
  - to: "us/states/mn/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mn/districts/senate/23"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mn/districts/house/23a"
    rel: in-district
    area_weight: 0.7017
  - to: "us/states/mn/districts/house/23b"
    rel: in-district
    area_weight: 0.2983
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Freeborn County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 30623 |
| Under 18 | 6664 |
| 18–64 | 16802 |
| 65+ | 7157 |
| Median household income | 71023 |
| Poverty rate | 10.63 |
| Homeownership rate | 79.5 |
| Unemployment rate | 4.61 |
| Median home value | 171100 |
| Gini index | 0.4573 |
| Vacancy rate | 9.0 |
| White | 25699 |
| Black | 479 |
| Asian | 1086 |
| Native | 91 |
| Hispanic/Latino | 3302 |
| Bachelor's or higher | 5254 |

## Districts

- [MN-01](/us/states/mn/districts/01.md) — 100% (congressional)
- [MN Senate District 23](/us/states/mn/districts/senate/23.md) — 100% (state senate)
- [MN House District 23A](/us/states/mn/districts/house/23a.md) — 70% (state house)
- [MN House District 23B](/us/states/mn/districts/house/23b.md) — 30% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
