---
type: Jurisdiction
title: "Long County, GA"
classification: county
fips: "13183"
state: "GA"
demographics:
  population: 18374
  population_under_18: 5072
  population_18_64: 11502
  population_65_plus: 1800
  median_household_income: 68808
  poverty_rate: 17.35
  homeownership_rate: 65.19
  unemployment_rate: 6.8
  median_home_value: 218300
  gini_index: 0.3717
  vacancy_rate: 10.19
  race_white: 10025
  race_black: 4413
  race_asian: 134
  race_native: 13
  hispanic: 2405
  bachelors_plus: 2063
districts:
  - to: "us/states/ga/districts/01"
    rel: in-district
    area_weight: 0.9976
  - to: "us/states/ga/districts/senate/19"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ga/districts/house/167"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Long County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18374 |
| Under 18 | 5072 |
| 18–64 | 11502 |
| 65+ | 1800 |
| Median household income | 68808 |
| Poverty rate | 17.35 |
| Homeownership rate | 65.19 |
| Unemployment rate | 6.8 |
| Median home value | 218300 |
| Gini index | 0.3717 |
| Vacancy rate | 10.19 |
| White | 10025 |
| Black | 4413 |
| Asian | 134 |
| Native | 13 |
| Hispanic/Latino | 2405 |
| Bachelor's or higher | 2063 |

## Districts

- [GA-01](/us/states/ga/districts/01.md) — 100% (congressional)
- [GA Senate District 19](/us/states/ga/districts/senate/19.md) — 100% (state senate)
- [GA House District 167](/us/states/ga/districts/house/167.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
