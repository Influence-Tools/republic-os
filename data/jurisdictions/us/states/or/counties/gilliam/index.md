---
type: Jurisdiction
title: "Gilliam County, OR"
classification: county
fips: "41021"
state: "OR"
demographics:
  population: 1971
  population_under_18: 375
  population_18_64: 957
  population_65_plus: 639
  median_household_income: 66917
  poverty_rate: 15.25
  homeownership_rate: 74.06
  unemployment_rate: 2.79
  median_home_value: 189300
  gini_index: 0.4593
  vacancy_rate: 23.11
  race_white: 1602
  race_black: 0
  race_asian: 0
  race_native: 32
  hispanic: 186
  bachelors_plus: 382
districts:
  - to: "us/states/or/districts/02"
    rel: in-district
    area_weight: 0.9999
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

# Gilliam County, OR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1971 |
| Under 18 | 375 |
| 18–64 | 957 |
| 65+ | 639 |
| Median household income | 66917 |
| Poverty rate | 15.25 |
| Homeownership rate | 74.06 |
| Unemployment rate | 2.79 |
| Median home value | 189300 |
| Gini index | 0.4593 |
| Vacancy rate | 23.11 |
| White | 1602 |
| Black | 0 |
| Asian | 0 |
| Native | 32 |
| Hispanic/Latino | 186 |
| Bachelor's or higher | 382 |

## Districts

- [OR-02](/us/states/or/districts/02.md) — 100% (congressional)
- [OR Senate District 29](/us/states/or/districts/senate/29.md) — 100% (state senate)
- [OR House District 57](/us/states/or/districts/house/57.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
