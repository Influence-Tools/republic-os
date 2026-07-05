---
type: Jurisdiction
title: "Norman County, MN"
classification: county
fips: "27107"
state: "MN"
demographics:
  population: 6367
  population_under_18: 1483
  population_18_64: 3505
  population_65_plus: 1379
  median_household_income: 72260
  poverty_rate: 10.12
  homeownership_rate: 79.44
  unemployment_rate: 5.25
  median_home_value: 147100
  gini_index: 0.397
  vacancy_rate: 16.23
  race_white: 5637
  race_black: 34
  race_asian: 28
  race_native: 109
  hispanic: 352
  bachelors_plus: 1250
districts:
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 0.9977
  - to: "us/states/mn/districts/senate/1"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/mn/districts/house/1b"
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

# Norman County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6367 |
| Under 18 | 1483 |
| 18–64 | 3505 |
| 65+ | 1379 |
| Median household income | 72260 |
| Poverty rate | 10.12 |
| Homeownership rate | 79.44 |
| Unemployment rate | 5.25 |
| Median home value | 147100 |
| Gini index | 0.397 |
| Vacancy rate | 16.23 |
| White | 5637 |
| Black | 34 |
| Asian | 28 |
| Native | 109 |
| Hispanic/Latino | 352 |
| Bachelor's or higher | 1250 |

## Districts

- [MN-07](/us/states/mn/districts/07.md) — 100% (congressional)
- [MN Senate District 1](/us/states/mn/districts/senate/1.md) — 100% (state senate)
- [MN House District 1B](/us/states/mn/districts/house/1b.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
