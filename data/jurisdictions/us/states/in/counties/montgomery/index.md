---
type: Jurisdiction
title: "Montgomery County, IN"
classification: county
fips: "18107"
state: "IN"
demographics:
  population: 38312
  population_under_18: 8809
  population_18_64: 22281
  population_65_plus: 7222
  median_household_income: 71479
  poverty_rate: 10.53
  homeownership_rate: 80.27
  unemployment_rate: 3.31
  median_home_value: 171800
  gini_index: 0.418
  vacancy_rate: 5.93
  race_white: 34624
  race_black: 372
  race_asian: 209
  race_native: 40
  hispanic: 2367
  bachelors_plus: 7241
districts:
  - to: "us/states/in/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/in/districts/senate/7"
    rel: in-district
    area_weight: 0.6517
  - to: "us/states/in/districts/senate/23"
    rel: in-district
    area_weight: 0.3482
  - to: "us/states/in/districts/house/44"
    rel: in-district
    area_weight: 0.6053
  - to: "us/states/in/districts/house/28"
    rel: in-district
    area_weight: 0.2209
  - to: "us/states/in/districts/house/13"
    rel: in-district
    area_weight: 0.1066
  - to: "us/states/in/districts/house/41"
    rel: in-district
    area_weight: 0.0671
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Montgomery County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 38312 |
| Under 18 | 8809 |
| 18–64 | 22281 |
| 65+ | 7222 |
| Median household income | 71479 |
| Poverty rate | 10.53 |
| Homeownership rate | 80.27 |
| Unemployment rate | 3.31 |
| Median home value | 171800 |
| Gini index | 0.418 |
| Vacancy rate | 5.93 |
| White | 34624 |
| Black | 372 |
| Asian | 209 |
| Native | 40 |
| Hispanic/Latino | 2367 |
| Bachelor's or higher | 7241 |

## Districts

- [IN-04](/us/states/in/districts/04.md) — 100% (congressional)
- [IN Senate District 7](/us/states/in/districts/senate/7.md) — 65% (state senate)
- [IN Senate District 23](/us/states/in/districts/senate/23.md) — 35% (state senate)
- [IN House District 44](/us/states/in/districts/house/44.md) — 61% (state house)
- [IN House District 28](/us/states/in/districts/house/28.md) — 22% (state house)
- [IN House District 13](/us/states/in/districts/house/13.md) — 11% (state house)
- [IN House District 41](/us/states/in/districts/house/41.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
