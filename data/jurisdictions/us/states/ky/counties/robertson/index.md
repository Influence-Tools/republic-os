---
type: Jurisdiction
title: "Robertson County, KY"
classification: county
fips: "21201"
state: "KY"
demographics:
  population: 2283
  population_under_18: 607
  population_18_64: 1297
  population_65_plus: 379
  median_household_income: 51830
  poverty_rate: 21.12
  homeownership_rate: 79.51
  unemployment_rate: 3.84
  median_home_value: 165100
  gini_index: 0.487
  vacancy_rate: 19.24
  race_white: 2108
  race_black: 82
  race_asian: 0
  race_native: 4
  hispanic: 18
  bachelors_plus: 307
districts:
  - to: "us/states/ky/districts/04"
    rel: in-district
    area_weight: 0.9978
  - to: "us/states/ky/districts/senate/27"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ky/districts/house/70"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Robertson County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2283 |
| Under 18 | 607 |
| 18–64 | 1297 |
| 65+ | 379 |
| Median household income | 51830 |
| Poverty rate | 21.12 |
| Homeownership rate | 79.51 |
| Unemployment rate | 3.84 |
| Median home value | 165100 |
| Gini index | 0.487 |
| Vacancy rate | 19.24 |
| White | 2108 |
| Black | 82 |
| Asian | 0 |
| Native | 4 |
| Hispanic/Latino | 18 |
| Bachelor's or higher | 307 |

## Districts

- [KY-04](/us/states/ky/districts/04.md) — 100% (congressional)
- [KY Senate District 27](/us/states/ky/districts/senate/27.md) — 100% (state senate)
- [KY House District 70](/us/states/ky/districts/house/70.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
