---
type: Jurisdiction
title: "Pennington County, SD"
classification: county
fips: "46103"
state: "SD"
demographics:
  population: 115979
  population_under_18: 28470
  population_18_64: 36175
  population_65_plus: 51334
  median_household_income: 79250
  poverty_rate: 8.82
  homeownership_rate: 69.97
  unemployment_rate: 3.42
  median_home_value: 360900
  gini_index: 0.4209
  vacancy_rate: 11.65
  race_white: 90475
  race_black: 962
  race_asian: 1839
  race_native: 9062
  hispanic: 7116
  bachelors_plus: 40179
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/27"
    rel: in-district
    area_weight: 0.6395
  - to: "us/states/sd/districts/senate/30"
    rel: in-district
    area_weight: 0.278
  - to: "us/states/sd/districts/senate/33"
    rel: in-district
    area_weight: 0.0499
  - to: "us/states/sd/districts/senate/35"
    rel: in-district
    area_weight: 0.0163
  - to: "us/states/sd/districts/senate/34"
    rel: in-district
    area_weight: 0.0132
  - to: "us/states/sd/districts/house/27"
    rel: in-district
    area_weight: 0.6395
  - to: "us/states/sd/districts/house/30"
    rel: in-district
    area_weight: 0.278
  - to: "us/states/sd/districts/house/33"
    rel: in-district
    area_weight: 0.0499
  - to: "us/states/sd/districts/house/35"
    rel: in-district
    area_weight: 0.0163
  - to: "us/states/sd/districts/house/34"
    rel: in-district
    area_weight: 0.0132
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Pennington County, SD

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 115979 |
| Under 18 | 28470 |
| 18–64 | 36175 |
| 65+ | 51334 |
| Median household income | 79250 |
| Poverty rate | 8.82 |
| Homeownership rate | 69.97 |
| Unemployment rate | 3.42 |
| Median home value | 360900 |
| Gini index | 0.4209 |
| Vacancy rate | 11.65 |
| White | 90475 |
| Black | 962 |
| Asian | 1839 |
| Native | 9062 |
| Hispanic/Latino | 7116 |
| Bachelor's or higher | 40179 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 27](/us/states/sd/districts/senate/27.md) — 64% (state senate)
- [SD Senate District 30](/us/states/sd/districts/senate/30.md) — 28% (state senate)
- [SD Senate District 33](/us/states/sd/districts/senate/33.md) — 5% (state senate)
- [SD Senate District 35](/us/states/sd/districts/senate/35.md) — 2% (state senate)
- [SD Senate District 34](/us/states/sd/districts/senate/34.md) — 1% (state senate)
- [SD House District 27](/us/states/sd/districts/house/27.md) — 64% (state house)
- [SD House District 30](/us/states/sd/districts/house/30.md) — 28% (state house)
- [SD House District 33](/us/states/sd/districts/house/33.md) — 5% (state house)
- [SD House District 35](/us/states/sd/districts/house/35.md) — 2% (state house)
- [SD House District 34](/us/states/sd/districts/house/34.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
