---
type: Jurisdiction
title: "Knox County, ME"
classification: county
fips: "23013"
state: "ME"
demographics:
  population: 41003
  population_under_18: 6902
  population_18_64: 22642
  population_65_plus: 11459
  median_household_income: 74096
  poverty_rate: 8.18
  homeownership_rate: 78.72
  unemployment_rate: 3.88
  median_home_value: 324900
  gini_index: 0.4474
  vacancy_rate: 24.75
  race_white: 38422
  race_black: 118
  race_asian: 202
  race_native: 53
  hispanic: 768
  bachelors_plus: 17373
districts:
  - to: "us/states/me/districts/01"
    rel: in-district
    area_weight: 0.4059
  - to: "us/states/me/districts/senate/12"
    rel: in-district
    area_weight: 0.3144
  - to: "us/states/me/districts/senate/13"
    rel: in-district
    area_weight: 0.0348
  - to: "us/states/me/districts/senate/7"
    rel: in-district
    area_weight: 0.0123
  - to: "us/states/me/districts/house/44"
    rel: in-district
    area_weight: 0.0949
  - to: "us/states/me/districts/house/43"
    rel: in-district
    area_weight: 0.0749
  - to: "us/states/me/districts/house/45"
    rel: in-district
    area_weight: 0.05
  - to: "us/states/me/districts/house/15"
    rel: in-district
    area_weight: 0.04
  - to: "us/states/me/districts/house/41"
    rel: in-district
    area_weight: 0.0377
  - to: "us/states/me/districts/house/42"
    rel: in-district
    area_weight: 0.0344
  - to: "us/states/me/districts/house/40"
    rel: in-district
    area_weight: 0.0297
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, me]
timestamp: "2026-07-03"
---

# Knox County, ME

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 41003 |
| Under 18 | 6902 |
| 18–64 | 22642 |
| 65+ | 11459 |
| Median household income | 74096 |
| Poverty rate | 8.18 |
| Homeownership rate | 78.72 |
| Unemployment rate | 3.88 |
| Median home value | 324900 |
| Gini index | 0.4474 |
| Vacancy rate | 24.75 |
| White | 38422 |
| Black | 118 |
| Asian | 202 |
| Native | 53 |
| Hispanic/Latino | 768 |
| Bachelor's or higher | 17373 |

## Districts

- [ME-01](/us/states/me/districts/01.md) — 41% (congressional)
- [ME Senate District 12](/us/states/me/districts/senate/12.md) — 31% (state senate)
- [ME Senate District 13](/us/states/me/districts/senate/13.md) — 3% (state senate)
- [ME Senate District 7](/us/states/me/districts/senate/7.md) — 1% (state senate)
- [ME House District 44](/us/states/me/districts/house/44.md) — 9% (state house)
- [ME House District 43](/us/states/me/districts/house/43.md) — 7% (state house)
- [ME House District 45](/us/states/me/districts/house/45.md) — 5% (state house)
- [ME House District 15](/us/states/me/districts/house/15.md) — 4% (state house)
- [ME House District 41](/us/states/me/districts/house/41.md) — 4% (state house)
- [ME House District 42](/us/states/me/districts/house/42.md) — 3% (state house)
- [ME House District 40](/us/states/me/districts/house/40.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
