---
type: Jurisdiction
title: "Garrard County, KY"
classification: county
fips: "21079"
state: "KY"
demographics:
  population: 17568
  population_under_18: 3791
  population_18_64: 10488
  population_65_plus: 3289
  median_household_income: 63087
  poverty_rate: 15.93
  homeownership_rate: 79.9
  unemployment_rate: 5.15
  median_home_value: 204900
  gini_index: 0.4286
  vacancy_rate: 8.04
  race_white: 16144
  race_black: 415
  race_asian: 9
  race_native: 30
  hispanic: 524
  bachelors_plus: 3347
districts:
  - to: "us/states/ky/districts/06"
    rel: in-district
    area_weight: 0.9948
  - to: "us/states/ky/districts/senate/22"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/ky/districts/house/80"
    rel: in-district
    area_weight: 0.9989
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Garrard County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17568 |
| Under 18 | 3791 |
| 18–64 | 10488 |
| 65+ | 3289 |
| Median household income | 63087 |
| Poverty rate | 15.93 |
| Homeownership rate | 79.9 |
| Unemployment rate | 5.15 |
| Median home value | 204900 |
| Gini index | 0.4286 |
| Vacancy rate | 8.04 |
| White | 16144 |
| Black | 415 |
| Asian | 9 |
| Native | 30 |
| Hispanic/Latino | 524 |
| Bachelor's or higher | 3347 |

## Districts

- [KY-06](/us/states/ky/districts/06.md) — 99% (congressional)
- [KY Senate District 22](/us/states/ky/districts/senate/22.md) — 100% (state senate)
- [KY House District 80](/us/states/ky/districts/house/80.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
