---
type: Jurisdiction
title: "Livingston County, MO"
classification: county
fips: "29117"
state: "MO"
demographics:
  population: 14364
  population_under_18: 3107
  population_18_64: 8375
  population_65_plus: 2882
  median_household_income: 63627
  poverty_rate: 11.94
  homeownership_rate: 72.31
  unemployment_rate: 2.74
  median_home_value: 147700
  gini_index: 0.4503
  vacancy_rate: 12.36
  race_white: 13093
  race_black: 434
  race_asian: 52
  race_native: 51
  hispanic: 295
  bachelors_plus: 2432
districts:
  - to: "us/states/mo/districts/06"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/12"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/house/7"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Livingston County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14364 |
| Under 18 | 3107 |
| 18–64 | 8375 |
| 65+ | 2882 |
| Median household income | 63627 |
| Poverty rate | 11.94 |
| Homeownership rate | 72.31 |
| Unemployment rate | 2.74 |
| Median home value | 147700 |
| Gini index | 0.4503 |
| Vacancy rate | 12.36 |
| White | 13093 |
| Black | 434 |
| Asian | 52 |
| Native | 51 |
| Hispanic/Latino | 295 |
| Bachelor's or higher | 2432 |

## Districts

- [MO-06](/us/states/mo/districts/06.md) — 100% (congressional)
- [MO Senate District 12](/us/states/mo/districts/senate/12.md) — 100% (state senate)
- [MO House District 7](/us/states/mo/districts/house/7.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
