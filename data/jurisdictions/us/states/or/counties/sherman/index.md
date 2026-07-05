---
type: Jurisdiction
title: "Sherman County, OR"
classification: county
fips: "41055"
state: "OR"
demographics:
  population: 1938
  population_under_18: 390
  population_18_64: 1137
  population_65_plus: 411
  median_household_income: 60161
  poverty_rate: 22.03
  homeownership_rate: 65.92
  unemployment_rate: 1.01
  median_home_value: 211800
  gini_index: 0.4269
  vacancy_rate: 17.03
  race_white: 1663
  race_black: 9
  race_asian: 5
  race_native: 9
  hispanic: 85
  bachelors_plus: 286
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

# Sherman County, OR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1938 |
| Under 18 | 390 |
| 18–64 | 1137 |
| 65+ | 411 |
| Median household income | 60161 |
| Poverty rate | 22.03 |
| Homeownership rate | 65.92 |
| Unemployment rate | 1.01 |
| Median home value | 211800 |
| Gini index | 0.4269 |
| Vacancy rate | 17.03 |
| White | 1663 |
| Black | 9 |
| Asian | 5 |
| Native | 9 |
| Hispanic/Latino | 85 |
| Bachelor's or higher | 286 |

## Districts

- [OR-02](/us/states/or/districts/02.md) — 100% (congressional)
- [OR Senate District 29](/us/states/or/districts/senate/29.md) — 100% (state senate)
- [OR House District 57](/us/states/or/districts/house/57.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
