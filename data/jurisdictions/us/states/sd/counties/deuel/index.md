---
type: Jurisdiction
title: "Deuel County, SD"
classification: county
fips: "46039"
state: "SD"
demographics:
  population: 4328
  population_under_18: 1048
  population_18_64: 2324
  population_65_plus: 956
  median_household_income: 83112
  poverty_rate: 8.76
  homeownership_rate: 82.78
  unemployment_rate: 2.13
  median_home_value: 205900
  gini_index: 0.4004
  vacancy_rate: 18.61
  race_white: 4098
  race_black: 22
  race_asian: 4
  race_native: 13
  hispanic: 136
  bachelors_plus: 900
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/sd/districts/senate/4"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/sd/districts/house/4"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Deuel County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4328 |
| Under 18 | 1048 |
| 18–64 | 2324 |
| 65+ | 956 |
| Median household income | 83112 |
| Poverty rate | 8.76 |
| Homeownership rate | 82.78 |
| Unemployment rate | 2.13 |
| Median home value | 205900 |
| Gini index | 0.4004 |
| Vacancy rate | 18.61 |
| White | 4098 |
| Black | 22 |
| Asian | 4 |
| Native | 13 |
| Hispanic/Latino | 136 |
| Bachelor's or higher | 900 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 4](/us/states/sd/districts/senate/4.md) — 100% (state senate)
- [SD House District 4](/us/states/sd/districts/house/4.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
