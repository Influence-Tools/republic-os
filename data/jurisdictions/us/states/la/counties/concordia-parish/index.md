---
type: Jurisdiction
title: "Concordia Parish, LA"
classification: county
fips: "22029"
state: "LA"
demographics:
  population: 18174
  population_under_18: 4245
  population_18_64: 10433
  population_65_plus: 3496
  median_household_income: 39943
  poverty_rate: 31.82
  homeownership_rate: 74.23
  unemployment_rate: 11.7
  median_home_value: 103800
  gini_index: 0.5244
  vacancy_rate: 25.02
  race_white: 10091
  race_black: 7104
  race_asian: 38
  race_native: 60
  hispanic: 516
  bachelors_plus: 2842
districts:
  - to: "us/states/la/districts/05"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/la/districts/senate/32"
    rel: in-district
    area_weight: 0.778
  - to: "us/states/la/districts/senate/34"
    rel: in-district
    area_weight: 0.2214
  - to: "us/states/la/districts/house/21"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Concordia Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18174 |
| Under 18 | 4245 |
| 18–64 | 10433 |
| 65+ | 3496 |
| Median household income | 39943 |
| Poverty rate | 31.82 |
| Homeownership rate | 74.23 |
| Unemployment rate | 11.7 |
| Median home value | 103800 |
| Gini index | 0.5244 |
| Vacancy rate | 25.02 |
| White | 10091 |
| Black | 7104 |
| Asian | 38 |
| Native | 60 |
| Hispanic/Latino | 516 |
| Bachelor's or higher | 2842 |

## Districts

- [LA-05](/us/states/la/districts/05.md) — 100% (congressional)
- [LA Senate District 32](/us/states/la/districts/senate/32.md) — 78% (state senate)
- [LA Senate District 34](/us/states/la/districts/senate/34.md) — 22% (state senate)
- [LA House District 21](/us/states/la/districts/house/21.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
