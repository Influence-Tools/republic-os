---
type: Jurisdiction
title: "Banks County, GA"
classification: county
fips: "13011"
state: "GA"
demographics:
  population: 19264
  population_under_18: 4117
  population_18_64: 11796
  population_65_plus: 3351
  median_household_income: 77063
  poverty_rate: 11.27
  homeownership_rate: 78.72
  unemployment_rate: 2.91
  median_home_value: 278100
  gini_index: 0.4088
  vacancy_rate: 8.33
  race_white: 16527
  race_black: 524
  race_asian: 367
  race_native: 27
  hispanic: 1409
  bachelors_plus: 3370
districts:
  - to: "us/states/ga/districts/09"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/ga/districts/senate/50"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ga/districts/house/32"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Banks County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19264 |
| Under 18 | 4117 |
| 18–64 | 11796 |
| 65+ | 3351 |
| Median household income | 77063 |
| Poverty rate | 11.27 |
| Homeownership rate | 78.72 |
| Unemployment rate | 2.91 |
| Median home value | 278100 |
| Gini index | 0.4088 |
| Vacancy rate | 8.33 |
| White | 16527 |
| Black | 524 |
| Asian | 367 |
| Native | 27 |
| Hispanic/Latino | 1409 |
| Bachelor's or higher | 3370 |

## Districts

- [GA-09](/us/states/ga/districts/09.md) — 100% (congressional)
- [GA Senate District 50](/us/states/ga/districts/senate/50.md) — 100% (state senate)
- [GA House District 32](/us/states/ga/districts/house/32.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
