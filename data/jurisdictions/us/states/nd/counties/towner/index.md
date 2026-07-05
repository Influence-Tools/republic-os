---
type: Jurisdiction
title: "Towner County, ND"
classification: county
fips: "38095"
state: "ND"
demographics:
  population: 2079
  population_under_18: 517
  population_18_64: 1083
  population_65_plus: 479
  median_household_income: 67350
  poverty_rate: 8.5
  homeownership_rate: 78.77
  unemployment_rate: 0.66
  median_home_value: 134800
  gini_index: 0.4654
  vacancy_rate: 21.2
  race_white: 1739
  race_black: 1
  race_asian: 0
  race_native: 127
  hispanic: 106
  bachelors_plus: 395
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/nd/districts/senate/15"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/nd/districts/house/15"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Towner County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2079 |
| Under 18 | 517 |
| 18–64 | 1083 |
| 65+ | 479 |
| Median household income | 67350 |
| Poverty rate | 8.5 |
| Homeownership rate | 78.77 |
| Unemployment rate | 0.66 |
| Median home value | 134800 |
| Gini index | 0.4654 |
| Vacancy rate | 21.2 |
| White | 1739 |
| Black | 1 |
| Asian | 0 |
| Native | 127 |
| Hispanic/Latino | 106 |
| Bachelor's or higher | 395 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 15](/us/states/nd/districts/senate/15.md) — 100% (state senate)
- [ND House District 15](/us/states/nd/districts/house/15.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
