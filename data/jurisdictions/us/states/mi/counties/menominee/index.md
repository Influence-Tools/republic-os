---
type: Jurisdiction
title: "Menominee County, MI"
classification: county
fips: "26109"
state: "MI"
demographics:
  population: 23247
  population_under_18: 4054
  population_18_64: 12932
  population_65_plus: 6261
  median_household_income: 56435
  poverty_rate: 12.18
  homeownership_rate: 80.68
  unemployment_rate: 4.16
  median_home_value: 151800
  gini_index: 0.4335
  vacancy_rate: 21.87
  race_white: 21318
  race_black: 101
  race_asian: 90
  race_native: 484
  hispanic: 564
  bachelors_plus: 4222
districts:
  - to: "us/states/mi/districts/01"
    rel: in-district
    area_weight: 0.7842
  - to: "us/states/mi/districts/senate/38"
    rel: in-district
    area_weight: 0.7866
  - to: "us/states/mi/districts/house/108"
    rel: in-district
    area_weight: 0.7866
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Menominee County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 23247 |
| Under 18 | 4054 |
| 18–64 | 12932 |
| 65+ | 6261 |
| Median household income | 56435 |
| Poverty rate | 12.18 |
| Homeownership rate | 80.68 |
| Unemployment rate | 4.16 |
| Median home value | 151800 |
| Gini index | 0.4335 |
| Vacancy rate | 21.87 |
| White | 21318 |
| Black | 101 |
| Asian | 90 |
| Native | 484 |
| Hispanic/Latino | 564 |
| Bachelor's or higher | 4222 |

## Districts

- [MI-01](/us/states/mi/districts/01.md) — 78% (congressional)
- [MI Senate District 38](/us/states/mi/districts/senate/38.md) — 79% (state senate)
- [MI House District 108](/us/states/mi/districts/house/108.md) — 79% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
