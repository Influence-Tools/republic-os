---
type: Jurisdiction
title: "Linn County, KS"
classification: county
fips: "20107"
state: "KS"
demographics:
  population: 9767
  population_under_18: 2146
  population_18_64: 5394
  population_65_plus: 2227
  median_household_income: 59069
  poverty_rate: 8.4
  homeownership_rate: 81.14
  unemployment_rate: 4.38
  median_home_value: 173600
  gini_index: 0.4436
  vacancy_rate: 16.74
  race_white: 9136
  race_black: 142
  race_asian: 24
  race_native: 20
  hispanic: 303
  bachelors_plus: 2076
districts:
  - to: "us/states/ks/districts/02"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ks/districts/senate/12"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ks/districts/house/4"
    rel: in-district
    area_weight: 0.8936
  - to: "us/states/ks/districts/house/9"
    rel: in-district
    area_weight: 0.1063
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Linn County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9767 |
| Under 18 | 2146 |
| 18–64 | 5394 |
| 65+ | 2227 |
| Median household income | 59069 |
| Poverty rate | 8.4 |
| Homeownership rate | 81.14 |
| Unemployment rate | 4.38 |
| Median home value | 173600 |
| Gini index | 0.4436 |
| Vacancy rate | 16.74 |
| White | 9136 |
| Black | 142 |
| Asian | 24 |
| Native | 20 |
| Hispanic/Latino | 303 |
| Bachelor's or higher | 2076 |

## Districts

- [KS-02](/us/states/ks/districts/02.md) — 100% (congressional)
- [KS Senate District 12](/us/states/ks/districts/senate/12.md) — 100% (state senate)
- [KS House District 4](/us/states/ks/districts/house/4.md) — 89% (state house)
- [KS House District 9](/us/states/ks/districts/house/9.md) — 11% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
