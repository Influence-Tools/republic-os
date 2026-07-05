---
type: Jurisdiction
title: "Montgomery County, KS"
classification: county
fips: "20125"
state: "KS"
demographics:
  population: 30940
  population_under_18: 7318
  population_18_64: 17339
  population_65_plus: 6283
  median_household_income: 55697
  poverty_rate: 15.92
  homeownership_rate: 72.92
  unemployment_rate: 4.35
  median_home_value: 101700
  gini_index: 0.4224
  vacancy_rate: 17.11
  race_white: 24221
  race_black: 1180
  race_asian: 52
  race_native: 730
  hispanic: 2491
  bachelors_plus: 6453
districts:
  - to: "us/states/ks/districts/02"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ks/districts/senate/15"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/house/11"
    rel: in-district
    area_weight: 0.5559
  - to: "us/states/ks/districts/house/12"
    rel: in-district
    area_weight: 0.444
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Montgomery County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 30940 |
| Under 18 | 7318 |
| 18–64 | 17339 |
| 65+ | 6283 |
| Median household income | 55697 |
| Poverty rate | 15.92 |
| Homeownership rate | 72.92 |
| Unemployment rate | 4.35 |
| Median home value | 101700 |
| Gini index | 0.4224 |
| Vacancy rate | 17.11 |
| White | 24221 |
| Black | 1180 |
| Asian | 52 |
| Native | 730 |
| Hispanic/Latino | 2491 |
| Bachelor's or higher | 6453 |

## Districts

- [KS-02](/us/states/ks/districts/02.md) — 100% (congressional)
- [KS Senate District 15](/us/states/ks/districts/senate/15.md) — 100% (state senate)
- [KS House District 11](/us/states/ks/districts/house/11.md) — 56% (state house)
- [KS House District 12](/us/states/ks/districts/house/12.md) — 44% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
