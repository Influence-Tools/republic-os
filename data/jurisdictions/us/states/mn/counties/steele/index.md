---
type: Jurisdiction
title: "Steele County, MN"
classification: county
fips: "27147"
state: "MN"
demographics:
  population: 37439
  population_under_18: 9095
  population_18_64: 21157
  population_65_plus: 7187
  median_household_income: 84196
  poverty_rate: 8.33
  homeownership_rate: 79.4
  unemployment_rate: 3.41
  median_home_value: 245400
  gini_index: 0.4145
  vacancy_rate: 5.36
  race_white: 32125
  race_black: 1253
  race_asian: 275
  race_native: 129
  hispanic: 3326
  bachelors_plus: 9261
districts:
  - to: "us/states/mn/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mn/districts/senate/23"
    rel: in-district
    area_weight: 0.5004
  - to: "us/states/mn/districts/senate/19"
    rel: in-district
    area_weight: 0.4995
  - to: "us/states/mn/districts/house/19b"
    rel: in-district
    area_weight: 0.4995
  - to: "us/states/mn/districts/house/23a"
    rel: in-district
    area_weight: 0.4168
  - to: "us/states/mn/districts/house/23b"
    rel: in-district
    area_weight: 0.0836
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Steele County, MN

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 37439 |
| Under 18 | 9095 |
| 18–64 | 21157 |
| 65+ | 7187 |
| Median household income | 84196 |
| Poverty rate | 8.33 |
| Homeownership rate | 79.4 |
| Unemployment rate | 3.41 |
| Median home value | 245400 |
| Gini index | 0.4145 |
| Vacancy rate | 5.36 |
| White | 32125 |
| Black | 1253 |
| Asian | 275 |
| Native | 129 |
| Hispanic/Latino | 3326 |
| Bachelor's or higher | 9261 |

## Districts

- [MN-01](/us/states/mn/districts/01.md) — 100% (congressional)
- [MN Senate District 23](/us/states/mn/districts/senate/23.md) — 50% (state senate)
- [MN Senate District 19](/us/states/mn/districts/senate/19.md) — 50% (state senate)
- [MN House District 19B](/us/states/mn/districts/house/19b.md) — 50% (state house)
- [MN House District 23A](/us/states/mn/districts/house/23a.md) — 42% (state house)
- [MN House District 23B](/us/states/mn/districts/house/23b.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
