---
type: Jurisdiction
title: "Lincoln County, MN"
classification: county
fips: "27081"
state: "MN"
demographics:
  population: 5603
  population_under_18: 1259
  population_18_64: 2949
  population_65_plus: 1395
  median_household_income: 69694
  poverty_rate: 11.95
  homeownership_rate: 81.43
  unemployment_rate: 2.66
  median_home_value: 164400
  gini_index: 0.4614
  vacancy_rate: 19.7
  race_white: 5314
  race_black: 6
  race_asian: 42
  race_native: 21
  hispanic: 147
  bachelors_plus: 1295
districts:
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mn/districts/senate/21"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Lincoln County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5603 |
| Under 18 | 1259 |
| 18–64 | 2949 |
| 65+ | 1395 |
| Median household income | 69694 |
| Poverty rate | 11.95 |
| Homeownership rate | 81.43 |
| Unemployment rate | 2.66 |
| Median home value | 164400 |
| Gini index | 0.4614 |
| Vacancy rate | 19.7 |
| White | 5314 |
| Black | 6 |
| Asian | 42 |
| Native | 21 |
| Hispanic/Latino | 147 |
| Bachelor's or higher | 1295 |

## Districts

- [MN-07](/us/states/mn/districts/07.md) — 100% (congressional)
- [MN Senate District 21](/us/states/mn/districts/senate/21.md) — 100% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
