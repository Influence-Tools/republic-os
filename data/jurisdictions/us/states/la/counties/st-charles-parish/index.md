---
type: Jurisdiction
title: "St. Charles Parish, LA"
classification: county
fips: "22089"
state: "LA"
demographics:
  population: 51396
  population_under_18: 12384
  population_18_64: 31031
  population_65_plus: 7981
  median_household_income: 80897
  poverty_rate: 11.74
  homeownership_rate: 82.05
  unemployment_rate: 6.75
  median_home_value: 263700
  gini_index: 0.4196
  vacancy_rate: 10.08
  race_white: 32857
  race_black: 11356
  race_asian: 429
  race_native: 486
  hispanic: 4229
  bachelors_plus: 12042
districts:
  - to: "us/states/la/districts/02"
    rel: in-district
    area_weight: 0.7212
  - to: "us/states/la/districts/01"
    rel: in-district
    area_weight: 0.2784
  - to: "us/states/la/districts/senate/19"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/la/districts/house/56"
    rel: in-district
    area_weight: 0.8817
  - to: "us/states/la/districts/house/57"
    rel: in-district
    area_weight: 0.1181
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# St. Charles Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 51396 |
| Under 18 | 12384 |
| 18–64 | 31031 |
| 65+ | 7981 |
| Median household income | 80897 |
| Poverty rate | 11.74 |
| Homeownership rate | 82.05 |
| Unemployment rate | 6.75 |
| Median home value | 263700 |
| Gini index | 0.4196 |
| Vacancy rate | 10.08 |
| White | 32857 |
| Black | 11356 |
| Asian | 429 |
| Native | 486 |
| Hispanic/Latino | 4229 |
| Bachelor's or higher | 12042 |

## Districts

- [LA-02](/us/states/la/districts/02.md) — 72% (congressional)
- [LA-01](/us/states/la/districts/01.md) — 28% (congressional)
- [LA Senate District 19](/us/states/la/districts/senate/19.md) — 100% (state senate)
- [LA House District 56](/us/states/la/districts/house/56.md) — 88% (state house)
- [LA House District 57](/us/states/la/districts/house/57.md) — 12% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
