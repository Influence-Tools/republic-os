---
type: Jurisdiction
title: "Montgomery County, MS"
classification: county
fips: "28097"
state: "MS"
demographics:
  population: 9602
  population_under_18: 2162
  population_18_64: 5277
  population_65_plus: 2163
  median_household_income: 41748
  poverty_rate: 25.18
  homeownership_rate: 75.78
  unemployment_rate: 4.72
  median_home_value: 126800
  gini_index: 0.5246
  vacancy_rate: 24.15
  race_white: 4989
  race_black: 4283
  race_asian: 1
  race_native: 0
  hispanic: 21
  bachelors_plus: 1899
districts:
  - to: "us/states/ms/districts/02"
    rel: in-district
    area_weight: 0.9988
  - to: "us/states/ms/districts/senate/14"
    rel: in-district
    area_weight: 0.5519
  - to: "us/states/ms/districts/senate/15"
    rel: in-district
    area_weight: 0.4481
  - to: "us/states/ms/districts/house/46"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Montgomery County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9602 |
| Under 18 | 2162 |
| 18–64 | 5277 |
| 65+ | 2163 |
| Median household income | 41748 |
| Poverty rate | 25.18 |
| Homeownership rate | 75.78 |
| Unemployment rate | 4.72 |
| Median home value | 126800 |
| Gini index | 0.5246 |
| Vacancy rate | 24.15 |
| White | 4989 |
| Black | 4283 |
| Asian | 1 |
| Native | 0 |
| Hispanic/Latino | 21 |
| Bachelor's or higher | 1899 |

## Districts

- [MS-02](/us/states/ms/districts/02.md) — 100% (congressional)
- [MS Senate District 14](/us/states/ms/districts/senate/14.md) — 55% (state senate)
- [MS Senate District 15](/us/states/ms/districts/senate/15.md) — 45% (state senate)
- [MS House District 46](/us/states/ms/districts/house/46.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
