---
type: Jurisdiction
title: "Brooks County, GA"
classification: county
fips: "13027"
state: "GA"
demographics:
  population: 16293
  population_under_18: 3258
  population_18_64: 9447
  population_65_plus: 3588
  median_household_income: 46807
  poverty_rate: 25.43
  homeownership_rate: 71.71
  unemployment_rate: 5.01
  median_home_value: 139200
  gini_index: 0.4832
  vacancy_rate: 17.74
  race_white: 9124
  race_black: 5531
  race_asian: 235
  race_native: 8
  hispanic: 1112
  bachelors_plus: 2575
districts:
  - to: "us/states/ga/districts/08"
    rel: in-district
    area_weight: 0.9981
  - to: "us/states/ga/districts/senate/11"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/ga/districts/house/175"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Brooks County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16293 |
| Under 18 | 3258 |
| 18–64 | 9447 |
| 65+ | 3588 |
| Median household income | 46807 |
| Poverty rate | 25.43 |
| Homeownership rate | 71.71 |
| Unemployment rate | 5.01 |
| Median home value | 139200 |
| Gini index | 0.4832 |
| Vacancy rate | 17.74 |
| White | 9124 |
| Black | 5531 |
| Asian | 235 |
| Native | 8 |
| Hispanic/Latino | 1112 |
| Bachelor's or higher | 2575 |

## Districts

- [GA-08](/us/states/ga/districts/08.md) — 100% (congressional)
- [GA Senate District 11](/us/states/ga/districts/senate/11.md) — 100% (state senate)
- [GA House District 175](/us/states/ga/districts/house/175.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
