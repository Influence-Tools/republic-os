---
type: Jurisdiction
title: "Montgomery County, KY"
classification: county
fips: "21173"
state: "KY"
demographics:
  population: 28395
  population_under_18: 6593
  population_18_64: 16996
  population_65_plus: 4806
  median_household_income: 56396
  poverty_rate: 15.41
  homeownership_rate: 68.31
  unemployment_rate: 4.0
  median_home_value: 172200
  gini_index: 0.4401
  vacancy_rate: 10.02
  race_white: 26051
  race_black: 382
  race_asian: 151
  race_native: 206
  hispanic: 983
  bachelors_plus: 5703
districts:
  - to: "us/states/ky/districts/06"
    rel: in-district
    area_weight: 0.998
  - to: "us/states/ky/districts/senate/28"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ky/districts/house/74"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Montgomery County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 28395 |
| Under 18 | 6593 |
| 18–64 | 16996 |
| 65+ | 4806 |
| Median household income | 56396 |
| Poverty rate | 15.41 |
| Homeownership rate | 68.31 |
| Unemployment rate | 4.0 |
| Median home value | 172200 |
| Gini index | 0.4401 |
| Vacancy rate | 10.02 |
| White | 26051 |
| Black | 382 |
| Asian | 151 |
| Native | 206 |
| Hispanic/Latino | 983 |
| Bachelor's or higher | 5703 |

## Districts

- [KY-06](/us/states/ky/districts/06.md) — 100% (congressional)
- [KY Senate District 28](/us/states/ky/districts/senate/28.md) — 100% (state senate)
- [KY House District 74](/us/states/ky/districts/house/74.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
