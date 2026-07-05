---
type: Jurisdiction
title: "Benzie County, MI"
classification: county
fips: "26019"
state: "MI"
demographics:
  population: 18310
  population_under_18: 3094
  population_18_64: 9955
  population_65_plus: 5261
  median_household_income: 74834
  poverty_rate: 9.66
  homeownership_rate: 87.75
  unemployment_rate: 3.09
  median_home_value: 285700
  gini_index: 0.4486
  vacancy_rate: 37.47
  race_white: 16806
  race_black: 124
  race_asian: 161
  race_native: 167
  hispanic: 457
  bachelors_plus: 7152
districts:
  - to: "us/states/mi/districts/01"
    rel: in-district
    area_weight: 0.4037
  - to: "us/states/mi/districts/senate/32"
    rel: in-district
    area_weight: 0.4043
  - to: "us/states/mi/districts/house/104"
    rel: in-district
    area_weight: 0.3199
  - to: "us/states/mi/districts/house/103"
    rel: in-district
    area_weight: 0.0845
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Benzie County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18310 |
| Under 18 | 3094 |
| 18–64 | 9955 |
| 65+ | 5261 |
| Median household income | 74834 |
| Poverty rate | 9.66 |
| Homeownership rate | 87.75 |
| Unemployment rate | 3.09 |
| Median home value | 285700 |
| Gini index | 0.4486 |
| Vacancy rate | 37.47 |
| White | 16806 |
| Black | 124 |
| Asian | 161 |
| Native | 167 |
| Hispanic/Latino | 457 |
| Bachelor's or higher | 7152 |

## Districts

- [MI-01](/us/states/mi/districts/01.md) — 40% (congressional)
- [MI Senate District 32](/us/states/mi/districts/senate/32.md) — 40% (state senate)
- [MI House District 104](/us/states/mi/districts/house/104.md) — 32% (state house)
- [MI House District 103](/us/states/mi/districts/house/103.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
