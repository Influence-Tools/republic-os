---
type: Jurisdiction
title: "St. Helena Parish, LA"
classification: county
fips: "22091"
state: "LA"
demographics:
  population: 10858
  population_under_18: 2217
  population_18_64: 6314
  population_65_plus: 2327
  median_household_income: 41934
  poverty_rate: 32.43
  homeownership_rate: 78.95
  unemployment_rate: 17.59
  median_home_value: 77300
  gini_index: 0.4991
  vacancy_rate: 22.02
  race_white: 4852
  race_black: 5501
  race_asian: 39
  race_native: 70
  hispanic: 94
  bachelors_plus: 1140
districts:
  - to: "us/states/la/districts/05"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/la/districts/senate/6"
    rel: in-district
    area_weight: 0.7619
  - to: "us/states/la/districts/senate/17"
    rel: in-district
    area_weight: 0.2378
  - to: "us/states/la/districts/house/72"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# St. Helena Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10858 |
| Under 18 | 2217 |
| 18–64 | 6314 |
| 65+ | 2327 |
| Median household income | 41934 |
| Poverty rate | 32.43 |
| Homeownership rate | 78.95 |
| Unemployment rate | 17.59 |
| Median home value | 77300 |
| Gini index | 0.4991 |
| Vacancy rate | 22.02 |
| White | 4852 |
| Black | 5501 |
| Asian | 39 |
| Native | 70 |
| Hispanic/Latino | 94 |
| Bachelor's or higher | 1140 |

## Districts

- [LA-05](/us/states/la/districts/05.md) — 100% (congressional)
- [LA Senate District 6](/us/states/la/districts/senate/6.md) — 76% (state senate)
- [LA Senate District 17](/us/states/la/districts/senate/17.md) — 24% (state senate)
- [LA House District 72](/us/states/la/districts/house/72.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
