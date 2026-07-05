---
type: Jurisdiction
title: "Crook County, WY"
classification: county
fips: "56011"
state: "WY"
demographics:
  population: 7455
  population_under_18: 1833
  population_18_64: 3917
  population_65_plus: 1705
  median_household_income: 79637
  poverty_rate: 6.01
  homeownership_rate: 78.05
  unemployment_rate: 0.57
  median_home_value: 285800
  gini_index: 0.3653
  vacancy_rate: 21.11
  race_white: 6940
  race_black: 0
  race_asian: 15
  race_native: 13
  hispanic: 158
  bachelors_plus: 1505
districts:
  - to: "us/states/wy/districts/00"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wy/districts/senate/1"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wy/districts/house/1"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wy]
timestamp: "2026-07-03"
---

# Crook County, WY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7455 |
| Under 18 | 1833 |
| 18–64 | 3917 |
| 65+ | 1705 |
| Median household income | 79637 |
| Poverty rate | 6.01 |
| Homeownership rate | 78.05 |
| Unemployment rate | 0.57 |
| Median home value | 285800 |
| Gini index | 0.3653 |
| Vacancy rate | 21.11 |
| White | 6940 |
| Black | 0 |
| Asian | 15 |
| Native | 13 |
| Hispanic/Latino | 158 |
| Bachelor's or higher | 1505 |

## Districts

- [WY-00](/us/states/wy/districts/00.md) — 100% (congressional)
- [WY Senate District 1](/us/states/wy/districts/senate/1.md) — 100% (state senate)
- [WY House District 1](/us/states/wy/districts/house/1.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
