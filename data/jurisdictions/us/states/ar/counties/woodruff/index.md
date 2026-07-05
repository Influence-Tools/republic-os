---
type: Jurisdiction
title: "Woodruff County, AR"
classification: county
fips: "05147"
state: "AR"
demographics:
  population: 6026
  population_under_18: 1303
  population_18_64: 3228
  population_65_plus: 1495
  median_household_income: 48158
  poverty_rate: 24.05
  homeownership_rate: 64.75
  unemployment_rate: 4.98
  median_home_value: 106500
  gini_index: 0.5044
  vacancy_rate: 17.32
  race_white: 4169
  race_black: 1498
  race_asian: 5
  race_native: 1
  hispanic: 86
  bachelors_plus: 969
districts:
  - to: "us/states/ar/districts/01"
    rel: in-district
    area_weight: 0.9951
  - to: "us/states/ar/districts/senate/10"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ar/districts/house/61"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Woodruff County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6026 |
| Under 18 | 1303 |
| 18–64 | 3228 |
| 65+ | 1495 |
| Median household income | 48158 |
| Poverty rate | 24.05 |
| Homeownership rate | 64.75 |
| Unemployment rate | 4.98 |
| Median home value | 106500 |
| Gini index | 0.5044 |
| Vacancy rate | 17.32 |
| White | 4169 |
| Black | 1498 |
| Asian | 5 |
| Native | 1 |
| Hispanic/Latino | 86 |
| Bachelor's or higher | 969 |

## Districts

- [AR-01](/us/states/ar/districts/01.md) — 100% (congressional)
- [AR Senate District 10](/us/states/ar/districts/senate/10.md) — 100% (state senate)
- [AR House District 61](/us/states/ar/districts/house/61.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
