---
type: Jurisdiction
title: "Jackson County, KS"
classification: county
fips: "20085"
state: "KS"
demographics:
  population: 13341
  population_under_18: 3312
  population_18_64: 7399
  population_65_plus: 2630
  median_household_income: 75215
  poverty_rate: 6.08
  homeownership_rate: 77.1
  unemployment_rate: 1.79
  median_home_value: 207300
  gini_index: 0.3883
  vacancy_rate: 11.09
  race_white: 11018
  race_black: 98
  race_asian: 64
  race_native: 731
  hispanic: 768
  bachelors_plus: 2761
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 0.8733
  - to: "us/states/ks/districts/02"
    rel: in-district
    area_weight: 0.1267
  - to: "us/states/ks/districts/senate/1"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/house/61"
    rel: in-district
    area_weight: 0.423
  - to: "us/states/ks/districts/house/62"
    rel: in-district
    area_weight: 0.4179
  - to: "us/states/ks/districts/house/47"
    rel: in-district
    area_weight: 0.1591
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Jackson County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13341 |
| Under 18 | 3312 |
| 18–64 | 7399 |
| 65+ | 2630 |
| Median household income | 75215 |
| Poverty rate | 6.08 |
| Homeownership rate | 77.1 |
| Unemployment rate | 1.79 |
| Median home value | 207300 |
| Gini index | 0.3883 |
| Vacancy rate | 11.09 |
| White | 11018 |
| Black | 98 |
| Asian | 64 |
| Native | 731 |
| Hispanic/Latino | 768 |
| Bachelor's or higher | 2761 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 87% (congressional)
- [KS-02](/us/states/ks/districts/02.md) — 13% (congressional)
- [KS Senate District 1](/us/states/ks/districts/senate/1.md) — 100% (state senate)
- [KS House District 61](/us/states/ks/districts/house/61.md) — 42% (state house)
- [KS House District 62](/us/states/ks/districts/house/62.md) — 42% (state house)
- [KS House District 47](/us/states/ks/districts/house/47.md) — 16% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
