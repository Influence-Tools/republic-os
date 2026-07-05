---
type: Jurisdiction
title: "Wheeler County, OR"
classification: county
fips: "41069"
state: "OR"
demographics:
  population: 1485
  population_under_18: 175
  population_18_64: 732
  population_65_plus: 578
  median_household_income: 55284
  poverty_rate: 10.77
  homeownership_rate: 71.83
  unemployment_rate: 2.64
  median_home_value: 272400
  gini_index: 0.4897
  vacancy_rate: 22.58
  race_white: 1264
  race_black: 0
  race_asian: 7
  race_native: 2
  hispanic: 72
  bachelors_plus: 321
districts:
  - to: "us/states/or/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/or/districts/senate/29"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/or/districts/house/57"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, or]
timestamp: "2026-07-03"
---

# Wheeler County, OR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1485 |
| Under 18 | 175 |
| 18–64 | 732 |
| 65+ | 578 |
| Median household income | 55284 |
| Poverty rate | 10.77 |
| Homeownership rate | 71.83 |
| Unemployment rate | 2.64 |
| Median home value | 272400 |
| Gini index | 0.4897 |
| Vacancy rate | 22.58 |
| White | 1264 |
| Black | 0 |
| Asian | 7 |
| Native | 2 |
| Hispanic/Latino | 72 |
| Bachelor's or higher | 321 |

## Districts

- [OR-02](/us/states/or/districts/02.md) — 100% (congressional)
- [OR Senate District 29](/us/states/or/districts/senate/29.md) — 100% (state senate)
- [OR House District 57](/us/states/or/districts/house/57.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
