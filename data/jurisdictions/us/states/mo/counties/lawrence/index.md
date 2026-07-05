---
type: Jurisdiction
title: "Lawrence County, MO"
classification: county
fips: "29109"
state: "MO"
demographics:
  population: 38593
  population_under_18: 9809
  population_18_64: 21788
  population_65_plus: 6996
  median_household_income: 61215
  poverty_rate: 14.53
  homeownership_rate: 73.86
  unemployment_rate: 4.26
  median_home_value: 175100
  gini_index: 0.409
  vacancy_rate: 10.43
  race_white: 34058
  race_black: 107
  race_asian: 187
  race_native: 225
  hispanic: 3263
  bachelors_plus: 5821
districts:
  - to: "us/states/mo/districts/07"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/senate/29"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/157"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Lawrence County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 38593 |
| Under 18 | 9809 |
| 18–64 | 21788 |
| 65+ | 6996 |
| Median household income | 61215 |
| Poverty rate | 14.53 |
| Homeownership rate | 73.86 |
| Unemployment rate | 4.26 |
| Median home value | 175100 |
| Gini index | 0.409 |
| Vacancy rate | 10.43 |
| White | 34058 |
| Black | 107 |
| Asian | 187 |
| Native | 225 |
| Hispanic/Latino | 3263 |
| Bachelor's or higher | 5821 |

## Districts

- [MO-07](/us/states/mo/districts/07.md) — 100% (congressional)
- [MO Senate District 29](/us/states/mo/districts/senate/29.md) — 100% (state senate)
- [MO House District 157](/us/states/mo/districts/house/157.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
