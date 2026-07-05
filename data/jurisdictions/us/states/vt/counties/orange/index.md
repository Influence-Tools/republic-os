---
type: Jurisdiction
title: "Orange County, VT"
classification: county
fips: "50017"
state: "VT"
demographics:
  population: 29761
  population_under_18: 5298
  population_18_64: 17448
  population_65_plus: 7015
  median_household_income: 82232
  poverty_rate: 9.31
  homeownership_rate: 83.18
  unemployment_rate: 2.31
  median_home_value: 271300
  gini_index: 0.413
  vacancy_rate: 15.49
  race_white: 27755
  race_black: 108
  race_asian: 192
  race_native: 65
  hispanic: 538
  bachelors_plus: 12408
districts:
  - to: "us/states/vt/districts/00"
    rel: in-district
    area_weight: 0.9987
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, vt]
timestamp: "2026-07-03"
---

# Orange County, VT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 29761 |
| Under 18 | 5298 |
| 18–64 | 17448 |
| 65+ | 7015 |
| Median household income | 82232 |
| Poverty rate | 9.31 |
| Homeownership rate | 83.18 |
| Unemployment rate | 2.31 |
| Median home value | 271300 |
| Gini index | 0.413 |
| Vacancy rate | 15.49 |
| White | 27755 |
| Black | 108 |
| Asian | 192 |
| Native | 65 |
| Hispanic/Latino | 538 |
| Bachelor's or higher | 12408 |

## Districts

- [VT-00](/us/states/vt/districts/00.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
