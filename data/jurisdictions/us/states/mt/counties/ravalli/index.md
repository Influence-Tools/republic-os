---
type: Jurisdiction
title: "Ravalli County, MT"
classification: county
fips: "30081"
state: "MT"
demographics:
  population: 46727
  population_under_18: 8703
  population_18_64: 25402
  population_65_plus: 12622
  median_household_income: 71283
  poverty_rate: 8.77
  homeownership_rate: 79.37
  unemployment_rate: 3.2
  median_home_value: 476600
  gini_index: 0.4374
  vacancy_rate: 11.89
  race_white: 42013
  race_black: 181
  race_asian: 319
  race_native: 317
  hispanic: 1928
  bachelors_plus: 13979
districts:
  - to: "us/states/mt/districts/01"
    rel: in-district
    area_weight: 0.998
  - to: "us/states/mt/districts/senate/43"
    rel: in-district
    area_weight: 0.7603
  - to: "us/states/mt/districts/senate/44"
    rel: in-district
    area_weight: 0.2391
  - to: "us/states/mt/districts/house/85"
    rel: in-district
    area_weight: 0.7466
  - to: "us/states/mt/districts/house/87"
    rel: in-district
    area_weight: 0.1647
  - to: "us/states/mt/districts/house/88"
    rel: in-district
    area_weight: 0.0744
  - to: "us/states/mt/districts/house/86"
    rel: in-district
    area_weight: 0.0137
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Ravalli County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 46727 |
| Under 18 | 8703 |
| 18–64 | 25402 |
| 65+ | 12622 |
| Median household income | 71283 |
| Poverty rate | 8.77 |
| Homeownership rate | 79.37 |
| Unemployment rate | 3.2 |
| Median home value | 476600 |
| Gini index | 0.4374 |
| Vacancy rate | 11.89 |
| White | 42013 |
| Black | 181 |
| Asian | 319 |
| Native | 317 |
| Hispanic/Latino | 1928 |
| Bachelor's or higher | 13979 |

## Districts

- [MT-01](/us/states/mt/districts/01.md) — 100% (congressional)
- [MT Senate District 43](/us/states/mt/districts/senate/43.md) — 76% (state senate)
- [MT Senate District 44](/us/states/mt/districts/senate/44.md) — 24% (state senate)
- [MT House District 85](/us/states/mt/districts/house/85.md) — 75% (state house)
- [MT House District 87](/us/states/mt/districts/house/87.md) — 16% (state house)
- [MT House District 88](/us/states/mt/districts/house/88.md) — 7% (state house)
- [MT House District 86](/us/states/mt/districts/house/86.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
