---
type: Jurisdiction
title: "Denali Borough, AK"
classification: county
fips: "02068"
state: "AK"
demographics:
  population: 1969
  population_under_18: 311
  population_18_64: 1060
  population_65_plus: 598
  median_household_income: 80781
  poverty_rate: 8.26
  homeownership_rate: 64.96
  unemployment_rate: 0.91
  median_home_value: 275000
  gini_index: 0.4297
  vacancy_rate: 56.57
  race_white: 1444
  race_black: 53
  race_asian: 43
  race_native: 57
  hispanic: 160
  bachelors_plus: 541
districts:
  - to: "us/states/ak/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ak/districts/senate/o"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ak/districts/house/30"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ak]
timestamp: "2026-07-03"
---

# Denali Borough, AK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1969 |
| Under 18 | 311 |
| 18–64 | 1060 |
| 65+ | 598 |
| Median household income | 80781 |
| Poverty rate | 8.26 |
| Homeownership rate | 64.96 |
| Unemployment rate | 0.91 |
| Median home value | 275000 |
| Gini index | 0.4297 |
| Vacancy rate | 56.57 |
| White | 1444 |
| Black | 53 |
| Asian | 43 |
| Native | 57 |
| Hispanic/Latino | 160 |
| Bachelor's or higher | 541 |

## Districts

- [AK-00](/us/states/ak/districts/00.md) — 100% (congressional)
- [AK Senate District O](/us/states/ak/districts/senate/o.md) — 100% (state senate)
- [AK House District 30](/us/states/ak/districts/house/30.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
