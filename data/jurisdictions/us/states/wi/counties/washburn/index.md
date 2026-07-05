---
type: Jurisdiction
title: "Washburn County, WI"
classification: county
fips: "55129"
state: "WI"
demographics:
  population: 16854
  population_under_18: 3035
  population_18_64: 9085
  population_65_plus: 4734
  median_household_income: 63441
  poverty_rate: 11.55
  homeownership_rate: 82.18
  unemployment_rate: 3.92
  median_home_value: 226100
  gini_index: 0.4465
  vacancy_rate: 41.13
  race_white: 15666
  race_black: 45
  race_asian: 78
  race_native: 170
  hispanic: 353
  bachelors_plus: 4238
districts:
  - to: "us/states/wi/districts/07"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wi/districts/senate/25"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wi/districts/house/74"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Washburn County, WI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16854 |
| Under 18 | 3035 |
| 18–64 | 9085 |
| 65+ | 4734 |
| Median household income | 63441 |
| Poverty rate | 11.55 |
| Homeownership rate | 82.18 |
| Unemployment rate | 3.92 |
| Median home value | 226100 |
| Gini index | 0.4465 |
| Vacancy rate | 41.13 |
| White | 15666 |
| Black | 45 |
| Asian | 78 |
| Native | 170 |
| Hispanic/Latino | 353 |
| Bachelor's or higher | 4238 |

## Districts

- [WI-07](/us/states/wi/districts/07.md) — 100% (congressional)
- [WI Senate District 25](/us/states/wi/districts/senate/25.md) — 100% (state senate)
- [WI House District 74](/us/states/wi/districts/house/74.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
