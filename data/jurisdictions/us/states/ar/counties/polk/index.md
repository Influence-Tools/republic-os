---
type: Jurisdiction
title: "Polk County, AR"
classification: county
fips: "05113"
state: "AR"
demographics:
  population: 19361
  population_under_18: 4360
  population_18_64: 10602
  population_65_plus: 4399
  median_household_income: 49191
  poverty_rate: 15.89
  homeownership_rate: 78.91
  unemployment_rate: 7.26
  median_home_value: 138400
  gini_index: 0.4463
  vacancy_rate: 18.1
  race_white: 17029
  race_black: 24
  race_asian: 17
  race_native: 154
  hispanic: 1352
  bachelors_plus: 3065
districts:
  - to: "us/states/ar/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ar/districts/senate/5"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ar/districts/house/86"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Polk County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19361 |
| Under 18 | 4360 |
| 18–64 | 10602 |
| 65+ | 4399 |
| Median household income | 49191 |
| Poverty rate | 15.89 |
| Homeownership rate | 78.91 |
| Unemployment rate | 7.26 |
| Median home value | 138400 |
| Gini index | 0.4463 |
| Vacancy rate | 18.1 |
| White | 17029 |
| Black | 24 |
| Asian | 17 |
| Native | 154 |
| Hispanic/Latino | 1352 |
| Bachelor's or higher | 3065 |

## Districts

- [AR-04](/us/states/ar/districts/04.md) — 100% (congressional)
- [AR Senate District 5](/us/states/ar/districts/senate/5.md) — 100% (state senate)
- [AR House District 86](/us/states/ar/districts/house/86.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
