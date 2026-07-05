---
type: Jurisdiction
title: "Richland County, WI"
classification: county
fips: "55103"
state: "WI"
demographics:
  population: 17205
  population_under_18: 3652
  population_18_64: 9259
  population_65_plus: 4294
  median_household_income: 66420
  poverty_rate: 14.54
  homeownership_rate: 73.86
  unemployment_rate: 3.59
  median_home_value: 197500
  gini_index: 0.4384
  vacancy_rate: 15.03
  race_white: 15947
  race_black: 55
  race_asian: 158
  race_native: 11
  hispanic: 563
  bachelors_plus: 3403
districts:
  - to: "us/states/wi/districts/03"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/wi/districts/senate/14"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wi/districts/house/41"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Richland County, WI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17205 |
| Under 18 | 3652 |
| 18–64 | 9259 |
| 65+ | 4294 |
| Median household income | 66420 |
| Poverty rate | 14.54 |
| Homeownership rate | 73.86 |
| Unemployment rate | 3.59 |
| Median home value | 197500 |
| Gini index | 0.4384 |
| Vacancy rate | 15.03 |
| White | 15947 |
| Black | 55 |
| Asian | 158 |
| Native | 11 |
| Hispanic/Latino | 563 |
| Bachelor's or higher | 3403 |

## Districts

- [WI-03](/us/states/wi/districts/03.md) — 100% (congressional)
- [WI Senate District 14](/us/states/wi/districts/senate/14.md) — 100% (state senate)
- [WI House District 41](/us/states/wi/districts/house/41.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
