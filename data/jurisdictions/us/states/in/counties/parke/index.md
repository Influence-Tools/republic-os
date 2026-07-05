---
type: Jurisdiction
title: "Parke County, IN"
classification: county
fips: "18121"
state: "IN"
demographics:
  population: 16406
  population_under_18: 3651
  population_18_64: 9385
  population_65_plus: 3370
  median_household_income: 68485
  poverty_rate: 16.16
  homeownership_rate: 82.43
  unemployment_rate: 4.36
  median_home_value: 151200
  gini_index: 0.4187
  vacancy_rate: 19.72
  race_white: 15503
  race_black: 261
  race_asian: 0
  race_native: 6
  hispanic: 125
  bachelors_plus: 2515
districts:
  - to: "us/states/in/districts/08"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/in/districts/senate/23"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/in/districts/house/42"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Parke County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16406 |
| Under 18 | 3651 |
| 18–64 | 9385 |
| 65+ | 3370 |
| Median household income | 68485 |
| Poverty rate | 16.16 |
| Homeownership rate | 82.43 |
| Unemployment rate | 4.36 |
| Median home value | 151200 |
| Gini index | 0.4187 |
| Vacancy rate | 19.72 |
| White | 15503 |
| Black | 261 |
| Asian | 0 |
| Native | 6 |
| Hispanic/Latino | 125 |
| Bachelor's or higher | 2515 |

## Districts

- [IN-08](/us/states/in/districts/08.md) — 100% (congressional)
- [IN Senate District 23](/us/states/in/districts/senate/23.md) — 100% (state senate)
- [IN House District 42](/us/states/in/districts/house/42.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
