---
type: Jurisdiction
title: "Osceola County, IA"
classification: county
fips: "19143"
state: "IA"
demographics:
  population: 6100
  population_under_18: 1383
  population_18_64: 3328
  population_65_plus: 1389
  median_household_income: 69239
  poverty_rate: 15.97
  homeownership_rate: 77.87
  unemployment_rate: 3.39
  median_home_value: 122600
  gini_index: 0.4344
  vacancy_rate: 8.16
  race_white: 5226
  race_black: 29
  race_asian: 35
  race_native: 65
  hispanic: 647
  bachelors_plus: 896
districts:
  - to: "us/states/ia/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/senate/3"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/house/5"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Osceola County, IA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6100 |
| Under 18 | 1383 |
| 18–64 | 3328 |
| 65+ | 1389 |
| Median household income | 69239 |
| Poverty rate | 15.97 |
| Homeownership rate | 77.87 |
| Unemployment rate | 3.39 |
| Median home value | 122600 |
| Gini index | 0.4344 |
| Vacancy rate | 8.16 |
| White | 5226 |
| Black | 29 |
| Asian | 35 |
| Native | 65 |
| Hispanic/Latino | 647 |
| Bachelor's or higher | 896 |

## Districts

- [IA-04](/us/states/ia/districts/04.md) — 100% (congressional)
- [IA Senate District 3](/us/states/ia/districts/senate/3.md) — 100% (state senate)
- [IA House District 5](/us/states/ia/districts/house/5.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
