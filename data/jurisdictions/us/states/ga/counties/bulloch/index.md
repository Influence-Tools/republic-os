---
type: Jurisdiction
title: "Bulloch County, GA"
classification: county
fips: "13031"
state: "GA"
demographics:
  population: 82683
  population_under_18: 16550
  population_18_64: 55868
  population_65_plus: 10265
  median_household_income: 58810
  poverty_rate: 23.01
  homeownership_rate: 53.11
  unemployment_rate: 8.24
  median_home_value: 222500
  gini_index: 0.4846
  vacancy_rate: 9.73
  race_white: 51440
  race_black: 23278
  race_asian: 1195
  race_native: 560
  hispanic: 4263
  bachelors_plus: 21236
districts:
  - to: "us/states/ga/districts/12"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ga/districts/senate/4"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ga/districts/house/160"
    rel: in-district
    area_weight: 0.5194
  - to: "us/states/ga/districts/house/158"
    rel: in-district
    area_weight: 0.2652
  - to: "us/states/ga/districts/house/159"
    rel: in-district
    area_weight: 0.2153
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Bulloch County, GA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 82683 |
| Under 18 | 16550 |
| 18–64 | 55868 |
| 65+ | 10265 |
| Median household income | 58810 |
| Poverty rate | 23.01 |
| Homeownership rate | 53.11 |
| Unemployment rate | 8.24 |
| Median home value | 222500 |
| Gini index | 0.4846 |
| Vacancy rate | 9.73 |
| White | 51440 |
| Black | 23278 |
| Asian | 1195 |
| Native | 560 |
| Hispanic/Latino | 4263 |
| Bachelor's or higher | 21236 |

## Districts

- [GA-12](/us/states/ga/districts/12.md) — 100% (congressional)
- [GA Senate District 4](/us/states/ga/districts/senate/4.md) — 100% (state senate)
- [GA House District 160](/us/states/ga/districts/house/160.md) — 52% (state house)
- [GA House District 158](/us/states/ga/districts/house/158.md) — 27% (state house)
- [GA House District 159](/us/states/ga/districts/house/159.md) — 22% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
