---
type: Jurisdiction
title: "Marion County, AR"
classification: county
fips: "05089"
state: "AR"
demographics:
  population: 17228
  population_under_18: 3197
  population_18_64: 9038
  population_65_plus: 4993
  median_household_income: 48619
  poverty_rate: 17.98
  homeownership_rate: 81.34
  unemployment_rate: 4.95
  median_home_value: 163300
  gini_index: 0.439
  vacancy_rate: 21.39
  race_white: 15895
  race_black: 15
  race_asian: 156
  race_native: 232
  hispanic: 470
  bachelors_plus: 2807
districts:
  - to: "us/states/ar/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ar/districts/senate/23"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ar/districts/house/4"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Marion County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17228 |
| Under 18 | 3197 |
| 18–64 | 9038 |
| 65+ | 4993 |
| Median household income | 48619 |
| Poverty rate | 17.98 |
| Homeownership rate | 81.34 |
| Unemployment rate | 4.95 |
| Median home value | 163300 |
| Gini index | 0.439 |
| Vacancy rate | 21.39 |
| White | 15895 |
| Black | 15 |
| Asian | 156 |
| Native | 232 |
| Hispanic/Latino | 470 |
| Bachelor's or higher | 2807 |

## Districts

- [AR-01](/us/states/ar/districts/01.md) — 100% (congressional)
- [AR Senate District 23](/us/states/ar/districts/senate/23.md) — 100% (state senate)
- [AR House District 4](/us/states/ar/districts/house/4.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
