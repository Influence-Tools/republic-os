---
type: Jurisdiction
title: "O'Brien County, IA"
classification: county
fips: "19141"
state: "IA"
demographics:
  population: 14126
  population_under_18: 3446
  population_18_64: 7691
  population_65_plus: 2989
  median_household_income: 68356
  poverty_rate: 13.32
  homeownership_rate: 76.11
  unemployment_rate: 1.0
  median_home_value: 173100
  gini_index: 0.3922
  vacancy_rate: 11.5
  race_white: 12358
  race_black: 240
  race_asian: 92
  race_native: 55
  hispanic: 1074
  bachelors_plus: 2596
districts:
  - to: "us/states/ia/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/senate/3"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/house/5"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# O'Brien County, IA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14126 |
| Under 18 | 3446 |
| 18–64 | 7691 |
| 65+ | 2989 |
| Median household income | 68356 |
| Poverty rate | 13.32 |
| Homeownership rate | 76.11 |
| Unemployment rate | 1.0 |
| Median home value | 173100 |
| Gini index | 0.3922 |
| Vacancy rate | 11.5 |
| White | 12358 |
| Black | 240 |
| Asian | 92 |
| Native | 55 |
| Hispanic/Latino | 1074 |
| Bachelor's or higher | 2596 |

## Districts

- [IA-04](/us/states/ia/districts/04.md) — 100% (congressional)
- [IA Senate District 3](/us/states/ia/districts/senate/3.md) — 100% (state senate)
- [IA House District 5](/us/states/ia/districts/house/5.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
