---
type: Jurisdiction
title: "Kearney County, NE"
classification: county
fips: "31099"
state: "NE"
demographics:
  population: 6713
  population_under_18: 1663
  population_18_64: 3671
  population_65_plus: 1379
  median_household_income: 78631
  poverty_rate: 7.21
  homeownership_rate: 77.47
  unemployment_rate: 1.67
  median_home_value: 223400
  gini_index: 0.4705
  vacancy_rate: 5.82
  race_white: 6185
  race_black: 1
  race_asian: 36
  race_native: 16
  hispanic: 459
  bachelors_plus: 1888
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

# Kearney County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6713 |
| Under 18 | 1663 |
| 18–64 | 3671 |
| 65+ | 1379 |
| Median household income | 78631 |
| Poverty rate | 7.21 |
| Homeownership rate | 77.47 |
| Unemployment rate | 1.67 |
| Median home value | 223400 |
| Gini index | 0.4705 |
| Vacancy rate | 5.82 |
| White | 6185 |
| Black | 1 |
| Asian | 36 |
| Native | 16 |
| Hispanic/Latino | 459 |
| Bachelor's or higher | 1888 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
