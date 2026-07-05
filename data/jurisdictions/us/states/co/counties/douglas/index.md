---
type: Jurisdiction
title: "Douglas County, CO"
classification: county
fips: "08035"
state: "CO"
demographics:
  population: 377150
  population_under_18: 88298
  population_18_64: 236379
  population_65_plus: 52473
  median_household_income: 149594
  poverty_rate: 3.77
  homeownership_rate: 77.39
  unemployment_rate: 3.58
  median_home_value: 713600
  gini_index: 0.406
  vacancy_rate: 3.1
  race_white: 301359
  race_black: 5465
  race_asian: 21889
  race_native: 1653
  hispanic: 38394
  bachelors_plus: 219370
districts:
  - to: "us/states/co/districts/04"
    rel: in-district
    area_weight: 0.9935
  - to: "us/states/co/districts/senate/4"
    rel: in-district
    area_weight: 0.7148
  - to: "us/states/co/districts/senate/30"
    rel: in-district
    area_weight: 0.1434
  - to: "us/states/co/districts/senate/2"
    rel: in-district
    area_weight: 0.1388
  - to: "us/states/co/districts/house/39"
    rel: in-district
    area_weight: 0.8016
  - to: "us/states/co/districts/house/45"
    rel: in-district
    area_weight: 0.0941
  - to: "us/states/co/districts/house/44"
    rel: in-district
    area_weight: 0.0741
  - to: "us/states/co/districts/house/43"
    rel: in-district
    area_weight: 0.0249
  - to: "us/states/co/districts/house/61"
    rel: in-district
    area_weight: 0.0051
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Douglas County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 377150 |
| Under 18 | 88298 |
| 18–64 | 236379 |
| 65+ | 52473 |
| Median household income | 149594 |
| Poverty rate | 3.77 |
| Homeownership rate | 77.39 |
| Unemployment rate | 3.58 |
| Median home value | 713600 |
| Gini index | 0.406 |
| Vacancy rate | 3.1 |
| White | 301359 |
| Black | 5465 |
| Asian | 21889 |
| Native | 1653 |
| Hispanic/Latino | 38394 |
| Bachelor's or higher | 219370 |

## Districts

- [CO-04](/us/states/co/districts/04.md) — 99% (congressional)
- [CO Senate District 4](/us/states/co/districts/senate/4.md) — 71% (state senate)
- [CO Senate District 30](/us/states/co/districts/senate/30.md) — 14% (state senate)
- [CO Senate District 2](/us/states/co/districts/senate/2.md) — 14% (state senate)
- [CO House District 39](/us/states/co/districts/house/39.md) — 80% (state house)
- [CO House District 45](/us/states/co/districts/house/45.md) — 9% (state house)
- [CO House District 44](/us/states/co/districts/house/44.md) — 7% (state house)
- [CO House District 43](/us/states/co/districts/house/43.md) — 2% (state house)
- [CO House District 61](/us/states/co/districts/house/61.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
