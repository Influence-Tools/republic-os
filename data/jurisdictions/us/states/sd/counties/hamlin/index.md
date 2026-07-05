---
type: Jurisdiction
title: "Hamlin County, SD"
classification: county
fips: "46057"
state: "SD"
demographics:
  population: 6373
  population_under_18: 2111
  population_18_64: 3351
  population_65_plus: 911
  median_household_income: 87101
  poverty_rate: 6.86
  homeownership_rate: 82.0
  unemployment_rate: 0.5
  median_home_value: 208600
  gini_index: 0.4183
  vacancy_rate: 23.29
  race_white: 5860
  race_black: 9
  race_asian: 18
  race_native: 23
  hispanic: 375
  bachelors_plus: 1126
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/4"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/house/4"
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

# Hamlin County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6373 |
| Under 18 | 2111 |
| 18–64 | 3351 |
| 65+ | 911 |
| Median household income | 87101 |
| Poverty rate | 6.86 |
| Homeownership rate | 82.0 |
| Unemployment rate | 0.5 |
| Median home value | 208600 |
| Gini index | 0.4183 |
| Vacancy rate | 23.29 |
| White | 5860 |
| Black | 9 |
| Asian | 18 |
| Native | 23 |
| Hispanic/Latino | 375 |
| Bachelor's or higher | 1126 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 4](/us/states/sd/districts/senate/4.md) — 100% (state senate)
- [SD House District 4](/us/states/sd/districts/house/4.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
