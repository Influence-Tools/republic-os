---
type: Jurisdiction
title: "Ottawa County, MI"
classification: county
fips: "26139"
state: "MI"
demographics:
  population: 301203
  population_under_18: 69275
  population_18_64: 181608
  population_65_plus: 50320
  median_household_income: 90502
  poverty_rate: 8.31
  homeownership_rate: 79.27
  unemployment_rate: 3.52
  median_home_value: 323400
  gini_index: 0.4278
  vacancy_rate: 5.34
  race_white: 253027
  race_black: 4821
  race_asian: 8146
  race_native: 1563
  hispanic: 30924
  bachelors_plus: 101277
districts:
  - to: "us/states/mi/districts/03"
    rel: in-district
    area_weight: 0.172
  - to: "us/states/mi/districts/04"
    rel: in-district
    area_weight: 0.1598
  - to: "us/states/mi/districts/02"
    rel: in-district
    area_weight: 0.022
  - to: "us/states/mi/districts/senate/31"
    rel: in-district
    area_weight: 0.2421
  - to: "us/states/mi/districts/senate/30"
    rel: in-district
    area_weight: 0.0895
  - to: "us/states/mi/districts/senate/33"
    rel: in-district
    area_weight: 0.022
  - to: "us/states/mi/districts/house/89"
    rel: in-district
    area_weight: 0.1339
  - to: "us/states/mi/districts/house/88"
    rel: in-district
    area_weight: 0.1165
  - to: "us/states/mi/districts/house/85"
    rel: in-district
    area_weight: 0.0561
  - to: "us/states/mi/districts/house/86"
    rel: in-district
    area_weight: 0.0307
  - to: "us/states/mi/districts/house/43"
    rel: in-district
    area_weight: 0.0166
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Ottawa County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 301203 |
| Under 18 | 69275 |
| 18–64 | 181608 |
| 65+ | 50320 |
| Median household income | 90502 |
| Poverty rate | 8.31 |
| Homeownership rate | 79.27 |
| Unemployment rate | 3.52 |
| Median home value | 323400 |
| Gini index | 0.4278 |
| Vacancy rate | 5.34 |
| White | 253027 |
| Black | 4821 |
| Asian | 8146 |
| Native | 1563 |
| Hispanic/Latino | 30924 |
| Bachelor's or higher | 101277 |

## Districts

- [MI-03](/us/states/mi/districts/03.md) — 17% (congressional)
- [MI-04](/us/states/mi/districts/04.md) — 16% (congressional)
- [MI-02](/us/states/mi/districts/02.md) — 2% (congressional)
- [MI Senate District 31](/us/states/mi/districts/senate/31.md) — 24% (state senate)
- [MI Senate District 30](/us/states/mi/districts/senate/30.md) — 9% (state senate)
- [MI Senate District 33](/us/states/mi/districts/senate/33.md) — 2% (state senate)
- [MI House District 89](/us/states/mi/districts/house/89.md) — 13% (state house)
- [MI House District 88](/us/states/mi/districts/house/88.md) — 12% (state house)
- [MI House District 85](/us/states/mi/districts/house/85.md) — 6% (state house)
- [MI House District 86](/us/states/mi/districts/house/86.md) — 3% (state house)
- [MI House District 43](/us/states/mi/districts/house/43.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
