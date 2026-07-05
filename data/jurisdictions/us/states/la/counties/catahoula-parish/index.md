---
type: Jurisdiction
title: "Catahoula Parish, LA"
classification: county
fips: "22025"
state: "LA"
demographics:
  population: 8583
  population_under_18: 1899
  population_18_64: 5073
  population_65_plus: 1611
  median_household_income: 50275
  poverty_rate: 24.28
  homeownership_rate: 77.98
  unemployment_rate: 8.92
  median_home_value: 101800
  gini_index: 0.4331
  vacancy_rate: 28.39
  race_white: 5392
  race_black: 2941
  race_asian: 12
  race_native: 13
  hispanic: 50
  bachelors_plus: 1360
districts:
  - to: "us/states/la/districts/05"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/la/districts/senate/32"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/la/districts/house/20"
    rel: in-district
    area_weight: 0.8703
  - to: "us/states/la/districts/house/21"
    rel: in-district
    area_weight: 0.1296
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Catahoula Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8583 |
| Under 18 | 1899 |
| 18–64 | 5073 |
| 65+ | 1611 |
| Median household income | 50275 |
| Poverty rate | 24.28 |
| Homeownership rate | 77.98 |
| Unemployment rate | 8.92 |
| Median home value | 101800 |
| Gini index | 0.4331 |
| Vacancy rate | 28.39 |
| White | 5392 |
| Black | 2941 |
| Asian | 12 |
| Native | 13 |
| Hispanic/Latino | 50 |
| Bachelor's or higher | 1360 |

## Districts

- [LA-05](/us/states/la/districts/05.md) — 100% (congressional)
- [LA Senate District 32](/us/states/la/districts/senate/32.md) — 100% (state senate)
- [LA House District 20](/us/states/la/districts/house/20.md) — 87% (state house)
- [LA House District 21](/us/states/la/districts/house/21.md) — 13% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
