---
type: Jurisdiction
title: "Sawyer County, WI"
classification: county
fips: "55113"
state: "WI"
demographics:
  population: 18476
  population_under_18: 3207
  population_18_64: 9998
  population_65_plus: 5271
  median_household_income: 60801
  poverty_rate: 15.61
  homeownership_rate: 76.72
  unemployment_rate: 5.97
  median_home_value: 236200
  gini_index: 0.459
  vacancy_rate: 45.78
  race_white: 14349
  race_black: 118
  race_asian: 109
  race_native: 2433
  hispanic: 450
  bachelors_plus: 5299
districts:
  - to: "us/states/wi/districts/07"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wi/districts/senate/25"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wi/districts/house/74"
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

# Sawyer County, WI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18476 |
| Under 18 | 3207 |
| 18–64 | 9998 |
| 65+ | 5271 |
| Median household income | 60801 |
| Poverty rate | 15.61 |
| Homeownership rate | 76.72 |
| Unemployment rate | 5.97 |
| Median home value | 236200 |
| Gini index | 0.459 |
| Vacancy rate | 45.78 |
| White | 14349 |
| Black | 118 |
| Asian | 109 |
| Native | 2433 |
| Hispanic/Latino | 450 |
| Bachelor's or higher | 5299 |

## Districts

- [WI-07](/us/states/wi/districts/07.md) — 100% (congressional)
- [WI Senate District 25](/us/states/wi/districts/senate/25.md) — 100% (state senate)
- [WI House District 74](/us/states/wi/districts/house/74.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
