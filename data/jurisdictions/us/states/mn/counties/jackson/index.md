---
type: Jurisdiction
title: "Jackson County, MN"
classification: county
fips: "27063"
state: "MN"
demographics:
  population: 9933
  population_under_18: 2163
  population_18_64: 5447
  population_65_plus: 2323
  median_household_income: 75743
  poverty_rate: 8.6
  homeownership_rate: 80.15
  unemployment_rate: 2.42
  median_home_value: 157100
  gini_index: 0.4399
  vacancy_rate: 10.56
  race_white: 9026
  race_black: 59
  race_asian: 131
  race_native: 16
  hispanic: 484
  bachelors_plus: 2419
districts:
  - to: "us/states/mn/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mn/districts/senate/21"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mn/districts/house/21b"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Jackson County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9933 |
| Under 18 | 2163 |
| 18–64 | 5447 |
| 65+ | 2323 |
| Median household income | 75743 |
| Poverty rate | 8.6 |
| Homeownership rate | 80.15 |
| Unemployment rate | 2.42 |
| Median home value | 157100 |
| Gini index | 0.4399 |
| Vacancy rate | 10.56 |
| White | 9026 |
| Black | 59 |
| Asian | 131 |
| Native | 16 |
| Hispanic/Latino | 484 |
| Bachelor's or higher | 2419 |

## Districts

- [MN-01](/us/states/mn/districts/01.md) — 100% (congressional)
- [MN Senate District 21](/us/states/mn/districts/senate/21.md) — 100% (state senate)
- [MN House District 21B](/us/states/mn/districts/house/21b.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
