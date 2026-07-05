---
type: Jurisdiction
title: "Newberry County, SC"
classification: county
fips: "45071"
state: "SC"
demographics:
  population: 38435
  population_under_18: 8231
  population_18_64: 22351
  population_65_plus: 7853
  median_household_income: 61780
  poverty_rate: 17.36
  homeownership_rate: 73.1
  unemployment_rate: 4.45
  median_home_value: 173300
  gini_index: 0.4407
  vacancy_rate: 17.42
  race_white: 23731
  race_black: 11088
  race_asian: 182
  race_native: 92
  hispanic: 3551
  bachelors_plus: 8608
districts:
  - to: "us/states/sc/districts/03"
    rel: in-district
    area_weight: 0.9966
  - to: "us/states/sc/districts/senate/18"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/sc/districts/house/40"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Newberry County, SC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 38435 |
| Under 18 | 8231 |
| 18–64 | 22351 |
| 65+ | 7853 |
| Median household income | 61780 |
| Poverty rate | 17.36 |
| Homeownership rate | 73.1 |
| Unemployment rate | 4.45 |
| Median home value | 173300 |
| Gini index | 0.4407 |
| Vacancy rate | 17.42 |
| White | 23731 |
| Black | 11088 |
| Asian | 182 |
| Native | 92 |
| Hispanic/Latino | 3551 |
| Bachelor's or higher | 8608 |

## Districts

- [SC-03](/us/states/sc/districts/03.md) — 100% (congressional)
- [SC Senate District 18](/us/states/sc/districts/senate/18.md) — 100% (state senate)
- [SC House District 40](/us/states/sc/districts/house/40.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
