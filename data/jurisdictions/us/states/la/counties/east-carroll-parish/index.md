---
type: Jurisdiction
title: "East Carroll Parish, LA"
classification: county
fips: "22035"
state: "LA"
demographics:
  population: 7072
  population_under_18: 1332
  population_18_64: 4633
  population_65_plus: 1107
  median_household_income: 33341
  poverty_rate: 35.22
  homeownership_rate: 58.43
  unemployment_rate: 13.9
  median_home_value: 100500
  gini_index: 0.5128
  vacancy_rate: 23.79
  race_white: 2017
  race_black: 4449
  race_asian: 0
  race_native: 58
  hispanic: 163
  bachelors_plus: 693
districts:
  - to: "us/states/la/districts/05"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/la/districts/senate/34"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/la/districts/house/21"
    rel: in-district
    area_weight: 0.6694
  - to: "us/states/la/districts/house/19"
    rel: in-district
    area_weight: 0.33
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# East Carroll Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7072 |
| Under 18 | 1332 |
| 18–64 | 4633 |
| 65+ | 1107 |
| Median household income | 33341 |
| Poverty rate | 35.22 |
| Homeownership rate | 58.43 |
| Unemployment rate | 13.9 |
| Median home value | 100500 |
| Gini index | 0.5128 |
| Vacancy rate | 23.79 |
| White | 2017 |
| Black | 4449 |
| Asian | 0 |
| Native | 58 |
| Hispanic/Latino | 163 |
| Bachelor's or higher | 693 |

## Districts

- [LA-05](/us/states/la/districts/05.md) — 100% (congressional)
- [LA Senate District 34](/us/states/la/districts/senate/34.md) — 100% (state senate)
- [LA House District 21](/us/states/la/districts/house/21.md) — 67% (state house)
- [LA House District 19](/us/states/la/districts/house/19.md) — 33% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
