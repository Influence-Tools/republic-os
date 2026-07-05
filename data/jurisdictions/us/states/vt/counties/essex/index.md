---
type: Jurisdiction
title: "Essex County, VT"
classification: county
fips: "50009"
state: "VT"
demographics:
  population: 5982
  population_under_18: 999
  population_18_64: 3332
  population_65_plus: 1651
  median_household_income: 59294
  poverty_rate: 13.85
  homeownership_rate: 82.43
  unemployment_rate: 4.79
  median_home_value: 172500
  gini_index: 0.4513
  vacancy_rate: 42.99
  race_white: 5606
  race_black: 4
  race_asian: 62
  race_native: 41
  hispanic: 96
  bachelors_plus: 1394
districts:
  - to: "us/states/vt/districts/00"
    rel: in-district
    area_weight: 0.9969
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, vt]
timestamp: "2026-07-03"
---

# Essex County, VT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5982 |
| Under 18 | 999 |
| 18–64 | 3332 |
| 65+ | 1651 |
| Median household income | 59294 |
| Poverty rate | 13.85 |
| Homeownership rate | 82.43 |
| Unemployment rate | 4.79 |
| Median home value | 172500 |
| Gini index | 0.4513 |
| Vacancy rate | 42.99 |
| White | 5606 |
| Black | 4 |
| Asian | 62 |
| Native | 41 |
| Hispanic/Latino | 96 |
| Bachelor's or higher | 1394 |

## Districts

- [VT-00](/us/states/vt/districts/00.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
