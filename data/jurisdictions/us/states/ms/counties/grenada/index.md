---
type: Jurisdiction
title: "Grenada County, MS"
classification: county
fips: "28043"
state: "MS"
demographics:
  population: 21217
  population_under_18: 5133
  population_18_64: 12095
  population_65_plus: 3989
  median_household_income: 48804
  poverty_rate: 24.61
  homeownership_rate: 66.59
  unemployment_rate: 4.92
  median_home_value: 132200
  gini_index: 0.5
  vacancy_rate: 18.96
  race_white: 10678
  race_black: 9489
  race_asian: 0
  race_native: 8
  hispanic: 102
  bachelors_plus: 4397
districts:
  - to: "us/states/ms/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ms/districts/senate/14"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ms/districts/house/34"
    rel: in-district
    area_weight: 0.7928
  - to: "us/states/ms/districts/house/30"
    rel: in-district
    area_weight: 0.1885
  - to: "us/states/ms/districts/house/46"
    rel: in-district
    area_weight: 0.0187
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Grenada County, MS

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21217 |
| Under 18 | 5133 |
| 18–64 | 12095 |
| 65+ | 3989 |
| Median household income | 48804 |
| Poverty rate | 24.61 |
| Homeownership rate | 66.59 |
| Unemployment rate | 4.92 |
| Median home value | 132200 |
| Gini index | 0.5 |
| Vacancy rate | 18.96 |
| White | 10678 |
| Black | 9489 |
| Asian | 0 |
| Native | 8 |
| Hispanic/Latino | 102 |
| Bachelor's or higher | 4397 |

## Districts

- [MS-02](/us/states/ms/districts/02.md) — 100% (congressional)
- [MS Senate District 14](/us/states/ms/districts/senate/14.md) — 100% (state senate)
- [MS House District 34](/us/states/ms/districts/house/34.md) — 79% (state house)
- [MS House District 30](/us/states/ms/districts/house/30.md) — 19% (state house)
- [MS House District 46](/us/states/ms/districts/house/46.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
