---
type: Jurisdiction
title: "Rockcastle County, KY"
classification: county
fips: "21203"
state: "KY"
demographics:
  population: 16163
  population_under_18: 3480
  population_18_64: 9567
  population_65_plus: 3116
  median_household_income: 48862
  poverty_rate: 25.64
  homeownership_rate: 74.33
  unemployment_rate: 4.57
  median_home_value: 123600
  gini_index: 0.4823
  vacancy_rate: 11.6
  race_white: 15473
  race_black: 97
  race_asian: 13
  race_native: 5
  hispanic: 204
  bachelors_plus: 2471
districts:
  - to: "us/states/ky/districts/05"
    rel: in-district
    area_weight: 0.9978
  - to: "us/states/ky/districts/senate/21"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ky/districts/house/71"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Rockcastle County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16163 |
| Under 18 | 3480 |
| 18–64 | 9567 |
| 65+ | 3116 |
| Median household income | 48862 |
| Poverty rate | 25.64 |
| Homeownership rate | 74.33 |
| Unemployment rate | 4.57 |
| Median home value | 123600 |
| Gini index | 0.4823 |
| Vacancy rate | 11.6 |
| White | 15473 |
| Black | 97 |
| Asian | 13 |
| Native | 5 |
| Hispanic/Latino | 204 |
| Bachelor's or higher | 2471 |

## Districts

- [KY-05](/us/states/ky/districts/05.md) — 100% (congressional)
- [KY Senate District 21](/us/states/ky/districts/senate/21.md) — 100% (state senate)
- [KY House District 71](/us/states/ky/districts/house/71.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
