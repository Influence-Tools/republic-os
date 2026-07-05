---
type: Jurisdiction
title: "Dickinson County, MI"
classification: county
fips: "26043"
state: "MI"
demographics:
  population: 25954
  population_under_18: 5181
  population_18_64: 14495
  population_65_plus: 6278
  median_household_income: 65156
  poverty_rate: 10.55
  homeownership_rate: 82.36
  unemployment_rate: 3.6
  median_home_value: 153300
  gini_index: 0.4244
  vacancy_rate: 14.67
  race_white: 24127
  race_black: 91
  race_asian: 75
  race_native: 144
  hispanic: 511
  bachelors_plus: 6307
districts:
  - to: "us/states/mi/districts/01"
    rel: in-district
    area_weight: 0.9988
  - to: "us/states/mi/districts/senate/38"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mi/districts/house/109"
    rel: in-district
    area_weight: 0.6865
  - to: "us/states/mi/districts/house/110"
    rel: in-district
    area_weight: 0.3133
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Dickinson County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25954 |
| Under 18 | 5181 |
| 18–64 | 14495 |
| 65+ | 6278 |
| Median household income | 65156 |
| Poverty rate | 10.55 |
| Homeownership rate | 82.36 |
| Unemployment rate | 3.6 |
| Median home value | 153300 |
| Gini index | 0.4244 |
| Vacancy rate | 14.67 |
| White | 24127 |
| Black | 91 |
| Asian | 75 |
| Native | 144 |
| Hispanic/Latino | 511 |
| Bachelor's or higher | 6307 |

## Districts

- [MI-01](/us/states/mi/districts/01.md) — 100% (congressional)
- [MI Senate District 38](/us/states/mi/districts/senate/38.md) — 100% (state senate)
- [MI House District 109](/us/states/mi/districts/house/109.md) — 69% (state house)
- [MI House District 110](/us/states/mi/districts/house/110.md) — 31% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
