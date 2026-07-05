---
type: Jurisdiction
title: "Antelope County, NE"
classification: county
fips: "31003"
state: "NE"
demographics:
  population: 6305
  population_under_18: 1564
  population_18_64: 3183
  population_65_plus: 1558
  median_household_income: 66105
  poverty_rate: 9.24
  homeownership_rate: 79.02
  unemployment_rate: 1.73
  median_home_value: 130300
  gini_index: 0.4314
  vacancy_rate: 16.29
  race_white: 5880
  race_black: 52
  race_asian: 19
  race_native: 6
  hispanic: 252
  bachelors_plus: 1191
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

# Antelope County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6305 |
| Under 18 | 1564 |
| 18–64 | 3183 |
| 65+ | 1558 |
| Median household income | 66105 |
| Poverty rate | 9.24 |
| Homeownership rate | 79.02 |
| Unemployment rate | 1.73 |
| Median home value | 130300 |
| Gini index | 0.4314 |
| Vacancy rate | 16.29 |
| White | 5880 |
| Black | 52 |
| Asian | 19 |
| Native | 6 |
| Hispanic/Latino | 252 |
| Bachelor's or higher | 1191 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
