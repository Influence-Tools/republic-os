---
type: Jurisdiction
title: "Seminole County, GA"
classification: county
fips: "13253"
state: "GA"
demographics:
  population: 9156
  population_under_18: 1836
  population_18_64: 4963
  population_65_plus: 2357
  median_household_income: 49495
  poverty_rate: 20.11
  homeownership_rate: 80.2
  unemployment_rate: 5.97
  median_home_value: 121900
  gini_index: 0.4831
  vacancy_rate: 25.86
  race_white: 5772
  race_black: 3063
  race_asian: 43
  race_native: 26
  hispanic: 284
  bachelors_plus: 1252
districts:
  - to: "us/states/ga/districts/02"
    rel: in-district
    area_weight: 0.9977
  - to: "us/states/ga/districts/senate/11"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/ga/districts/house/154"
    rel: in-district
    area_weight: 0.9992
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Seminole County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9156 |
| Under 18 | 1836 |
| 18–64 | 4963 |
| 65+ | 2357 |
| Median household income | 49495 |
| Poverty rate | 20.11 |
| Homeownership rate | 80.2 |
| Unemployment rate | 5.97 |
| Median home value | 121900 |
| Gini index | 0.4831 |
| Vacancy rate | 25.86 |
| White | 5772 |
| Black | 3063 |
| Asian | 43 |
| Native | 26 |
| Hispanic/Latino | 284 |
| Bachelor's or higher | 1252 |

## Districts

- [GA-02](/us/states/ga/districts/02.md) — 100% (congressional)
- [GA Senate District 11](/us/states/ga/districts/senate/11.md) — 100% (state senate)
- [GA House District 154](/us/states/ga/districts/house/154.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
