---
type: Jurisdiction
title: "Butler County, KY"
classification: county
fips: "21031"
state: "KY"
demographics:
  population: 12393
  population_under_18: 2867
  population_18_64: 7120
  population_65_plus: 2406
  median_household_income: 56092
  poverty_rate: 20.52
  homeownership_rate: 73.72
  unemployment_rate: 4.36
  median_home_value: 111100
  gini_index: 0.4207
  vacancy_rate: 16.28
  race_white: 11481
  race_black: 2
  race_asian: 31
  race_native: 0
  hispanic: 656
  bachelors_plus: 1258
districts:
  - to: "us/states/ky/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ky/districts/senate/5"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ky/districts/house/15"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Butler County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12393 |
| Under 18 | 2867 |
| 18–64 | 7120 |
| 65+ | 2406 |
| Median household income | 56092 |
| Poverty rate | 20.52 |
| Homeownership rate | 73.72 |
| Unemployment rate | 4.36 |
| Median home value | 111100 |
| Gini index | 0.4207 |
| Vacancy rate | 16.28 |
| White | 11481 |
| Black | 2 |
| Asian | 31 |
| Native | 0 |
| Hispanic/Latino | 656 |
| Bachelor's or higher | 1258 |

## Districts

- [KY-02](/us/states/ky/districts/02.md) — 100% (congressional)
- [KY Senate District 5](/us/states/ky/districts/senate/5.md) — 100% (state senate)
- [KY House District 15](/us/states/ky/districts/house/15.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
