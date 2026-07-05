---
type: Jurisdiction
title: "Sumter County, GA"
classification: county
fips: "13261"
state: "GA"
demographics:
  population: 29061
  population_under_18: 6511
  population_18_64: 17398
  population_65_plus: 5152
  median_household_income: 42653
  poverty_rate: 23.75
  homeownership_rate: 56.62
  unemployment_rate: 4.71
  median_home_value: 120200
  gini_index: 0.497
  vacancy_rate: 18.71
  race_white: 12022
  race_black: 14487
  race_asian: 378
  race_native: 56
  hispanic: 1812
  bachelors_plus: 5812
districts:
  - to: "us/states/ga/districts/02"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ga/districts/house/151"
    rel: in-district
    area_weight: 0.6957
  - to: "us/states/ga/districts/house/150"
    rel: in-district
    area_weight: 0.3041
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Sumter County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 29061 |
| Under 18 | 6511 |
| 18–64 | 17398 |
| 65+ | 5152 |
| Median household income | 42653 |
| Poverty rate | 23.75 |
| Homeownership rate | 56.62 |
| Unemployment rate | 4.71 |
| Median home value | 120200 |
| Gini index | 0.497 |
| Vacancy rate | 18.71 |
| White | 12022 |
| Black | 14487 |
| Asian | 378 |
| Native | 56 |
| Hispanic/Latino | 1812 |
| Bachelor's or higher | 5812 |

## Districts

- [GA-02](/us/states/ga/districts/02.md) — 100% (congressional)
- [GA House District 151](/us/states/ga/districts/house/151.md) — 70% (state house)
- [GA House District 150](/us/states/ga/districts/house/150.md) — 30% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
