---
type: Jurisdiction
title: "Beaver County, UT"
classification: county
fips: "49001"
state: "UT"
demographics:
  population: 7273
  population_under_18: 2141
  population_18_64: 4022
  population_65_plus: 1110
  median_household_income: 79360
  poverty_rate: 6.64
  homeownership_rate: 80.98
  unemployment_rate: 1.67
  median_home_value: 283700
  gini_index: 0.3432
  vacancy_rate: 15.19
  race_white: 6465
  race_black: 24
  race_asian: 0
  race_native: 4
  hispanic: 1088
  bachelors_plus: 1304
districts:
  - to: "us/states/ut/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ut/districts/senate/28"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ut/districts/house/70"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ut]
timestamp: "2026-07-03"
---

# Beaver County, UT

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7273 |
| Under 18 | 2141 |
| 18–64 | 4022 |
| 65+ | 1110 |
| Median household income | 79360 |
| Poverty rate | 6.64 |
| Homeownership rate | 80.98 |
| Unemployment rate | 1.67 |
| Median home value | 283700 |
| Gini index | 0.3432 |
| Vacancy rate | 15.19 |
| White | 6465 |
| Black | 24 |
| Asian | 0 |
| Native | 4 |
| Hispanic/Latino | 1088 |
| Bachelor's or higher | 1304 |

## Districts

- [UT-02](/us/states/ut/districts/02.md) — 100% (congressional)
- [UT Senate District 28](/us/states/ut/districts/senate/28.md) — 100% (state senate)
- [UT House District 70](/us/states/ut/districts/house/70.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
