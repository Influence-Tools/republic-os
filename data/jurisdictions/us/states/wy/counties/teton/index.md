---
type: Jurisdiction
title: "Teton County, WY"
classification: county
fips: "56039"
state: "WY"
demographics:
  population: 23396
  population_under_18: 3996
  population_18_64: 15207
  population_65_plus: 4193
  median_household_income: 124172
  poverty_rate: 5.73
  homeownership_rate: 58.34
  unemployment_rate: 1.75
  median_home_value: 1633900
  gini_index: 0.5367
  vacancy_rate: 28.03
  race_white: 18227
  race_black: 95
  race_asian: 368
  race_native: 61
  hispanic: 3575
  bachelors_plus: 14972
districts:
  - to: "us/states/wy/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wy/districts/senate/17"
    rel: in-district
    area_weight: 0.9327
  - to: "us/states/wy/districts/senate/16"
    rel: in-district
    area_weight: 0.0671
  - to: "us/states/wy/districts/house/23"
    rel: in-district
    area_weight: 0.9322
  - to: "us/states/wy/districts/house/22"
    rel: in-district
    area_weight: 0.0671
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wy]
timestamp: "2026-07-03"
---

# Teton County, WY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 23396 |
| Under 18 | 3996 |
| 18–64 | 15207 |
| 65+ | 4193 |
| Median household income | 124172 |
| Poverty rate | 5.73 |
| Homeownership rate | 58.34 |
| Unemployment rate | 1.75 |
| Median home value | 1633900 |
| Gini index | 0.5367 |
| Vacancy rate | 28.03 |
| White | 18227 |
| Black | 95 |
| Asian | 368 |
| Native | 61 |
| Hispanic/Latino | 3575 |
| Bachelor's or higher | 14972 |

## Districts

- [WY-00](/us/states/wy/districts/00.md) — 100% (congressional)
- [WY Senate District 17](/us/states/wy/districts/senate/17.md) — 93% (state senate)
- [WY Senate District 16](/us/states/wy/districts/senate/16.md) — 7% (state senate)
- [WY House District 23](/us/states/wy/districts/house/23.md) — 93% (state house)
- [WY House District 22](/us/states/wy/districts/house/22.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
