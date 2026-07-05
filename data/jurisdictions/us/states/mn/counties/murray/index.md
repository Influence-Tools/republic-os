---
type: Jurisdiction
title: "Murray County, MN"
classification: county
fips: "27101"
state: "MN"
demographics:
  population: 8097
  population_under_18: 1755
  population_18_64: 4190
  population_65_plus: 2152
  median_household_income: 74033
  poverty_rate: 9.32
  homeownership_rate: 82.24
  unemployment_rate: 2.69
  median_home_value: 185400
  gini_index: 0.4168
  vacancy_rate: 18.0
  race_white: 7292
  race_black: 58
  race_asian: 82
  race_native: 17
  hispanic: 420
  bachelors_plus: 1695
districts:
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mn/districts/senate/21"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Murray County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8097 |
| Under 18 | 1755 |
| 18–64 | 4190 |
| 65+ | 2152 |
| Median household income | 74033 |
| Poverty rate | 9.32 |
| Homeownership rate | 82.24 |
| Unemployment rate | 2.69 |
| Median home value | 185400 |
| Gini index | 0.4168 |
| Vacancy rate | 18.0 |
| White | 7292 |
| Black | 58 |
| Asian | 82 |
| Native | 17 |
| Hispanic/Latino | 420 |
| Bachelor's or higher | 1695 |

## Districts

- [MN-07](/us/states/mn/districts/07.md) — 100% (congressional)
- [MN Senate District 21](/us/states/mn/districts/senate/21.md) — 100% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
