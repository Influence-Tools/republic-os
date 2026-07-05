---
type: Jurisdiction
title: "Kimball County, NE"
classification: county
fips: "31105"
state: "NE"
demographics:
  population: 3248
  population_under_18: 635
  population_18_64: 1699
  population_65_plus: 914
  median_household_income: 56712
  poverty_rate: 12.17
  homeownership_rate: 75.22
  unemployment_rate: 0.72
  median_home_value: 109400
  gini_index: 0.4427
  vacancy_rate: 16.44
  race_white: 2733
  race_black: 54
  race_asian: 22
  race_native: 57
  hispanic: 321
  bachelors_plus: 446
districts:
  - to: "us/states/ne/districts/03"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ne]
timestamp: "2026-07-03"
---

# Kimball County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3248 |
| Under 18 | 635 |
| 18–64 | 1699 |
| 65+ | 914 |
| Median household income | 56712 |
| Poverty rate | 12.17 |
| Homeownership rate | 75.22 |
| Unemployment rate | 0.72 |
| Median home value | 109400 |
| Gini index | 0.4427 |
| Vacancy rate | 16.44 |
| White | 2733 |
| Black | 54 |
| Asian | 22 |
| Native | 57 |
| Hispanic/Latino | 321 |
| Bachelor's or higher | 446 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
