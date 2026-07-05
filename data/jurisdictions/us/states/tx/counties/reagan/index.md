---
type: Jurisdiction
title: "Reagan County, TX"
classification: county
fips: "48383"
state: "TX"
demographics:
  population: 3232
  population_under_18: 1085
  population_18_64: 1815
  population_65_plus: 332
  median_household_income: 57813
  poverty_rate: 11.79
  homeownership_rate: 69.99
  unemployment_rate: 4.97
  median_home_value: 171500
  gini_index: 0.4489
  vacancy_rate: 22.68
  race_white: 1235
  race_black: 188
  race_asian: 46
  race_native: 35
  hispanic: 2220
  bachelors_plus: 339
districts:
  - to: "us/states/tx/districts/23"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/72"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Reagan County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3232 |
| Under 18 | 1085 |
| 18–64 | 1815 |
| 65+ | 332 |
| Median household income | 57813 |
| Poverty rate | 11.79 |
| Homeownership rate | 69.99 |
| Unemployment rate | 4.97 |
| Median home value | 171500 |
| Gini index | 0.4489 |
| Vacancy rate | 22.68 |
| White | 1235 |
| Black | 188 |
| Asian | 46 |
| Native | 35 |
| Hispanic/Latino | 2220 |
| Bachelor's or higher | 339 |

## Districts

- [TX-23](/us/states/tx/districts/23.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 72](/us/states/tx/districts/house/72.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
