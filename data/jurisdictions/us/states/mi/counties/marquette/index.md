---
type: Jurisdiction
title: "Marquette County, MI"
classification: county
fips: "26103"
state: "MI"
demographics:
  population: 67112
  population_under_18: 11749
  population_18_64: 41729
  population_65_plus: 13634
  median_household_income: 65429
  poverty_rate: 13.95
  homeownership_rate: 69.65
  unemployment_rate: 4.62
  median_home_value: 216500
  gini_index: 0.428
  vacancy_rate: 15.93
  race_white: 61199
  race_black: 914
  race_asian: 340
  race_native: 708
  hispanic: 1414
  bachelors_plus: 21890
districts:
  - to: "us/states/mi/districts/01"
    rel: in-district
    area_weight: 0.5443
  - to: "us/states/mi/districts/senate/38"
    rel: in-district
    area_weight: 0.5439
  - to: "us/states/mi/districts/house/109"
    rel: in-district
    area_weight: 0.5438
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Marquette County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 67112 |
| Under 18 | 11749 |
| 18–64 | 41729 |
| 65+ | 13634 |
| Median household income | 65429 |
| Poverty rate | 13.95 |
| Homeownership rate | 69.65 |
| Unemployment rate | 4.62 |
| Median home value | 216500 |
| Gini index | 0.428 |
| Vacancy rate | 15.93 |
| White | 61199 |
| Black | 914 |
| Asian | 340 |
| Native | 708 |
| Hispanic/Latino | 1414 |
| Bachelor's or higher | 21890 |

## Districts

- [MI-01](/us/states/mi/districts/01.md) — 54% (congressional)
- [MI Senate District 38](/us/states/mi/districts/senate/38.md) — 54% (state senate)
- [MI House District 109](/us/states/mi/districts/house/109.md) — 54% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
