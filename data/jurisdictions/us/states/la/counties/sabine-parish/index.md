---
type: Jurisdiction
title: "Sabine Parish, LA"
classification: county
fips: "22085"
state: "LA"
demographics:
  population: 21977
  population_under_18: 5088
  population_18_64: 12182
  population_65_plus: 4707
  median_household_income: 50329
  poverty_rate: 23.72
  homeownership_rate: 80.25
  unemployment_rate: 6.59
  median_home_value: 123100
  gini_index: 0.4941
  vacancy_rate: 35.93
  race_white: 14754
  race_black: 3220
  race_asian: 86
  race_native: 1621
  hispanic: 777
  bachelors_plus: 2719
districts:
  - to: "us/states/la/districts/04"
    rel: in-district
    area_weight: 0.9978
  - to: "us/states/la/districts/senate/31"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/la/districts/house/24"
    rel: in-district
    area_weight: 0.5173
  - to: "us/states/la/districts/house/7"
    rel: in-district
    area_weight: 0.4817
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Sabine Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21977 |
| Under 18 | 5088 |
| 18–64 | 12182 |
| 65+ | 4707 |
| Median household income | 50329 |
| Poverty rate | 23.72 |
| Homeownership rate | 80.25 |
| Unemployment rate | 6.59 |
| Median home value | 123100 |
| Gini index | 0.4941 |
| Vacancy rate | 35.93 |
| White | 14754 |
| Black | 3220 |
| Asian | 86 |
| Native | 1621 |
| Hispanic/Latino | 777 |
| Bachelor's or higher | 2719 |

## Districts

- [LA-04](/us/states/la/districts/04.md) — 100% (congressional)
- [LA Senate District 31](/us/states/la/districts/senate/31.md) — 100% (state senate)
- [LA House District 24](/us/states/la/districts/house/24.md) — 52% (state house)
- [LA House District 7](/us/states/la/districts/house/7.md) — 48% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
