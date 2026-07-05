---
type: Jurisdiction
title: "Carroll County, AR"
classification: county
fips: "05015"
state: "AR"
demographics:
  population: 28626
  population_under_18: 6204
  population_18_64: 15717
  population_65_plus: 6705
  median_household_income: 54230
  poverty_rate: 17.18
  homeownership_rate: 77.48
  unemployment_rate: 4.71
  median_home_value: 210400
  gini_index: 0.4591
  vacancy_rate: 18.7
  race_white: 20802
  race_black: 94
  race_asian: 372
  race_native: 331
  hispanic: 4504
  bachelors_plus: 5481
districts:
  - to: "us/states/ar/districts/03"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/ar/districts/senate/28"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ar/districts/house/6"
    rel: in-district
    area_weight: 0.6608
  - to: "us/states/ar/districts/house/26"
    rel: in-district
    area_weight: 0.3385
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Carroll County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 28626 |
| Under 18 | 6204 |
| 18–64 | 15717 |
| 65+ | 6705 |
| Median household income | 54230 |
| Poverty rate | 17.18 |
| Homeownership rate | 77.48 |
| Unemployment rate | 4.71 |
| Median home value | 210400 |
| Gini index | 0.4591 |
| Vacancy rate | 18.7 |
| White | 20802 |
| Black | 94 |
| Asian | 372 |
| Native | 331 |
| Hispanic/Latino | 4504 |
| Bachelor's or higher | 5481 |

## Districts

- [AR-03](/us/states/ar/districts/03.md) — 100% (congressional)
- [AR Senate District 28](/us/states/ar/districts/senate/28.md) — 100% (state senate)
- [AR House District 6](/us/states/ar/districts/house/6.md) — 66% (state house)
- [AR House District 26](/us/states/ar/districts/house/26.md) — 34% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
