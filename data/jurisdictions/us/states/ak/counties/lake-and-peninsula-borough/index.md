---
type: Jurisdiction
title: "Lake and Peninsula Borough, AK"
classification: county
fips: "02164"
state: "AK"
demographics:
  population: 1013
  population_under_18: 267
  population_18_64: 439
  population_65_plus: 307
  median_household_income: 65625
  poverty_rate: 12.8
  homeownership_rate: 65.43
  unemployment_rate: 8.59
  median_home_value: 237500
  gini_index: 0.4261
  vacancy_rate: 75.75
  race_white: 174
  race_black: 14
  race_asian: 19
  race_native: 455
  hispanic: 28
  bachelors_plus: 143
districts:
  - to: "us/states/ak/districts/00"
    rel: in-district
    area_weight: 0.7926
  - to: "us/states/ak/districts/senate/s"
    rel: in-district
    area_weight: 0.7907
  - to: "us/states/ak/districts/house/37"
    rel: in-district
    area_weight: 0.7907
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ak]
timestamp: "2026-07-03"
---

# Lake and Peninsula Borough, AK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1013 |
| Under 18 | 267 |
| 18–64 | 439 |
| 65+ | 307 |
| Median household income | 65625 |
| Poverty rate | 12.8 |
| Homeownership rate | 65.43 |
| Unemployment rate | 8.59 |
| Median home value | 237500 |
| Gini index | 0.4261 |
| Vacancy rate | 75.75 |
| White | 174 |
| Black | 14 |
| Asian | 19 |
| Native | 455 |
| Hispanic/Latino | 28 |
| Bachelor's or higher | 143 |

## Districts

- [AK-00](/us/states/ak/districts/00.md) — 79% (congressional)
- [AK Senate District S](/us/states/ak/districts/senate/s.md) — 79% (state senate)
- [AK House District 37](/us/states/ak/districts/house/37.md) — 79% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
