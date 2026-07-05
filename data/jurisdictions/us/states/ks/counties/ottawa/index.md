---
type: Jurisdiction
title: "Ottawa County, KS"
classification: county
fips: "20143"
state: "KS"
demographics:
  population: 5819
  population_under_18: 1369
  population_18_64: 3229
  population_65_plus: 1221
  median_household_income: 74018
  poverty_rate: 10.41
  homeownership_rate: 77.16
  unemployment_rate: 2.87
  median_home_value: 166000
  gini_index: 0.4207
  vacancy_rate: 10.58
  race_white: 5442
  race_black: 23
  race_asian: 3
  race_native: 30
  hispanic: 194
  bachelors_plus: 1393
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/36"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/house/107"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Ottawa County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5819 |
| Under 18 | 1369 |
| 18–64 | 3229 |
| 65+ | 1221 |
| Median household income | 74018 |
| Poverty rate | 10.41 |
| Homeownership rate | 77.16 |
| Unemployment rate | 2.87 |
| Median home value | 166000 |
| Gini index | 0.4207 |
| Vacancy rate | 10.58 |
| White | 5442 |
| Black | 23 |
| Asian | 3 |
| Native | 30 |
| Hispanic/Latino | 194 |
| Bachelor's or higher | 1393 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 36](/us/states/ks/districts/senate/36.md) — 100% (state senate)
- [KS House District 107](/us/states/ks/districts/house/107.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
