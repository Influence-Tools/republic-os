---
type: Jurisdiction
title: "Polk County, NE"
classification: county
fips: "31143"
state: "NE"
demographics:
  population: 5225
  population_under_18: 1165
  population_18_64: 2849
  population_65_plus: 1211
  median_household_income: 69768
  poverty_rate: 7.87
  homeownership_rate: 78.95
  unemployment_rate: 1.33
  median_home_value: 189900
  gini_index: 0.4013
  vacancy_rate: 16.48
  race_white: 4757
  race_black: 10
  race_asian: 11
  race_native: 6
  hispanic: 330
  bachelors_plus: 972
districts:
  - to: "us/states/ne/districts/03"
    rel: in-district
    area_weight: 0.6556
  - to: "us/states/ne/districts/01"
    rel: in-district
    area_weight: 0.3444
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ne]
timestamp: "2026-07-03"
---

# Polk County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5225 |
| Under 18 | 1165 |
| 18–64 | 2849 |
| 65+ | 1211 |
| Median household income | 69768 |
| Poverty rate | 7.87 |
| Homeownership rate | 78.95 |
| Unemployment rate | 1.33 |
| Median home value | 189900 |
| Gini index | 0.4013 |
| Vacancy rate | 16.48 |
| White | 4757 |
| Black | 10 |
| Asian | 11 |
| Native | 6 |
| Hispanic/Latino | 330 |
| Bachelor's or higher | 972 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 66% (congressional)
- [NE-01](/us/states/ne/districts/01.md) — 34% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
