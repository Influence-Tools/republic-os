---
type: Jurisdiction
title: "Trigg County, KY"
classification: county
fips: "21221"
state: "KY"
demographics:
  population: 14315
  population_under_18: 3128
  population_18_64: 7974
  population_65_plus: 3213
  median_household_income: 59857
  poverty_rate: 20.6
  homeownership_rate: 76.95
  unemployment_rate: 4.17
  median_home_value: 207700
  gini_index: 0.4446
  vacancy_rate: 20.81
  race_white: 12479
  race_black: 604
  race_asian: 23
  race_native: 0
  hispanic: 387
  bachelors_plus: 3305
districts:
  - to: "us/states/ky/districts/01"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ky/districts/senate/1"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/ky/districts/house/5"
    rel: in-district
    area_weight: 0.6008
  - to: "us/states/ky/districts/house/8"
    rel: in-district
    area_weight: 0.3986
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Trigg County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14315 |
| Under 18 | 3128 |
| 18–64 | 7974 |
| 65+ | 3213 |
| Median household income | 59857 |
| Poverty rate | 20.6 |
| Homeownership rate | 76.95 |
| Unemployment rate | 4.17 |
| Median home value | 207700 |
| Gini index | 0.4446 |
| Vacancy rate | 20.81 |
| White | 12479 |
| Black | 604 |
| Asian | 23 |
| Native | 0 |
| Hispanic/Latino | 387 |
| Bachelor's or higher | 3305 |

## Districts

- [KY-01](/us/states/ky/districts/01.md) — 100% (congressional)
- [KY Senate District 1](/us/states/ky/districts/senate/1.md) — 100% (state senate)
- [KY House District 5](/us/states/ky/districts/house/5.md) — 60% (state house)
- [KY House District 8](/us/states/ky/districts/house/8.md) — 40% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
