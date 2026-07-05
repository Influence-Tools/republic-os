---
type: Jurisdiction
title: "Phillips County, AR"
classification: county
fips: "05107"
state: "AR"
demographics:
  population: 15450
  population_under_18: 4054
  population_18_64: 8196
  population_65_plus: 3200
  median_household_income: 40134
  poverty_rate: 29.35
  homeownership_rate: 51.19
  unemployment_rate: 14.51
  median_home_value: 78200
  gini_index: 0.4915
  vacancy_rate: 27.91
  race_white: 5232
  race_black: 9349
  race_asian: 167
  race_native: 4
  hispanic: 320
  bachelors_plus: 2092
districts:
  - to: "us/states/ar/districts/01"
    rel: in-district
    area_weight: 0.9981
  - to: "us/states/ar/districts/senate/9"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/ar/districts/house/62"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Phillips County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15450 |
| Under 18 | 4054 |
| 18–64 | 8196 |
| 65+ | 3200 |
| Median household income | 40134 |
| Poverty rate | 29.35 |
| Homeownership rate | 51.19 |
| Unemployment rate | 14.51 |
| Median home value | 78200 |
| Gini index | 0.4915 |
| Vacancy rate | 27.91 |
| White | 5232 |
| Black | 9349 |
| Asian | 167 |
| Native | 4 |
| Hispanic/Latino | 320 |
| Bachelor's or higher | 2092 |

## Districts

- [AR-01](/us/states/ar/districts/01.md) — 100% (congressional)
- [AR Senate District 9](/us/states/ar/districts/senate/9.md) — 100% (state senate)
- [AR House District 62](/us/states/ar/districts/house/62.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
