---
type: Jurisdiction
title: "Stephens County, GA"
classification: county
fips: "13257"
state: "GA"
demographics:
  population: 27012
  population_under_18: 5763
  population_18_64: 15514
  population_65_plus: 5735
  median_household_income: 54754
  poverty_rate: 15.75
  homeownership_rate: 73.62
  unemployment_rate: 5.36
  median_home_value: 175300
  gini_index: 0.4388
  vacancy_rate: 14.81
  race_white: 21871
  race_black: 2197
  race_asian: 284
  race_native: 86
  hispanic: 1068
  bachelors_plus: 3908
districts:
  - to: "us/states/ga/districts/09"
    rel: in-district
    area_weight: 0.9973
  - to: "us/states/ga/districts/senate/50"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ga/districts/house/32"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Stephens County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 27012 |
| Under 18 | 5763 |
| 18–64 | 15514 |
| 65+ | 5735 |
| Median household income | 54754 |
| Poverty rate | 15.75 |
| Homeownership rate | 73.62 |
| Unemployment rate | 5.36 |
| Median home value | 175300 |
| Gini index | 0.4388 |
| Vacancy rate | 14.81 |
| White | 21871 |
| Black | 2197 |
| Asian | 284 |
| Native | 86 |
| Hispanic/Latino | 1068 |
| Bachelor's or higher | 3908 |

## Districts

- [GA-09](/us/states/ga/districts/09.md) — 100% (congressional)
- [GA Senate District 50](/us/states/ga/districts/senate/50.md) — 100% (state senate)
- [GA House District 32](/us/states/ga/districts/house/32.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
