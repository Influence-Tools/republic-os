---
type: Jurisdiction
title: "Tuolumne County, CA"
classification: county
fips: "06109"
state: "CA"
demographics:
  population: 54498
  population_under_18: 9305
  population_18_64: 29854
  population_65_plus: 15339
  median_household_income: 77404
  poverty_rate: 10.44
  homeownership_rate: 73.91
  unemployment_rate: 8.22
  median_home_value: 433200
  gini_index: 0.4517
  vacancy_rate: 28.17
  race_white: 43875
  race_black: 1082
  race_asian: 844
  race_native: 867
  hispanic: 7398
  bachelors_plus: 13797
districts:
  - to: "us/states/ca/districts/05"
    rel: in-district
    area_weight: 0.998
  - to: "us/states/ca/districts/senate/4"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ca/districts/house/8"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Tuolumne County, CA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 54498 |
| Under 18 | 9305 |
| 18–64 | 29854 |
| 65+ | 15339 |
| Median household income | 77404 |
| Poverty rate | 10.44 |
| Homeownership rate | 73.91 |
| Unemployment rate | 8.22 |
| Median home value | 433200 |
| Gini index | 0.4517 |
| Vacancy rate | 28.17 |
| White | 43875 |
| Black | 1082 |
| Asian | 844 |
| Native | 867 |
| Hispanic/Latino | 7398 |
| Bachelor's or higher | 13797 |

## Districts

- [CA-05](/us/states/ca/districts/05.md) — 100% (congressional)
- [CA Senate District 4](/us/states/ca/districts/senate/4.md) — 100% (state senate)
- [CA House District 8](/us/states/ca/districts/house/8.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
