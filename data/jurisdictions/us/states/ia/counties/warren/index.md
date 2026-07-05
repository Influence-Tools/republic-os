---
type: Jurisdiction
title: "Warren County, IA"
classification: county
fips: "19181"
state: "IA"
demographics:
  population: 54409
  population_under_18: 13292
  population_18_64: 32005
  population_65_plus: 9112
  median_household_income: 94588
  poverty_rate: 5.14
  homeownership_rate: 82.34
  unemployment_rate: 3.4
  median_home_value: 269600
  gini_index: 0.394
  vacancy_rate: 5.67
  race_white: 50576
  race_black: 405
  race_asian: 407
  race_native: 154
  hispanic: 2020
  bachelors_plus: 15597
districts:
  - to: "us/states/ia/districts/01"
    rel: in-district
    area_weight: 0.9985
  - to: "us/states/ia/districts/senate/11"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ia/districts/house/22"
    rel: in-district
    area_weight: 0.6161
  - to: "us/states/ia/districts/house/21"
    rel: in-district
    area_weight: 0.3836
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Warren County, IA

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 54409 |
| Under 18 | 13292 |
| 18–64 | 32005 |
| 65+ | 9112 |
| Median household income | 94588 |
| Poverty rate | 5.14 |
| Homeownership rate | 82.34 |
| Unemployment rate | 3.4 |
| Median home value | 269600 |
| Gini index | 0.394 |
| Vacancy rate | 5.67 |
| White | 50576 |
| Black | 405 |
| Asian | 407 |
| Native | 154 |
| Hispanic/Latino | 2020 |
| Bachelor's or higher | 15597 |

## Districts

- [IA-01](/us/states/ia/districts/01.md) — 100% (congressional)
- [IA Senate District 11](/us/states/ia/districts/senate/11.md) — 100% (state senate)
- [IA House District 22](/us/states/ia/districts/house/22.md) — 62% (state house)
- [IA House District 21](/us/states/ia/districts/house/21.md) — 38% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
