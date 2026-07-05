---
type: Jurisdiction
title: "Duchesne County, UT"
classification: county
fips: "49013"
state: "UT"
demographics:
  population: 20185
  population_under_18: 6501
  population_18_64: 11051
  population_65_plus: 2633
  median_household_income: 78445
  poverty_rate: 11.8
  homeownership_rate: 78.92
  unemployment_rate: 4.31
  median_home_value: 283700
  gini_index: 0.4211
  vacancy_rate: 23.81
  race_white: 17567
  race_black: 29
  race_asian: 97
  race_native: 677
  hispanic: 1509
  bachelors_plus: 2932
districts:
  - to: "us/states/ut/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ut/districts/senate/20"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ut/districts/house/67"
    rel: in-district
    area_weight: 0.506
  - to: "us/states/ut/districts/house/68"
    rel: in-district
    area_weight: 0.494
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ut]
timestamp: "2026-07-03"
---

# Duchesne County, UT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20185 |
| Under 18 | 6501 |
| 18–64 | 11051 |
| 65+ | 2633 |
| Median household income | 78445 |
| Poverty rate | 11.8 |
| Homeownership rate | 78.92 |
| Unemployment rate | 4.31 |
| Median home value | 283700 |
| Gini index | 0.4211 |
| Vacancy rate | 23.81 |
| White | 17567 |
| Black | 29 |
| Asian | 97 |
| Native | 677 |
| Hispanic/Latino | 1509 |
| Bachelor's or higher | 2932 |

## Districts

- [UT-03](/us/states/ut/districts/03.md) — 100% (congressional)
- [UT Senate District 20](/us/states/ut/districts/senate/20.md) — 100% (state senate)
- [UT House District 67](/us/states/ut/districts/house/67.md) — 51% (state house)
- [UT House District 68](/us/states/ut/districts/house/68.md) — 49% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
