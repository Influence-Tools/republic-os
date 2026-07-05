---
type: Jurisdiction
title: "Richardson County, NE"
classification: county
fips: "31147"
state: "NE"
demographics:
  population: 7751
  population_under_18: 1680
  population_18_64: 4176
  population_65_plus: 1895
  median_household_income: 60108
  poverty_rate: 10.45
  homeownership_rate: 77.32
  unemployment_rate: 3.72
  median_home_value: 100300
  gini_index: 0.4669
  vacancy_rate: 12.74
  race_white: 7057
  race_black: 76
  race_asian: 9
  race_native: 121
  hispanic: 187
  bachelors_plus: 1704
districts:
  - to: "us/states/ne/districts/03"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ne]
timestamp: "2026-07-03"
---

# Richardson County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7751 |
| Under 18 | 1680 |
| 18–64 | 4176 |
| 65+ | 1895 |
| Median household income | 60108 |
| Poverty rate | 10.45 |
| Homeownership rate | 77.32 |
| Unemployment rate | 3.72 |
| Median home value | 100300 |
| Gini index | 0.4669 |
| Vacancy rate | 12.74 |
| White | 7057 |
| Black | 76 |
| Asian | 9 |
| Native | 121 |
| Hispanic/Latino | 187 |
| Bachelor's or higher | 1704 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
