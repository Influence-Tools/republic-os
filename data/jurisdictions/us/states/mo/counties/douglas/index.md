---
type: Jurisdiction
title: "Douglas County, MO"
classification: county
fips: "29067"
state: "MO"
demographics:
  population: 11965
  population_under_18: 2768
  population_18_64: 6220
  population_65_plus: 2977
  median_household_income: 45985
  poverty_rate: 17.55
  homeownership_rate: 80.6
  unemployment_rate: 6.08
  median_home_value: 168200
  gini_index: 0.5047
  vacancy_rate: 13.67
  race_white: 11051
  race_black: 108
  race_asian: 16
  race_native: 90
  hispanic: 280
  bachelors_plus: 1689
districts:
  - to: "us/states/mo/districts/08"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/senate/33"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/155"
    rel: in-district
    area_weight: 0.7018
  - to: "us/states/mo/districts/house/141"
    rel: in-district
    area_weight: 0.2981
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Douglas County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11965 |
| Under 18 | 2768 |
| 18–64 | 6220 |
| 65+ | 2977 |
| Median household income | 45985 |
| Poverty rate | 17.55 |
| Homeownership rate | 80.6 |
| Unemployment rate | 6.08 |
| Median home value | 168200 |
| Gini index | 0.5047 |
| Vacancy rate | 13.67 |
| White | 11051 |
| Black | 108 |
| Asian | 16 |
| Native | 90 |
| Hispanic/Latino | 280 |
| Bachelor's or higher | 1689 |

## Districts

- [MO-08](/us/states/mo/districts/08.md) — 100% (congressional)
- [MO Senate District 33](/us/states/mo/districts/senate/33.md) — 100% (state senate)
- [MO House District 155](/us/states/mo/districts/house/155.md) — 70% (state house)
- [MO House District 141](/us/states/mo/districts/house/141.md) — 30% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
