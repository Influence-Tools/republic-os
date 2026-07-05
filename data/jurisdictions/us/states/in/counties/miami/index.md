---
type: Jurisdiction
title: "Miami County, IN"
classification: county
fips: "18103"
state: "IN"
demographics:
  population: 35712
  population_under_18: 7430
  population_18_64: 21788
  population_65_plus: 6494
  median_household_income: 61139
  poverty_rate: 15.11
  homeownership_rate: 76.16
  unemployment_rate: 6.56
  median_home_value: 126200
  gini_index: 0.4227
  vacancy_rate: 10.93
  race_white: 31507
  race_black: 1338
  race_asian: 228
  race_native: 98
  hispanic: 1327
  bachelors_plus: 5303
districts:
  - to: "us/states/in/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/in/districts/senate/18"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/in/districts/house/23"
    rel: in-district
    area_weight: 0.9376
  - to: "us/states/in/districts/house/50"
    rel: in-district
    area_weight: 0.0621
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Miami County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 35712 |
| Under 18 | 7430 |
| 18–64 | 21788 |
| 65+ | 6494 |
| Median household income | 61139 |
| Poverty rate | 15.11 |
| Homeownership rate | 76.16 |
| Unemployment rate | 6.56 |
| Median home value | 126200 |
| Gini index | 0.4227 |
| Vacancy rate | 10.93 |
| White | 31507 |
| Black | 1338 |
| Asian | 228 |
| Native | 98 |
| Hispanic/Latino | 1327 |
| Bachelor's or higher | 5303 |

## Districts

- [IN-02](/us/states/in/districts/02.md) — 100% (congressional)
- [IN Senate District 18](/us/states/in/districts/senate/18.md) — 100% (state senate)
- [IN House District 23](/us/states/in/districts/house/23.md) — 94% (state house)
- [IN House District 50](/us/states/in/districts/house/50.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
