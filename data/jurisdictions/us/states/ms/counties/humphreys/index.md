---
type: Jurisdiction
title: "Humphreys County, MS"
classification: county
fips: "28053"
state: "MS"
demographics:
  population: 7395
  population_under_18: 1862
  population_18_64: 4135
  population_65_plus: 1398
  median_household_income: 33731
  poverty_rate: 27.04
  homeownership_rate: 61.69
  unemployment_rate: 12.52
  median_home_value: 87800
  gini_index: 0.5408
  vacancy_rate: 17.36
  race_white: 1497
  race_black: 5780
  race_asian: 14
  race_native: 13
  hispanic: 31
  bachelors_plus: 1465
districts:
  - to: "us/states/ms/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ms/districts/senate/22"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/ms/districts/house/51"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Humphreys County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7395 |
| Under 18 | 1862 |
| 18–64 | 4135 |
| 65+ | 1398 |
| Median household income | 33731 |
| Poverty rate | 27.04 |
| Homeownership rate | 61.69 |
| Unemployment rate | 12.52 |
| Median home value | 87800 |
| Gini index | 0.5408 |
| Vacancy rate | 17.36 |
| White | 1497 |
| Black | 5780 |
| Asian | 14 |
| Native | 13 |
| Hispanic/Latino | 31 |
| Bachelor's or higher | 1465 |

## Districts

- [MS-02](/us/states/ms/districts/02.md) — 100% (congressional)
- [MS Senate District 22](/us/states/ms/districts/senate/22.md) — 100% (state senate)
- [MS House District 51](/us/states/ms/districts/house/51.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
