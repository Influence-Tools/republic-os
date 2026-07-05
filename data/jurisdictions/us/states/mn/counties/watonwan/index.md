---
type: Jurisdiction
title: "Watonwan County, MN"
classification: county
fips: "27165"
state: "MN"
demographics:
  population: 11205
  population_under_18: 2948
  population_18_64: 5992
  population_65_plus: 2265
  median_household_income: 71699
  poverty_rate: 13.19
  homeownership_rate: 77.83
  unemployment_rate: 5.25
  median_home_value: 162400
  gini_index: 0.439
  vacancy_rate: 13.4
  race_white: 8278
  race_black: 4
  race_asian: 36
  race_native: 118
  hispanic: 3401
  bachelors_plus: 1584
districts:
  - to: "us/states/mn/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mn/districts/senate/22"
    rel: in-district
    area_weight: 0.5097
  - to: "us/states/mn/districts/senate/21"
    rel: in-district
    area_weight: 0.4903
  - to: "us/states/mn/districts/house/22a"
    rel: in-district
    area_weight: 0.5097
  - to: "us/states/mn/districts/house/21b"
    rel: in-district
    area_weight: 0.4903
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Watonwan County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11205 |
| Under 18 | 2948 |
| 18–64 | 5992 |
| 65+ | 2265 |
| Median household income | 71699 |
| Poverty rate | 13.19 |
| Homeownership rate | 77.83 |
| Unemployment rate | 5.25 |
| Median home value | 162400 |
| Gini index | 0.439 |
| Vacancy rate | 13.4 |
| White | 8278 |
| Black | 4 |
| Asian | 36 |
| Native | 118 |
| Hispanic/Latino | 3401 |
| Bachelor's or higher | 1584 |

## Districts

- [MN-01](/us/states/mn/districts/01.md) — 100% (congressional)
- [MN Senate District 22](/us/states/mn/districts/senate/22.md) — 51% (state senate)
- [MN Senate District 21](/us/states/mn/districts/senate/21.md) — 49% (state senate)
- [MN House District 22A](/us/states/mn/districts/house/22a.md) — 51% (state house)
- [MN House District 21B](/us/states/mn/districts/house/21b.md) — 49% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
