---
type: Jurisdiction
title: "Cherokee County, KS"
classification: county
fips: "20021"
state: "KS"
demographics:
  population: 19151
  population_under_18: 4356
  population_18_64: 10918
  population_65_plus: 3877
  median_household_income: 57668
  poverty_rate: 14.11
  homeownership_rate: 75.53
  unemployment_rate: 3.26
  median_home_value: 100100
  gini_index: 0.4229
  vacancy_rate: 13.6
  race_white: 16629
  race_black: 156
  race_asian: 100
  race_native: 388
  hispanic: 566
  bachelors_plus: 3388
districts:
  - to: "us/states/ks/districts/02"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ks/districts/senate/13"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ks/districts/house/1"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Cherokee County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19151 |
| Under 18 | 4356 |
| 18–64 | 10918 |
| 65+ | 3877 |
| Median household income | 57668 |
| Poverty rate | 14.11 |
| Homeownership rate | 75.53 |
| Unemployment rate | 3.26 |
| Median home value | 100100 |
| Gini index | 0.4229 |
| Vacancy rate | 13.6 |
| White | 16629 |
| Black | 156 |
| Asian | 100 |
| Native | 388 |
| Hispanic/Latino | 566 |
| Bachelor's or higher | 3388 |

## Districts

- [KS-02](/us/states/ks/districts/02.md) — 100% (congressional)
- [KS Senate District 13](/us/states/ks/districts/senate/13.md) — 100% (state senate)
- [KS House District 1](/us/states/ks/districts/house/1.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
