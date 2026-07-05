---
type: Jurisdiction
title: "Burke County, GA"
classification: county
fips: "13033"
state: "GA"
demographics:
  population: 24470
  population_under_18: 6005
  population_18_64: 14134
  population_65_plus: 4331
  median_household_income: 53014
  poverty_rate: 18.34
  homeownership_rate: 70.0
  unemployment_rate: 4.97
  median_home_value: 151600
  gini_index: 0.5478
  vacancy_rate: 18.73
  race_white: 12340
  race_black: 11077
  race_asian: 122
  race_native: 26
  hispanic: 872
  bachelors_plus: 3101
districts:
  - to: "us/states/ga/districts/12"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/ga/districts/senate/23"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ga/districts/house/126"
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

# Burke County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 24470 |
| Under 18 | 6005 |
| 18–64 | 14134 |
| 65+ | 4331 |
| Median household income | 53014 |
| Poverty rate | 18.34 |
| Homeownership rate | 70.0 |
| Unemployment rate | 4.97 |
| Median home value | 151600 |
| Gini index | 0.5478 |
| Vacancy rate | 18.73 |
| White | 12340 |
| Black | 11077 |
| Asian | 122 |
| Native | 26 |
| Hispanic/Latino | 872 |
| Bachelor's or higher | 3101 |

## Districts

- [GA-12](/us/states/ga/districts/12.md) — 100% (congressional)
- [GA Senate District 23](/us/states/ga/districts/senate/23.md) — 100% (state senate)
- [GA House District 126](/us/states/ga/districts/house/126.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
