---
type: Jurisdiction
title: "Hardin County, IL"
classification: county
fips: "17069"
state: "IL"
demographics:
  population: 3605
  population_under_18: 533
  population_18_64: 1996
  population_65_plus: 1076
  median_household_income: 54271
  poverty_rate: 10.96
  homeownership_rate: 79.55
  unemployment_rate: 2.76
  median_home_value: 103800
  gini_index: 0.4061
  vacancy_rate: 33.89
  race_white: 3477
  race_black: 49
  race_asian: 0
  race_native: 0
  hispanic: 33
  bachelors_plus: 537
districts:
  - to: "us/states/il/districts/12"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/il/districts/house/117"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Hardin County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3605 |
| Under 18 | 533 |
| 18–64 | 1996 |
| 65+ | 1076 |
| Median household income | 54271 |
| Poverty rate | 10.96 |
| Homeownership rate | 79.55 |
| Unemployment rate | 2.76 |
| Median home value | 103800 |
| Gini index | 0.4061 |
| Vacancy rate | 33.89 |
| White | 3477 |
| Black | 49 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 33 |
| Bachelor's or higher | 537 |

## Districts

- [IL-12](/us/states/il/districts/12.md) — 100% (congressional)
- [IL House District 117](/us/states/il/districts/house/117.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
