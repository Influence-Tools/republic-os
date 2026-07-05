---
type: Jurisdiction
title: "Wayne County, MS"
classification: county
fips: "28153"
state: "MS"
demographics:
  population: 19718
  population_under_18: 4916
  population_18_64: 11251
  population_65_plus: 3551
  median_household_income: 37619
  poverty_rate: 22.82
  homeownership_rate: 85.31
  unemployment_rate: 6.98
  median_home_value: 91100
  gini_index: 0.495
  vacancy_rate: 15.99
  race_white: 11143
  race_black: 7465
  race_asian: 117
  race_native: 12
  hispanic: 433
  bachelors_plus: 3240
districts:
  - to: "us/states/ms/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ms/districts/senate/43"
    rel: in-district
    area_weight: 0.9016
  - to: "us/states/ms/districts/senate/42"
    rel: in-district
    area_weight: 0.0983
  - to: "us/states/ms/districts/house/86"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Wayne County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19718 |
| Under 18 | 4916 |
| 18–64 | 11251 |
| 65+ | 3551 |
| Median household income | 37619 |
| Poverty rate | 22.82 |
| Homeownership rate | 85.31 |
| Unemployment rate | 6.98 |
| Median home value | 91100 |
| Gini index | 0.495 |
| Vacancy rate | 15.99 |
| White | 11143 |
| Black | 7465 |
| Asian | 117 |
| Native | 12 |
| Hispanic/Latino | 433 |
| Bachelor's or higher | 3240 |

## Districts

- [MS-04](/us/states/ms/districts/04.md) — 100% (congressional)
- [MS Senate District 43](/us/states/ms/districts/senate/43.md) — 90% (state senate)
- [MS Senate District 42](/us/states/ms/districts/senate/42.md) — 10% (state senate)
- [MS House District 86](/us/states/ms/districts/house/86.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
