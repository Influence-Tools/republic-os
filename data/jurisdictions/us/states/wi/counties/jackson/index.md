---
type: Jurisdiction
title: "Jackson County, WI"
classification: county
fips: "55053"
state: "WI"
demographics:
  population: 20981
  population_under_18: 4418
  population_18_64: 12271
  population_65_plus: 4292
  median_household_income: 68110
  poverty_rate: 12.36
  homeownership_rate: 80.14
  unemployment_rate: 4.72
  median_home_value: 196100
  gini_index: 0.428
  vacancy_rate: 15.14
  race_white: 18036
  race_black: 448
  race_asian: 103
  race_native: 1000
  hispanic: 781
  bachelors_plus: 3253
districts:
  - to: "us/states/wi/districts/03"
    rel: in-district
    area_weight: 0.6796
  - to: "us/states/wi/districts/07"
    rel: in-district
    area_weight: 0.3204
  - to: "us/states/wi/districts/senate/24"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wi/districts/house/70"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Jackson County, WI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20981 |
| Under 18 | 4418 |
| 18–64 | 12271 |
| 65+ | 4292 |
| Median household income | 68110 |
| Poverty rate | 12.36 |
| Homeownership rate | 80.14 |
| Unemployment rate | 4.72 |
| Median home value | 196100 |
| Gini index | 0.428 |
| Vacancy rate | 15.14 |
| White | 18036 |
| Black | 448 |
| Asian | 103 |
| Native | 1000 |
| Hispanic/Latino | 781 |
| Bachelor's or higher | 3253 |

## Districts

- [WI-03](/us/states/wi/districts/03.md) — 68% (congressional)
- [WI-07](/us/states/wi/districts/07.md) — 32% (congressional)
- [WI Senate District 24](/us/states/wi/districts/senate/24.md) — 100% (state senate)
- [WI House District 70](/us/states/wi/districts/house/70.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
