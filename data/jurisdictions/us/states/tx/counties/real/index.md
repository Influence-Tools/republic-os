---
type: Jurisdiction
title: "Real County, TX"
classification: county
fips: "48385"
state: "TX"
demographics:
  population: 2802
  population_under_18: 676
  population_18_64: 1064
  population_65_plus: 1062
  median_household_income: 39605
  poverty_rate: 17.87
  homeownership_rate: 78.1
  unemployment_rate: 0.0
  median_home_value: 112500
  gini_index: 0.4929
  vacancy_rate: 42.18
  race_white: 2613
  race_black: 21
  race_asian: 0
  race_native: 0
  hispanic: 530
  bachelors_plus: 500
districts:
  - to: "us/states/tx/districts/21"
    rel: in-district
    area_weight: 0.9981
  - to: "us/states/tx/districts/senate/19"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/53"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Real County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2802 |
| Under 18 | 676 |
| 18–64 | 1064 |
| 65+ | 1062 |
| Median household income | 39605 |
| Poverty rate | 17.87 |
| Homeownership rate | 78.1 |
| Unemployment rate | 0.0 |
| Median home value | 112500 |
| Gini index | 0.4929 |
| Vacancy rate | 42.18 |
| White | 2613 |
| Black | 21 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 530 |
| Bachelor's or higher | 500 |

## Districts

- [TX-21](/us/states/tx/districts/21.md) — 100% (congressional)
- [TX Senate District 19](/us/states/tx/districts/senate/19.md) — 100% (state senate)
- [TX House District 53](/us/states/tx/districts/house/53.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
