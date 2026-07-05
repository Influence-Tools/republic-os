---
type: Jurisdiction
title: "Edmunds County, SD"
classification: county
fips: "46045"
state: "SD"
demographics:
  population: 4048
  population_under_18: 956
  population_18_64: 2164
  population_65_plus: 928
  median_household_income: 81630
  poverty_rate: 9.93
  homeownership_rate: 81.1
  unemployment_rate: 1.1
  median_home_value: 163300
  gini_index: 0.4699
  vacancy_rate: 14.12
  race_white: 3834
  race_black: 2
  race_asian: 30
  race_native: 20
  hispanic: 108
  bachelors_plus: 982
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/23"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/house/23"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Edmunds County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4048 |
| Under 18 | 956 |
| 18–64 | 2164 |
| 65+ | 928 |
| Median household income | 81630 |
| Poverty rate | 9.93 |
| Homeownership rate | 81.1 |
| Unemployment rate | 1.1 |
| Median home value | 163300 |
| Gini index | 0.4699 |
| Vacancy rate | 14.12 |
| White | 3834 |
| Black | 2 |
| Asian | 30 |
| Native | 20 |
| Hispanic/Latino | 108 |
| Bachelor's or higher | 982 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 23](/us/states/sd/districts/senate/23.md) — 100% (state senate)
- [SD House District 23](/us/states/sd/districts/house/23.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
