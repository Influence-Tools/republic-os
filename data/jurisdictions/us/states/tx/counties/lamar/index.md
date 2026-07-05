---
type: Jurisdiction
title: "Lamar County, TX"
classification: county
fips: "48277"
state: "TX"
demographics:
  population: 50669
  population_under_18: 12194
  population_18_64: 28575
  population_65_plus: 9900
  median_household_income: 61880
  poverty_rate: 18.97
  homeownership_rate: 66.07
  unemployment_rate: 4.04
  median_home_value: 200700
  gini_index: 0.4725
  vacancy_rate: 12.29
  race_white: 38037
  race_black: 6146
  race_asian: 470
  race_native: 368
  hispanic: 4871
  bachelors_plus: 9969
districts:
  - to: "us/states/tx/districts/04"
    rel: in-district
    area_weight: 0.997
  - to: "us/states/tx/districts/senate/1"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/tx/districts/house/1"
    rel: in-district
    area_weight: 0.9992
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Lamar County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 50669 |
| Under 18 | 12194 |
| 18–64 | 28575 |
| 65+ | 9900 |
| Median household income | 61880 |
| Poverty rate | 18.97 |
| Homeownership rate | 66.07 |
| Unemployment rate | 4.04 |
| Median home value | 200700 |
| Gini index | 0.4725 |
| Vacancy rate | 12.29 |
| White | 38037 |
| Black | 6146 |
| Asian | 470 |
| Native | 368 |
| Hispanic/Latino | 4871 |
| Bachelor's or higher | 9969 |

## Districts

- [TX-04](/us/states/tx/districts/04.md) — 100% (congressional)
- [TX Senate District 1](/us/states/tx/districts/senate/1.md) — 100% (state senate)
- [TX House District 1](/us/states/tx/districts/house/1.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
