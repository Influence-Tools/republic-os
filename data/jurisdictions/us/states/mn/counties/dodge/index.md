---
type: Jurisdiction
title: "Dodge County, MN"
classification: county
fips: "27039"
state: "MN"
demographics:
  population: 21045
  population_under_18: 5279
  population_18_64: 12417
  population_65_plus: 3349
  median_household_income: 95739
  poverty_rate: 7.04
  homeownership_rate: 86.56
  unemployment_rate: 3.29
  median_home_value: 287700
  gini_index: 0.3826
  vacancy_rate: 4.73
  race_white: 19069
  race_black: 234
  race_asian: 110
  race_native: 52
  hispanic: 1136
  bachelors_plus: 5524
districts:
  - to: "us/states/mn/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mn/districts/senate/24"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mn/districts/house/24a"
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

# Dodge County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21045 |
| Under 18 | 5279 |
| 18–64 | 12417 |
| 65+ | 3349 |
| Median household income | 95739 |
| Poverty rate | 7.04 |
| Homeownership rate | 86.56 |
| Unemployment rate | 3.29 |
| Median home value | 287700 |
| Gini index | 0.3826 |
| Vacancy rate | 4.73 |
| White | 19069 |
| Black | 234 |
| Asian | 110 |
| Native | 52 |
| Hispanic/Latino | 1136 |
| Bachelor's or higher | 5524 |

## Districts

- [MN-01](/us/states/mn/districts/01.md) — 100% (congressional)
- [MN Senate District 24](/us/states/mn/districts/senate/24.md) — 100% (state senate)
- [MN House District 24A](/us/states/mn/districts/house/24a.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
