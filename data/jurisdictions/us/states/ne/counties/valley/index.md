---
type: Jurisdiction
title: "Valley County, NE"
classification: county
fips: "31175"
state: "NE"
demographics:
  population: 4066
  population_under_18: 894
  population_18_64: 2122
  population_65_plus: 1050
  median_household_income: 61852
  poverty_rate: 9.31
  homeownership_rate: 73.78
  unemployment_rate: 0.24
  median_home_value: 154600
  gini_index: 0.447
  vacancy_rate: 14.8
  race_white: 3876
  race_black: 7
  race_asian: 6
  race_native: 42
  hispanic: 119
  bachelors_plus: 921
districts:
  - to: "us/states/ne/districts/03"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ne]
timestamp: "2026-07-03"
---

# Valley County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4066 |
| Under 18 | 894 |
| 18–64 | 2122 |
| 65+ | 1050 |
| Median household income | 61852 |
| Poverty rate | 9.31 |
| Homeownership rate | 73.78 |
| Unemployment rate | 0.24 |
| Median home value | 154600 |
| Gini index | 0.447 |
| Vacancy rate | 14.8 |
| White | 3876 |
| Black | 7 |
| Asian | 6 |
| Native | 42 |
| Hispanic/Latino | 119 |
| Bachelor's or higher | 921 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
