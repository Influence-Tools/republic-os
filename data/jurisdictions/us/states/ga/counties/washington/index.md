---
type: Jurisdiction
title: "Washington County, GA"
classification: county
fips: "13303"
state: "GA"
demographics:
  population: 19849
  population_under_18: 4245
  population_18_64: 11977
  population_65_plus: 3627
  median_household_income: 46023
  poverty_rate: 17.17
  homeownership_rate: 64.5
  unemployment_rate: 8.0
  median_home_value: 112500
  gini_index: 0.4663
  vacancy_rate: 16.41
  race_white: 8370
  race_black: 10553
  race_asian: 107
  race_native: 15
  hispanic: 428
  bachelors_plus: 3033
districts:
  - to: "us/states/ga/districts/12"
    rel: in-district
    area_weight: 0.9968
  - to: "us/states/ga/districts/senate/26"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ga/districts/house/128"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Washington County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19849 |
| Under 18 | 4245 |
| 18–64 | 11977 |
| 65+ | 3627 |
| Median household income | 46023 |
| Poverty rate | 17.17 |
| Homeownership rate | 64.5 |
| Unemployment rate | 8.0 |
| Median home value | 112500 |
| Gini index | 0.4663 |
| Vacancy rate | 16.41 |
| White | 8370 |
| Black | 10553 |
| Asian | 107 |
| Native | 15 |
| Hispanic/Latino | 428 |
| Bachelor's or higher | 3033 |

## Districts

- [GA-12](/us/states/ga/districts/12.md) — 100% (congressional)
- [GA Senate District 26](/us/states/ga/districts/senate/26.md) — 100% (state senate)
- [GA House District 128](/us/states/ga/districts/house/128.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
