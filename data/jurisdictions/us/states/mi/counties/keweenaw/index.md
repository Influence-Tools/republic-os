---
type: Jurisdiction
title: "Keweenaw County, MI"
classification: county
fips: "26083"
state: "MI"
demographics:
  population: 2133
  population_under_18: 318
  population_18_64: 1036
  population_65_plus: 779
  median_household_income: 52583
  poverty_rate: 15.16
  homeownership_rate: 90.66
  unemployment_rate: 2.15
  median_home_value: 169800
  gini_index: 0.494
  vacancy_rate: 50.76
  race_white: 1981
  race_black: 0
  race_asian: 0
  race_native: 3
  hispanic: 42
  bachelors_plus: 1044
districts:
  - to: "us/states/mi/districts/01"
    rel: in-district
    area_weight: 0.0985
  - to: "us/states/mi/districts/senate/38"
    rel: in-district
    area_weight: 0.0981
  - to: "us/states/mi/districts/house/110"
    rel: in-district
    area_weight: 0.0981
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Keweenaw County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2133 |
| Under 18 | 318 |
| 18–64 | 1036 |
| 65+ | 779 |
| Median household income | 52583 |
| Poverty rate | 15.16 |
| Homeownership rate | 90.66 |
| Unemployment rate | 2.15 |
| Median home value | 169800 |
| Gini index | 0.494 |
| Vacancy rate | 50.76 |
| White | 1981 |
| Black | 0 |
| Asian | 0 |
| Native | 3 |
| Hispanic/Latino | 42 |
| Bachelor's or higher | 1044 |

## Districts

- [MI-01](/us/states/mi/districts/01.md) — 10% (congressional)
- [MI Senate District 38](/us/states/mi/districts/senate/38.md) — 10% (state senate)
- [MI House District 110](/us/states/mi/districts/house/110.md) — 10% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
