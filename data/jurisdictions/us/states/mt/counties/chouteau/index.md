---
type: Jurisdiction
title: "Chouteau County, MT"
classification: county
fips: "30015"
state: "MT"
demographics:
  population: 5906
  population_under_18: 1318
  population_18_64: 3207
  population_65_plus: 1381
  median_household_income: 58218
  poverty_rate: 11.19
  homeownership_rate: 68.18
  unemployment_rate: 3.18
  median_home_value: 207800
  gini_index: 0.4317
  vacancy_rate: 25.16
  race_white: 4550
  race_black: 4
  race_asian: 8
  race_native: 987
  hispanic: 183
  bachelors_plus: 1227
districts:
  - to: "us/states/mt/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mt/districts/senate/13"
    rel: in-district
    area_weight: 0.9827
  - to: "us/states/mt/districts/senate/16"
    rel: in-district
    area_weight: 0.0171
  - to: "us/states/mt/districts/house/26"
    rel: in-district
    area_weight: 0.9827
  - to: "us/states/mt/districts/house/32"
    rel: in-district
    area_weight: 0.0171
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Chouteau County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5906 |
| Under 18 | 1318 |
| 18–64 | 3207 |
| 65+ | 1381 |
| Median household income | 58218 |
| Poverty rate | 11.19 |
| Homeownership rate | 68.18 |
| Unemployment rate | 3.18 |
| Median home value | 207800 |
| Gini index | 0.4317 |
| Vacancy rate | 25.16 |
| White | 4550 |
| Black | 4 |
| Asian | 8 |
| Native | 987 |
| Hispanic/Latino | 183 |
| Bachelor's or higher | 1227 |

## Districts

- [MT-02](/us/states/mt/districts/02.md) — 100% (congressional)
- [MT Senate District 13](/us/states/mt/districts/senate/13.md) — 98% (state senate)
- [MT Senate District 16](/us/states/mt/districts/senate/16.md) — 2% (state senate)
- [MT House District 26](/us/states/mt/districts/house/26.md) — 98% (state house)
- [MT House District 32](/us/states/mt/districts/house/32.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
