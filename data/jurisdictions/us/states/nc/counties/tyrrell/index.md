---
type: Jurisdiction
title: "Tyrrell County, NC"
classification: county
fips: "37177"
state: "NC"
demographics:
  population: 3423
  population_under_18: 553
  population_18_64: 1815
  population_65_plus: 1055
  median_household_income: 41685
  poverty_rate: 18.71
  homeownership_rate: 77.83
  unemployment_rate: 2.82
  median_home_value: 164500
  gini_index: 0.4225
  vacancy_rate: 30.6
  race_white: 1962
  race_black: 1123
  race_asian: 0
  race_native: 5
  hispanic: 263
  bachelors_plus: 509
districts:
  - to: "us/states/nc/districts/01"
    rel: in-district
    area_weight: 0.6939
  - to: "us/states/nc/districts/senate/1"
    rel: in-district
    area_weight: 0.6851
  - to: "us/states/nc/districts/house/1"
    rel: in-district
    area_weight: 0.6851
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Tyrrell County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3423 |
| Under 18 | 553 |
| 18–64 | 1815 |
| 65+ | 1055 |
| Median household income | 41685 |
| Poverty rate | 18.71 |
| Homeownership rate | 77.83 |
| Unemployment rate | 2.82 |
| Median home value | 164500 |
| Gini index | 0.4225 |
| Vacancy rate | 30.6 |
| White | 1962 |
| Black | 1123 |
| Asian | 0 |
| Native | 5 |
| Hispanic/Latino | 263 |
| Bachelor's or higher | 509 |

## Districts

- [NC-01](/us/states/nc/districts/01.md) — 69% (congressional)
- [NC Senate District 1](/us/states/nc/districts/senate/1.md) — 69% (state senate)
- [NC House District 1](/us/states/nc/districts/house/1.md) — 69% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
