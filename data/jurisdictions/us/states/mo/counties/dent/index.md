---
type: Jurisdiction
title: "Dent County, MO"
classification: county
fips: "29065"
state: "MO"
demographics:
  population: 14539
  population_under_18: 3279
  population_18_64: 8027
  population_65_plus: 3233
  median_household_income: 56312
  poverty_rate: 12.22
  homeownership_rate: 75.93
  unemployment_rate: 4.44
  median_home_value: 167500
  gini_index: 0.4444
  vacancy_rate: 17.65
  race_white: 13353
  race_black: 68
  race_asian: 124
  race_native: 103
  hispanic: 324
  bachelors_plus: 2333
districts:
  - to: "us/states/mo/districts/08"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/senate/16"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/house/120"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Dent County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14539 |
| Under 18 | 3279 |
| 18–64 | 8027 |
| 65+ | 3233 |
| Median household income | 56312 |
| Poverty rate | 12.22 |
| Homeownership rate | 75.93 |
| Unemployment rate | 4.44 |
| Median home value | 167500 |
| Gini index | 0.4444 |
| Vacancy rate | 17.65 |
| White | 13353 |
| Black | 68 |
| Asian | 124 |
| Native | 103 |
| Hispanic/Latino | 324 |
| Bachelor's or higher | 2333 |

## Districts

- [MO-08](/us/states/mo/districts/08.md) — 100% (congressional)
- [MO Senate District 16](/us/states/mo/districts/senate/16.md) — 100% (state senate)
- [MO House District 120](/us/states/mo/districts/house/120.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
