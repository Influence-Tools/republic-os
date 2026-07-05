---
type: Jurisdiction
title: "Jasper County, IA"
classification: county
fips: "19099"
state: "IA"
demographics:
  population: 37954
  population_under_18: 8357
  population_18_64: 22097
  population_65_plus: 7500
  median_household_income: 71311
  poverty_rate: 8.3
  homeownership_rate: 72.35
  unemployment_rate: 5.68
  median_home_value: 186300
  gini_index: 0.4437
  vacancy_rate: 7.63
  race_white: 34806
  race_black: 583
  race_asian: 281
  race_native: 32
  hispanic: 1177
  bachelors_plus: 7092
districts:
  - to: "us/states/ia/districts/01"
    rel: in-district
    area_weight: 0.9976
  - to: "us/states/ia/districts/senate/19"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/house/38"
    rel: in-district
    area_weight: 0.7479
  - to: "us/states/ia/districts/house/37"
    rel: in-district
    area_weight: 0.252
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Jasper County, IA

County jurisdiction — 7 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 37954 |
| Under 18 | 8357 |
| 18–64 | 22097 |
| 65+ | 7500 |
| Median household income | 71311 |
| Poverty rate | 8.3 |
| Homeownership rate | 72.35 |
| Unemployment rate | 5.68 |
| Median home value | 186300 |
| Gini index | 0.4437 |
| Vacancy rate | 7.63 |
| White | 34806 |
| Black | 583 |
| Asian | 281 |
| Native | 32 |
| Hispanic/Latino | 1177 |
| Bachelor's or higher | 7092 |

## Districts

- [IA-01](/us/states/ia/districts/01.md) — 100% (congressional)
- [IA Senate District 19](/us/states/ia/districts/senate/19.md) — 100% (state senate)
- [IA House District 38](/us/states/ia/districts/house/38.md) — 75% (state house)
- [IA House District 37](/us/states/ia/districts/house/37.md) — 25% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
