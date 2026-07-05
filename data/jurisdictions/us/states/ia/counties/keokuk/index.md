---
type: Jurisdiction
title: "Keokuk County, IA"
classification: county
fips: "19107"
state: "IA"
demographics:
  population: 9924
  population_under_18: 2219
  population_18_64: 5472
  population_65_plus: 2233
  median_household_income: 62329
  poverty_rate: 12.13
  homeownership_rate: 81.27
  unemployment_rate: 4.51
  median_home_value: 118700
  gini_index: 0.4409
  vacancy_rate: 12.46
  race_white: 9453
  race_black: 26
  race_asian: 20
  race_native: 9
  hispanic: 233
  bachelors_plus: 1511
districts:
  - to: "us/states/ia/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/senate/44"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/house/88"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Keokuk County, IA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9924 |
| Under 18 | 2219 |
| 18–64 | 5472 |
| 65+ | 2233 |
| Median household income | 62329 |
| Poverty rate | 12.13 |
| Homeownership rate | 81.27 |
| Unemployment rate | 4.51 |
| Median home value | 118700 |
| Gini index | 0.4409 |
| Vacancy rate | 12.46 |
| White | 9453 |
| Black | 26 |
| Asian | 20 |
| Native | 9 |
| Hispanic/Latino | 233 |
| Bachelor's or higher | 1511 |

## Districts

- [IA-01](/us/states/ia/districts/01.md) — 100% (congressional)
- [IA Senate District 44](/us/states/ia/districts/senate/44.md) — 100% (state senate)
- [IA House District 88](/us/states/ia/districts/house/88.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
