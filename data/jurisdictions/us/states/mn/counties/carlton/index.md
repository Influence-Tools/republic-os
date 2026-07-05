---
type: Jurisdiction
title: "Carlton County, MN"
classification: county
fips: "27017"
state: "MN"
demographics:
  population: 36518
  population_under_18: 7866
  population_18_64: 21878
  population_65_plus: 6774
  median_household_income: 80573
  poverty_rate: 11.89
  homeownership_rate: 80.01
  unemployment_rate: 4.77
  median_home_value: 245100
  gini_index: 0.4201
  vacancy_rate: 11.36
  race_white: 31966
  race_black: 789
  race_asian: 196
  race_native: 1220
  hispanic: 711
  bachelors_plus: 9288
districts:
  - to: "us/states/mn/districts/08"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mn/districts/senate/11"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/mn/districts/house/11a"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Carlton County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 36518 |
| Under 18 | 7866 |
| 18–64 | 21878 |
| 65+ | 6774 |
| Median household income | 80573 |
| Poverty rate | 11.89 |
| Homeownership rate | 80.01 |
| Unemployment rate | 4.77 |
| Median home value | 245100 |
| Gini index | 0.4201 |
| Vacancy rate | 11.36 |
| White | 31966 |
| Black | 789 |
| Asian | 196 |
| Native | 1220 |
| Hispanic/Latino | 711 |
| Bachelor's or higher | 9288 |

## Districts

- [MN-08](/us/states/mn/districts/08.md) — 100% (congressional)
- [MN Senate District 11](/us/states/mn/districts/senate/11.md) — 100% (state senate)
- [MN House District 11A](/us/states/mn/districts/house/11a.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
