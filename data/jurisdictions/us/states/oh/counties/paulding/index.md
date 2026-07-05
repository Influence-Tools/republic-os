---
type: Jurisdiction
title: "Paulding County, OH"
classification: county
fips: "39125"
state: "OH"
demographics:
  population: 18791
  population_under_18: 4437
  population_18_64: 10729
  population_65_plus: 3625
  median_household_income: 67731
  poverty_rate: 8.9
  homeownership_rate: 80.12
  unemployment_rate: 3.62
  median_home_value: 140800
  gini_index: 0.4278
  vacancy_rate: 10.84
  race_white: 17070
  race_black: 34
  race_asian: 100
  race_native: 181
  hispanic: 1091
  bachelors_plus: 2947
districts:
  - to: "us/states/oh/districts/05"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/oh/districts/senate/1"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/oh/districts/house/82"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Paulding County, OH

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18791 |
| Under 18 | 4437 |
| 18–64 | 10729 |
| 65+ | 3625 |
| Median household income | 67731 |
| Poverty rate | 8.9 |
| Homeownership rate | 80.12 |
| Unemployment rate | 3.62 |
| Median home value | 140800 |
| Gini index | 0.4278 |
| Vacancy rate | 10.84 |
| White | 17070 |
| Black | 34 |
| Asian | 100 |
| Native | 181 |
| Hispanic/Latino | 1091 |
| Bachelor's or higher | 2947 |

## Districts

- [OH-05](/us/states/oh/districts/05.md) — 100% (congressional)
- [OH Senate District 1](/us/states/oh/districts/senate/1.md) — 100% (state senate)
- [OH House District 82](/us/states/oh/districts/house/82.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
