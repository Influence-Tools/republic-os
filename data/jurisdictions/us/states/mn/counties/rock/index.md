---
type: Jurisdiction
title: "Rock County, MN"
classification: county
fips: "27133"
state: "MN"
demographics:
  population: 9621
  population_under_18: 2349
  population_18_64: 5306
  population_65_plus: 1966
  median_household_income: 71295
  poverty_rate: 10.62
  homeownership_rate: 76.56
  unemployment_rate: 2.61
  median_home_value: 224300
  gini_index: 0.4319
  vacancy_rate: 5.19
  race_white: 8953
  race_black: 14
  race_asian: 43
  race_native: 55
  hispanic: 384
  bachelors_plus: 2221
districts:
  - to: "us/states/mn/districts/01"
    rel: in-district
    area_weight: 0.9997
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

# Rock County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9621 |
| Under 18 | 2349 |
| 18–64 | 5306 |
| 65+ | 1966 |
| Median household income | 71295 |
| Poverty rate | 10.62 |
| Homeownership rate | 76.56 |
| Unemployment rate | 2.61 |
| Median home value | 224300 |
| Gini index | 0.4319 |
| Vacancy rate | 5.19 |
| White | 8953 |
| Black | 14 |
| Asian | 43 |
| Native | 55 |
| Hispanic/Latino | 384 |
| Bachelor's or higher | 2221 |

## Districts

- [MN-01](/us/states/mn/districts/01.md) — 100% (congressional)
- [MN Senate District 21](/us/states/mn/districts/senate/21.md) — 100% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
