---
type: Jurisdiction
title: "Greenwood County, SC"
classification: county
fips: "45047"
state: "SC"
demographics:
  population: 69489
  population_under_18: 15553
  population_18_64: 40476
  population_65_plus: 13460
  median_household_income: 52830
  poverty_rate: 15.08
  homeownership_rate: 67.01
  unemployment_rate: 5.47
  median_home_value: 180500
  gini_index: 0.4706
  vacancy_rate: 12.04
  race_white: 43340
  race_black: 21748
  race_asian: 600
  race_native: 400
  hispanic: 5019
  bachelors_plus: 16029
districts:
  - to: "us/states/sc/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sc/districts/senate/10"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/sc/districts/house/13"
    rel: in-district
    area_weight: 0.7337
  - to: "us/states/sc/districts/house/12"
    rel: in-district
    area_weight: 0.2661
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Greenwood County, SC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 69489 |
| Under 18 | 15553 |
| 18–64 | 40476 |
| 65+ | 13460 |
| Median household income | 52830 |
| Poverty rate | 15.08 |
| Homeownership rate | 67.01 |
| Unemployment rate | 5.47 |
| Median home value | 180500 |
| Gini index | 0.4706 |
| Vacancy rate | 12.04 |
| White | 43340 |
| Black | 21748 |
| Asian | 600 |
| Native | 400 |
| Hispanic/Latino | 5019 |
| Bachelor's or higher | 16029 |

## Districts

- [SC-03](/us/states/sc/districts/03.md) — 100% (congressional)
- [SC Senate District 10](/us/states/sc/districts/senate/10.md) — 100% (state senate)
- [SC House District 13](/us/states/sc/districts/house/13.md) — 73% (state house)
- [SC House District 12](/us/states/sc/districts/house/12.md) — 27% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
