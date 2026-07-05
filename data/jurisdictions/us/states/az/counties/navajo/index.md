---
type: Jurisdiction
title: "Navajo County, AZ"
classification: county
fips: "04017"
state: "AZ"
demographics:
  population: 108415
  population_under_18: 27363
  population_18_64: 59229
  population_65_plus: 21823
  median_household_income: 54606
  poverty_rate: 24.72
  homeownership_rate: 73.19
  unemployment_rate: 8.85
  median_home_value: 201500
  gini_index: 0.4563
  vacancy_rate: 30.0
  race_white: 49164
  race_black: 1206
  race_asian: 458
  race_native: 45712
  hispanic: 11786
  bachelors_plus: 19299
districts:
  - to: "us/states/az/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/az/districts/senate/6"
    rel: in-district
    area_weight: 0.7671
  - to: "us/states/az/districts/senate/7"
    rel: in-district
    area_weight: 0.2329
  - to: "us/states/az/districts/house/6"
    rel: in-district
    area_weight: 0.7671
  - to: "us/states/az/districts/house/7"
    rel: in-district
    area_weight: 0.2329
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, az]
timestamp: "2026-07-03"
---

# Navajo County, AZ

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 108415 |
| Under 18 | 27363 |
| 18–64 | 59229 |
| 65+ | 21823 |
| Median household income | 54606 |
| Poverty rate | 24.72 |
| Homeownership rate | 73.19 |
| Unemployment rate | 8.85 |
| Median home value | 201500 |
| Gini index | 0.4563 |
| Vacancy rate | 30.0 |
| White | 49164 |
| Black | 1206 |
| Asian | 458 |
| Native | 45712 |
| Hispanic/Latino | 11786 |
| Bachelor's or higher | 19299 |

## Districts

- [AZ-02](/us/states/az/districts/02.md) — 100% (congressional)
- [AZ Senate District 6](/us/states/az/districts/senate/6.md) — 77% (state senate)
- [AZ Senate District 7](/us/states/az/districts/senate/7.md) — 23% (state senate)
- [AZ House District 6](/us/states/az/districts/house/6.md) — 77% (state house)
- [AZ House District 7](/us/states/az/districts/house/7.md) — 23% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
