---
type: Jurisdiction
title: "Boone County, AR"
classification: county
fips: "05009"
state: "AR"
demographics:
  population: 38138
  population_under_18: 8586
  population_18_64: 21469
  population_65_plus: 8083
  median_household_income: 55143
  poverty_rate: 11.71
  homeownership_rate: 70.81
  unemployment_rate: 2.53
  median_home_value: 188900
  gini_index: 0.4323
  vacancy_rate: 12.01
  race_white: 35826
  race_black: 96
  race_asian: 121
  race_native: 144
  hispanic: 1202
  bachelors_plus: 6115
districts:
  - to: "us/states/ar/districts/01"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/ar/districts/senate/28"
    rel: in-district
    area_weight: 0.6048
  - to: "us/states/ar/districts/senate/23"
    rel: in-district
    area_weight: 0.3951
  - to: "us/states/ar/districts/house/5"
    rel: in-district
    area_weight: 0.6026
  - to: "us/states/ar/districts/house/6"
    rel: in-district
    area_weight: 0.3971
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Boone County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 38138 |
| Under 18 | 8586 |
| 18–64 | 21469 |
| 65+ | 8083 |
| Median household income | 55143 |
| Poverty rate | 11.71 |
| Homeownership rate | 70.81 |
| Unemployment rate | 2.53 |
| Median home value | 188900 |
| Gini index | 0.4323 |
| Vacancy rate | 12.01 |
| White | 35826 |
| Black | 96 |
| Asian | 121 |
| Native | 144 |
| Hispanic/Latino | 1202 |
| Bachelor's or higher | 6115 |

## Districts

- [AR-01](/us/states/ar/districts/01.md) — 100% (congressional)
- [AR Senate District 28](/us/states/ar/districts/senate/28.md) — 60% (state senate)
- [AR Senate District 23](/us/states/ar/districts/senate/23.md) — 40% (state senate)
- [AR House District 5](/us/states/ar/districts/house/5.md) — 60% (state house)
- [AR House District 6](/us/states/ar/districts/house/6.md) — 40% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
