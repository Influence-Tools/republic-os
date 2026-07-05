---
type: Jurisdiction
title: "Juniata County, PA"
classification: county
fips: "42067"
state: "PA"
demographics:
  population: 23379
  population_under_18: 5161
  population_18_64: 13262
  population_65_plus: 4956
  median_household_income: 66318
  poverty_rate: 9.7
  homeownership_rate: 73.81
  unemployment_rate: 2.11
  median_home_value: 217000
  gini_index: 0.3961
  vacancy_rate: 14.1
  race_white: 21660
  race_black: 233
  race_asian: 112
  race_native: 34
  hispanic: 969
  bachelors_plus: 3295
districts:
  - to: "us/states/pa/districts/13"
    rel: in-district
    area_weight: 0.9985
  - to: "us/states/pa/districts/senate/30"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/pa/districts/house/86"
    rel: in-district
    area_weight: 0.8484
  - to: "us/states/pa/districts/house/85"
    rel: in-district
    area_weight: 0.1515
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Juniata County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 23379 |
| Under 18 | 5161 |
| 18–64 | 13262 |
| 65+ | 4956 |
| Median household income | 66318 |
| Poverty rate | 9.7 |
| Homeownership rate | 73.81 |
| Unemployment rate | 2.11 |
| Median home value | 217000 |
| Gini index | 0.3961 |
| Vacancy rate | 14.1 |
| White | 21660 |
| Black | 233 |
| Asian | 112 |
| Native | 34 |
| Hispanic/Latino | 969 |
| Bachelor's or higher | 3295 |

## Districts

- [PA-13](/us/states/pa/districts/13.md) — 100% (congressional)
- [PA Senate District 30](/us/states/pa/districts/senate/30.md) — 100% (state senate)
- [PA House District 86](/us/states/pa/districts/house/86.md) — 85% (state house)
- [PA House District 85](/us/states/pa/districts/house/85.md) — 15% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
