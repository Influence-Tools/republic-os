---
type: Jurisdiction
title: "Hancock County, ME"
classification: county
fips: "23009"
state: "ME"
demographics:
  population: 56460
  population_under_18: 9153
  population_18_64: 32286
  population_65_plus: 15021
  median_household_income: 72744
  poverty_rate: 9.92
  homeownership_rate: 78.54
  unemployment_rate: 4.6
  median_home_value: 310400
  gini_index: 0.4575
  vacancy_rate: 37.27
  race_white: 52554
  race_black: 537
  race_asian: 542
  race_native: 237
  hispanic: 1050
  bachelors_plus: 23917
districts:
  - to: "us/states/me/districts/02"
    rel: in-district
    area_weight: 0.801
  - to: "us/states/me/districts/senate/6"
    rel: in-district
    area_weight: 0.4224
  - to: "us/states/me/districts/senate/7"
    rel: in-district
    area_weight: 0.2708
  - to: "us/states/me/districts/senate/10"
    rel: in-district
    area_weight: 0.0553
  - to: "us/states/me/districts/house/18"
    rel: in-district
    area_weight: 0.3583
  - to: "us/states/me/districts/house/16"
    rel: in-district
    area_weight: 0.0862
  - to: "us/states/me/districts/house/12"
    rel: in-district
    area_weight: 0.0744
  - to: "us/states/me/districts/house/17"
    rel: in-district
    area_weight: 0.069
  - to: "us/states/me/districts/house/13"
    rel: in-district
    area_weight: 0.0608
  - to: "us/states/me/districts/house/15"
    rel: in-district
    area_weight: 0.0526
  - to: "us/states/me/districts/house/14"
    rel: in-district
    area_weight: 0.0473
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, me]
timestamp: "2026-07-03"
---

# Hancock County, ME

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 56460 |
| Under 18 | 9153 |
| 18–64 | 32286 |
| 65+ | 15021 |
| Median household income | 72744 |
| Poverty rate | 9.92 |
| Homeownership rate | 78.54 |
| Unemployment rate | 4.6 |
| Median home value | 310400 |
| Gini index | 0.4575 |
| Vacancy rate | 37.27 |
| White | 52554 |
| Black | 537 |
| Asian | 542 |
| Native | 237 |
| Hispanic/Latino | 1050 |
| Bachelor's or higher | 23917 |

## Districts

- [ME-02](/us/states/me/districts/02.md) — 80% (congressional)
- [ME Senate District 6](/us/states/me/districts/senate/6.md) — 42% (state senate)
- [ME Senate District 7](/us/states/me/districts/senate/7.md) — 27% (state senate)
- [ME Senate District 10](/us/states/me/districts/senate/10.md) — 6% (state senate)
- [ME House District 18](/us/states/me/districts/house/18.md) — 36% (state house)
- [ME House District 16](/us/states/me/districts/house/16.md) — 9% (state house)
- [ME House District 12](/us/states/me/districts/house/12.md) — 7% (state house)
- [ME House District 17](/us/states/me/districts/house/17.md) — 7% (state house)
- [ME House District 13](/us/states/me/districts/house/13.md) — 6% (state house)
- [ME House District 15](/us/states/me/districts/house/15.md) — 5% (state house)
- [ME House District 14](/us/states/me/districts/house/14.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
