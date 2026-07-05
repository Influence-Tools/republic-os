---
type: Jurisdiction
title: "Tensas Parish, LA"
classification: county
fips: "22107"
state: "LA"
demographics:
  population: 3935
  population_under_18: 843
  population_18_64: 1986
  population_65_plus: 1106
  median_household_income: 36615
  poverty_rate: 34.43
  homeownership_rate: 74.21
  unemployment_rate: 11.44
  median_home_value: 86300
  gini_index: 0.4616
  vacancy_rate: 43.48
  race_white: 1637
  race_black: 2124
  race_asian: 40
  race_native: 0
  hispanic: 43
  bachelors_plus: 582
districts:
  - to: "us/states/la/districts/05"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/la/districts/senate/34"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/la/districts/house/21"
    rel: in-district
    area_weight: 0.9992
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Tensas Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3935 |
| Under 18 | 843 |
| 18–64 | 1986 |
| 65+ | 1106 |
| Median household income | 36615 |
| Poverty rate | 34.43 |
| Homeownership rate | 74.21 |
| Unemployment rate | 11.44 |
| Median home value | 86300 |
| Gini index | 0.4616 |
| Vacancy rate | 43.48 |
| White | 1637 |
| Black | 2124 |
| Asian | 40 |
| Native | 0 |
| Hispanic/Latino | 43 |
| Bachelor's or higher | 582 |

## Districts

- [LA-05](/us/states/la/districts/05.md) — 100% (congressional)
- [LA Senate District 34](/us/states/la/districts/senate/34.md) — 100% (state senate)
- [LA House District 21](/us/states/la/districts/house/21.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
