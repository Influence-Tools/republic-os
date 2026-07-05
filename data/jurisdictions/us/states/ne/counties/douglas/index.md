---
type: Jurisdiction
title: "Douglas County, NE"
classification: county
fips: "31055"
state: "NE"
demographics:
  population: 590736
  population_under_18: 149685
  population_18_64: 357787
  population_65_plus: 83264
  median_household_income: 80391
  poverty_rate: 11.8
  homeownership_rate: 61.53
  unemployment_rate: 3.84
  median_home_value: 266100
  gini_index: 0.4845
  vacancy_rate: 5.22
  race_white: 405474
  race_black: 62368
  race_asian: 25957
  race_native: 4344
  hispanic: 85851
  bachelors_plus: 224487
districts:
  - to: "us/states/ne/districts/02"
    rel: in-district
    area_weight: 0.9969
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ne]
timestamp: "2026-07-03"
---

# Douglas County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 590736 |
| Under 18 | 149685 |
| 18–64 | 357787 |
| 65+ | 83264 |
| Median household income | 80391 |
| Poverty rate | 11.8 |
| Homeownership rate | 61.53 |
| Unemployment rate | 3.84 |
| Median home value | 266100 |
| Gini index | 0.4845 |
| Vacancy rate | 5.22 |
| White | 405474 |
| Black | 62368 |
| Asian | 25957 |
| Native | 4344 |
| Hispanic/Latino | 85851 |
| Bachelor's or higher | 224487 |

## Districts

- [NE-02](/us/states/ne/districts/02.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
