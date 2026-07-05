---
type: Jurisdiction
title: "Iosco County, MI"
classification: county
fips: "26069"
state: "MI"
demographics:
  population: 25347
  population_under_18: 4308
  population_18_64: 13167
  population_65_plus: 7872
  median_household_income: 50066
  poverty_rate: 17.73
  homeownership_rate: 82.07
  unemployment_rate: 6.49
  median_home_value: 142200
  gini_index: 0.4711
  vacancy_rate: 41.61
  race_white: 23326
  race_black: 237
  race_asian: 198
  race_native: 62
  hispanic: 719
  bachelors_plus: 5289
districts:
  - to: "us/states/mi/districts/01"
    rel: in-district
    area_weight: 0.2994
  - to: "us/states/mi/districts/senate/36"
    rel: in-district
    area_weight: 0.2996
  - to: "us/states/mi/districts/house/99"
    rel: in-district
    area_weight: 0.2996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Iosco County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25347 |
| Under 18 | 4308 |
| 18–64 | 13167 |
| 65+ | 7872 |
| Median household income | 50066 |
| Poverty rate | 17.73 |
| Homeownership rate | 82.07 |
| Unemployment rate | 6.49 |
| Median home value | 142200 |
| Gini index | 0.4711 |
| Vacancy rate | 41.61 |
| White | 23326 |
| Black | 237 |
| Asian | 198 |
| Native | 62 |
| Hispanic/Latino | 719 |
| Bachelor's or higher | 5289 |

## Districts

- [MI-01](/us/states/mi/districts/01.md) — 30% (congressional)
- [MI Senate District 36](/us/states/mi/districts/senate/36.md) — 30% (state senate)
- [MI House District 99](/us/states/mi/districts/house/99.md) — 30% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
