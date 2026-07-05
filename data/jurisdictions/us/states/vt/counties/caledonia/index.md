---
type: Jurisdiction
title: "Caledonia County, VT"
classification: county
fips: "50005"
state: "VT"
demographics:
  population: 30475
  population_under_18: 5609
  population_18_64: 17829
  population_65_plus: 7037
  median_household_income: 69970
  poverty_rate: 11.72
  homeownership_rate: 79.2
  unemployment_rate: 2.18
  median_home_value: 227900
  gini_index: 0.438
  vacancy_rate: 19.01
  race_white: 28294
  race_black: 247
  race_asian: 136
  race_native: 54
  hispanic: 657
  bachelors_plus: 10431
districts:
  - to: "us/states/vt/districts/00"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, vt]
timestamp: "2026-07-03"
---

# Caledonia County, VT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 30475 |
| Under 18 | 5609 |
| 18–64 | 17829 |
| 65+ | 7037 |
| Median household income | 69970 |
| Poverty rate | 11.72 |
| Homeownership rate | 79.2 |
| Unemployment rate | 2.18 |
| Median home value | 227900 |
| Gini index | 0.438 |
| Vacancy rate | 19.01 |
| White | 28294 |
| Black | 247 |
| Asian | 136 |
| Native | 54 |
| Hispanic/Latino | 657 |
| Bachelor's or higher | 10431 |

## Districts

- [VT-00](/us/states/vt/districts/00.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
