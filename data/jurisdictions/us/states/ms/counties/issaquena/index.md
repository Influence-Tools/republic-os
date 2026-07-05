---
type: Jurisdiction
title: "Issaquena County, MS"
classification: county
fips: "28055"
state: "MS"
demographics:
  population: 928
  population_under_18: 54
  population_18_64: 647
  population_65_plus: 227
  median_household_income: 31429
  poverty_rate: 16.16
  homeownership_rate: 66.0
  unemployment_rate: 5.1
  median_home_value: 110800
  gini_index: 0.4513
  vacancy_rate: 16.86
  race_white: 315
  race_black: 577
  race_asian: 4
  race_native: 0
  hispanic: 16
  bachelors_plus: 112
districts:
  - to: "us/states/ms/districts/02"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/ms/districts/senate/23"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/ms/districts/house/54"
    rel: in-district
    area_weight: 0.7898
  - to: "us/states/ms/districts/house/50"
    rel: in-district
    area_weight: 0.2094
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Issaquena County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 928 |
| Under 18 | 54 |
| 18–64 | 647 |
| 65+ | 227 |
| Median household income | 31429 |
| Poverty rate | 16.16 |
| Homeownership rate | 66.0 |
| Unemployment rate | 5.1 |
| Median home value | 110800 |
| Gini index | 0.4513 |
| Vacancy rate | 16.86 |
| White | 315 |
| Black | 577 |
| Asian | 4 |
| Native | 0 |
| Hispanic/Latino | 16 |
| Bachelor's or higher | 112 |

## Districts

- [MS-02](/us/states/ms/districts/02.md) — 100% (congressional)
- [MS Senate District 23](/us/states/ms/districts/senate/23.md) — 100% (state senate)
- [MS House District 54](/us/states/ms/districts/house/54.md) — 79% (state house)
- [MS House District 50](/us/states/ms/districts/house/50.md) — 21% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
