---
type: Jurisdiction
title: "Jackson County, SD"
classification: county
fips: "46071"
state: "SD"
demographics:
  population: 2802
  population_under_18: 923
  population_18_64: 1531
  population_65_plus: 348
  median_household_income: 35417
  poverty_rate: 42.36
  homeownership_rate: 67.35
  unemployment_rate: 7.18
  median_home_value: 117300
  gini_index: 0.5181
  vacancy_rate: 23.57
  race_white: 1026
  race_black: 0
  race_asian: 0
  race_native: 1716
  hispanic: 12
  bachelors_plus: 248
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/27"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/sd/districts/house/27"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Jackson County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2802 |
| Under 18 | 923 |
| 18–64 | 1531 |
| 65+ | 348 |
| Median household income | 35417 |
| Poverty rate | 42.36 |
| Homeownership rate | 67.35 |
| Unemployment rate | 7.18 |
| Median home value | 117300 |
| Gini index | 0.5181 |
| Vacancy rate | 23.57 |
| White | 1026 |
| Black | 0 |
| Asian | 0 |
| Native | 1716 |
| Hispanic/Latino | 12 |
| Bachelor's or higher | 248 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 27](/us/states/sd/districts/senate/27.md) — 100% (state senate)
- [SD House District 27](/us/states/sd/districts/house/27.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
