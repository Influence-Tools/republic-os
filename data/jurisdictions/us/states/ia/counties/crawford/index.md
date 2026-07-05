---
type: Jurisdiction
title: "Crawford County, IA"
classification: county
fips: "19047"
state: "IA"
demographics:
  population: 16277
  population_under_18: 4143
  population_18_64: 9206
  population_65_plus: 2928
  median_household_income: 67027
  poverty_rate: 14.77
  homeownership_rate: 75.98
  unemployment_rate: 3.82
  median_home_value: 153700
  gini_index: 0.4282
  vacancy_rate: 7.83
  race_white: 10805
  race_black: 152
  race_asian: 357
  race_native: 117
  hispanic: 5019
  bachelors_plus: 2325
districts:
  - to: "us/states/ia/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/senate/6"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/house/12"
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

# Crawford County, IA

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16277 |
| Under 18 | 4143 |
| 18–64 | 9206 |
| 65+ | 2928 |
| Median household income | 67027 |
| Poverty rate | 14.77 |
| Homeownership rate | 75.98 |
| Unemployment rate | 3.82 |
| Median home value | 153700 |
| Gini index | 0.4282 |
| Vacancy rate | 7.83 |
| White | 10805 |
| Black | 152 |
| Asian | 357 |
| Native | 117 |
| Hispanic/Latino | 5019 |
| Bachelor's or higher | 2325 |

## Districts

- [IA-04](/us/states/ia/districts/04.md) — 100% (congressional)
- [IA Senate District 6](/us/states/ia/districts/senate/6.md) — 100% (state senate)
- [IA House District 12](/us/states/ia/districts/house/12.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
