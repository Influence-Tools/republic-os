---
type: Jurisdiction
title: "Shiawassee County, MI"
classification: county
fips: "26155"
state: "MI"
demographics:
  population: 67991
  population_under_18: 14070
  population_18_64: 40448
  population_65_plus: 13473
  median_household_income: 67404
  poverty_rate: 12.04
  homeownership_rate: 80.13
  unemployment_rate: 4.0
  median_home_value: 171600
  gini_index: 0.4187
  vacancy_rate: 7.34
  race_white: 63964
  race_black: 294
  race_asian: 304
  race_native: 151
  hispanic: 2144
  bachelors_plus: 12735
districts:
  - to: "us/states/mi/districts/07"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/mi/districts/senate/28"
    rel: in-district
    area_weight: 0.8661
  - to: "us/states/mi/districts/senate/22"
    rel: in-district
    area_weight: 0.1338
  - to: "us/states/mi/districts/house/71"
    rel: in-district
    area_weight: 0.8967
  - to: "us/states/mi/districts/house/75"
    rel: in-district
    area_weight: 0.1033
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Shiawassee County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 67991 |
| Under 18 | 14070 |
| 18–64 | 40448 |
| 65+ | 13473 |
| Median household income | 67404 |
| Poverty rate | 12.04 |
| Homeownership rate | 80.13 |
| Unemployment rate | 4.0 |
| Median home value | 171600 |
| Gini index | 0.4187 |
| Vacancy rate | 7.34 |
| White | 63964 |
| Black | 294 |
| Asian | 304 |
| Native | 151 |
| Hispanic/Latino | 2144 |
| Bachelor's or higher | 12735 |

## Districts

- [MI-07](/us/states/mi/districts/07.md) — 100% (congressional)
- [MI Senate District 28](/us/states/mi/districts/senate/28.md) — 87% (state senate)
- [MI Senate District 22](/us/states/mi/districts/senate/22.md) — 13% (state senate)
- [MI House District 71](/us/states/mi/districts/house/71.md) — 90% (state house)
- [MI House District 75](/us/states/mi/districts/house/75.md) — 10% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
