---
type: Jurisdiction
title: "Alpena County, MI"
classification: county
fips: "26007"
state: "MI"
demographics:
  population: 28880
  population_under_18: 5333
  population_18_64: 16282
  population_65_plus: 7265
  median_household_income: 53950
  poverty_rate: 17.96
  homeownership_rate: 80.0
  unemployment_rate: 6.18
  median_home_value: 153900
  gini_index: 0.4678
  vacancy_rate: 17.11
  race_white: 26743
  race_black: 291
  race_asian: 53
  race_native: 25
  hispanic: 477
  bachelors_plus: 5470
districts:
  - to: "us/states/mi/districts/01"
    rel: in-district
    area_weight: 0.3503
  - to: "us/states/mi/districts/senate/36"
    rel: in-district
    area_weight: 0.3501
  - to: "us/states/mi/districts/house/106"
    rel: in-district
    area_weight: 0.3501
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Alpena County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 28880 |
| Under 18 | 5333 |
| 18–64 | 16282 |
| 65+ | 7265 |
| Median household income | 53950 |
| Poverty rate | 17.96 |
| Homeownership rate | 80.0 |
| Unemployment rate | 6.18 |
| Median home value | 153900 |
| Gini index | 0.4678 |
| Vacancy rate | 17.11 |
| White | 26743 |
| Black | 291 |
| Asian | 53 |
| Native | 25 |
| Hispanic/Latino | 477 |
| Bachelor's or higher | 5470 |

## Districts

- [MI-01](/us/states/mi/districts/01.md) — 35% (congressional)
- [MI Senate District 36](/us/states/mi/districts/senate/36.md) — 35% (state senate)
- [MI House District 106](/us/states/mi/districts/house/106.md) — 35% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
