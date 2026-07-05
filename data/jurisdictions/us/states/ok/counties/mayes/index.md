---
type: Jurisdiction
title: "Mayes County, OK"
classification: county
fips: "40097"
state: "OK"
demographics:
  population: 39604
  population_under_18: 9171
  population_18_64: 22909
  population_65_plus: 7524
  median_household_income: 60305
  poverty_rate: 16.17
  homeownership_rate: 74.4
  unemployment_rate: 6.27
  median_home_value: 188200
  gini_index: 0.4317
  vacancy_rate: 16.73
  race_white: 24901
  race_black: 182
  race_asian: 196
  race_native: 8084
  hispanic: 1536
  bachelors_plus: 6138
districts:
  - to: "us/states/ok/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ok/districts/senate/1"
    rel: in-district
    area_weight: 0.5967
  - to: "us/states/ok/districts/senate/3"
    rel: in-district
    area_weight: 0.4033
  - to: "us/states/ok/districts/house/8"
    rel: in-district
    area_weight: 0.3607
  - to: "us/states/ok/districts/house/5"
    rel: in-district
    area_weight: 0.3311
  - to: "us/states/ok/districts/house/6"
    rel: in-district
    area_weight: 0.183
  - to: "us/states/ok/districts/house/86"
    rel: in-district
    area_weight: 0.1251
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Mayes County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 39604 |
| Under 18 | 9171 |
| 18–64 | 22909 |
| 65+ | 7524 |
| Median household income | 60305 |
| Poverty rate | 16.17 |
| Homeownership rate | 74.4 |
| Unemployment rate | 6.27 |
| Median home value | 188200 |
| Gini index | 0.4317 |
| Vacancy rate | 16.73 |
| White | 24901 |
| Black | 182 |
| Asian | 196 |
| Native | 8084 |
| Hispanic/Latino | 1536 |
| Bachelor's or higher | 6138 |

## Districts

- [OK-02](/us/states/ok/districts/02.md) — 100% (congressional)
- [OK Senate District 1](/us/states/ok/districts/senate/1.md) — 60% (state senate)
- [OK Senate District 3](/us/states/ok/districts/senate/3.md) — 40% (state senate)
- [OK House District 8](/us/states/ok/districts/house/8.md) — 36% (state house)
- [OK House District 5](/us/states/ok/districts/house/5.md) — 33% (state house)
- [OK House District 6](/us/states/ok/districts/house/6.md) — 18% (state house)
- [OK House District 86](/us/states/ok/districts/house/86.md) — 13% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
