---
type: Jurisdiction
title: "Luce County, MI"
classification: county
fips: "26095"
state: "MI"
demographics:
  population: 6271
  population_under_18: 1021
  population_18_64: 3832
  population_65_plus: 1418
  median_household_income: 54893
  poverty_rate: 16.67
  homeownership_rate: 82.57
  unemployment_rate: 9.92
  median_home_value: 112000
  gini_index: 0.4046
  vacancy_rate: 39.64
  race_white: 4821
  race_black: 516
  race_asian: 8
  race_native: 433
  hispanic: 124
  bachelors_plus: 1198
districts:
  - to: "us/states/mi/districts/01"
    rel: in-district
    area_weight: 0.4824
  - to: "us/states/mi/districts/senate/38"
    rel: in-district
    area_weight: 0.4824
  - to: "us/states/mi/districts/house/108"
    rel: in-district
    area_weight: 0.4824
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Luce County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6271 |
| Under 18 | 1021 |
| 18–64 | 3832 |
| 65+ | 1418 |
| Median household income | 54893 |
| Poverty rate | 16.67 |
| Homeownership rate | 82.57 |
| Unemployment rate | 9.92 |
| Median home value | 112000 |
| Gini index | 0.4046 |
| Vacancy rate | 39.64 |
| White | 4821 |
| Black | 516 |
| Asian | 8 |
| Native | 433 |
| Hispanic/Latino | 124 |
| Bachelor's or higher | 1198 |

## Districts

- [MI-01](/us/states/mi/districts/01.md) — 48% (congressional)
- [MI Senate District 38](/us/states/mi/districts/senate/38.md) — 48% (state senate)
- [MI House District 108](/us/states/mi/districts/house/108.md) — 48% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
