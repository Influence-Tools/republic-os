---
type: Jurisdiction
title: "Schoolcraft County, MI"
classification: county
fips: "26153"
state: "MI"
demographics:
  population: 8128
  population_under_18: 1437
  population_18_64: 4339
  population_65_plus: 2352
  median_household_income: 56782
  poverty_rate: 14.06
  homeownership_rate: 86.63
  unemployment_rate: 6.2
  median_home_value: 141800
  gini_index: 0.4582
  vacancy_rate: 34.69
  race_white: 6643
  race_black: 48
  race_asian: 19
  race_native: 593
  hispanic: 135
  bachelors_plus: 1749
districts:
  - to: "us/states/mi/districts/01"
    rel: in-district
    area_weight: 0.6502
  - to: "us/states/mi/districts/senate/38"
    rel: in-district
    area_weight: 0.6503
  - to: "us/states/mi/districts/house/108"
    rel: in-district
    area_weight: 0.6501
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Schoolcraft County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8128 |
| Under 18 | 1437 |
| 18–64 | 4339 |
| 65+ | 2352 |
| Median household income | 56782 |
| Poverty rate | 14.06 |
| Homeownership rate | 86.63 |
| Unemployment rate | 6.2 |
| Median home value | 141800 |
| Gini index | 0.4582 |
| Vacancy rate | 34.69 |
| White | 6643 |
| Black | 48 |
| Asian | 19 |
| Native | 593 |
| Hispanic/Latino | 135 |
| Bachelor's or higher | 1749 |

## Districts

- [MI-01](/us/states/mi/districts/01.md) — 65% (congressional)
- [MI Senate District 38](/us/states/mi/districts/senate/38.md) — 65% (state senate)
- [MI House District 108](/us/states/mi/districts/house/108.md) — 65% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
