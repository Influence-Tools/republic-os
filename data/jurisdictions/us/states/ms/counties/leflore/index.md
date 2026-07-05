---
type: Jurisdiction
title: "Leflore County, MS"
classification: county
fips: "28083"
state: "MS"
demographics:
  population: 27141
  population_under_18: 7406
  population_18_64: 15632
  population_65_plus: 4103
  median_household_income: 35277
  poverty_rate: 31.5
  homeownership_rate: 52.45
  unemployment_rate: 11.61
  median_home_value: 101200
  gini_index: 0.528
  vacancy_rate: 19.15
  race_white: 5662
  race_black: 20177
  race_asian: 62
  race_native: 29
  hispanic: 874
  bachelors_plus: 5268
districts:
  - to: "us/states/ms/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ms/districts/senate/24"
    rel: in-district
    area_weight: 0.9613
  - to: "us/states/ms/districts/senate/14"
    rel: in-district
    area_weight: 0.0385
  - to: "us/states/ms/districts/house/32"
    rel: in-district
    area_weight: 0.592
  - to: "us/states/ms/districts/house/51"
    rel: in-district
    area_weight: 0.2436
  - to: "us/states/ms/districts/house/46"
    rel: in-district
    area_weight: 0.1642
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Leflore County, MS

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 27141 |
| Under 18 | 7406 |
| 18–64 | 15632 |
| 65+ | 4103 |
| Median household income | 35277 |
| Poverty rate | 31.5 |
| Homeownership rate | 52.45 |
| Unemployment rate | 11.61 |
| Median home value | 101200 |
| Gini index | 0.528 |
| Vacancy rate | 19.15 |
| White | 5662 |
| Black | 20177 |
| Asian | 62 |
| Native | 29 |
| Hispanic/Latino | 874 |
| Bachelor's or higher | 5268 |

## Districts

- [MS-02](/us/states/ms/districts/02.md) — 100% (congressional)
- [MS Senate District 24](/us/states/ms/districts/senate/24.md) — 96% (state senate)
- [MS Senate District 14](/us/states/ms/districts/senate/14.md) — 4% (state senate)
- [MS House District 32](/us/states/ms/districts/house/32.md) — 59% (state house)
- [MS House District 51](/us/states/ms/districts/house/51.md) — 24% (state house)
- [MS House District 46](/us/states/ms/districts/house/46.md) — 16% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
