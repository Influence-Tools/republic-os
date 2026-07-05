---
type: Jurisdiction
title: "Madison Parish, LA"
classification: county
fips: "22065"
state: "LA"
demographics:
  population: 9513
  population_under_18: 2437
  population_18_64: 5412
  population_65_plus: 1664
  median_household_income: 35456
  poverty_rate: 34.52
  homeownership_rate: 53.13
  unemployment_rate: 5.47
  median_home_value: 96200
  gini_index: 0.5151
  vacancy_rate: 30.28
  race_white: 3147
  race_black: 5887
  race_asian: 0
  race_native: 24
  hispanic: 245
  bachelors_plus: 1075
districts:
  - to: "us/states/la/districts/05"
    rel: in-district
    area_weight: 0.9986
  - to: "us/states/la/districts/senate/34"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/la/districts/house/19"
    rel: in-district
    area_weight: 0.6315
  - to: "us/states/la/districts/house/21"
    rel: in-district
    area_weight: 0.3678
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Madison Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9513 |
| Under 18 | 2437 |
| 18–64 | 5412 |
| 65+ | 1664 |
| Median household income | 35456 |
| Poverty rate | 34.52 |
| Homeownership rate | 53.13 |
| Unemployment rate | 5.47 |
| Median home value | 96200 |
| Gini index | 0.5151 |
| Vacancy rate | 30.28 |
| White | 3147 |
| Black | 5887 |
| Asian | 0 |
| Native | 24 |
| Hispanic/Latino | 245 |
| Bachelor's or higher | 1075 |

## Districts

- [LA-05](/us/states/la/districts/05.md) — 100% (congressional)
- [LA Senate District 34](/us/states/la/districts/senate/34.md) — 100% (state senate)
- [LA House District 19](/us/states/la/districts/house/19.md) — 63% (state house)
- [LA House District 21](/us/states/la/districts/house/21.md) — 37% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
