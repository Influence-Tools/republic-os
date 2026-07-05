---
type: Jurisdiction
title: "Hancock County, GA"
classification: county
fips: "13141"
state: "GA"
demographics:
  population: 8650
  population_under_18: 1188
  population_18_64: 5282
  population_65_plus: 2180
  median_household_income: 40082
  poverty_rate: 30.64
  homeownership_rate: 79.26
  unemployment_rate: 6.32
  median_home_value: 88600
  gini_index: 0.4944
  vacancy_rate: 41.22
  race_white: 2364
  race_black: 6026
  race_asian: 54
  race_native: 33
  hispanic: 59
  bachelors_plus: 917
districts:
  - to: "us/states/ga/districts/10"
    rel: in-district
    area_weight: 0.9958
  - to: "us/states/ga/districts/senate/26"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ga/districts/house/128"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Hancock County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8650 |
| Under 18 | 1188 |
| 18–64 | 5282 |
| 65+ | 2180 |
| Median household income | 40082 |
| Poverty rate | 30.64 |
| Homeownership rate | 79.26 |
| Unemployment rate | 6.32 |
| Median home value | 88600 |
| Gini index | 0.4944 |
| Vacancy rate | 41.22 |
| White | 2364 |
| Black | 6026 |
| Asian | 54 |
| Native | 33 |
| Hispanic/Latino | 59 |
| Bachelor's or higher | 917 |

## Districts

- [GA-10](/us/states/ga/districts/10.md) — 100% (congressional)
- [GA Senate District 26](/us/states/ga/districts/senate/26.md) — 100% (state senate)
- [GA House District 128](/us/states/ga/districts/house/128.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
