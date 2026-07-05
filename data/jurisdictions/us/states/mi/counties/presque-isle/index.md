---
type: Jurisdiction
title: "Presque Isle County, MI"
classification: county
fips: "26141"
state: "MI"
demographics:
  population: 13209
  population_under_18: 2033
  population_18_64: 6726
  population_65_plus: 4450
  median_household_income: 59321
  poverty_rate: 13.96
  homeownership_rate: 88.73
  unemployment_rate: 6.53
  median_home_value: 151300
  gini_index: 0.4385
  vacancy_rate: 32.11
  race_white: 12521
  race_black: 48
  race_asian: 30
  race_native: 32
  hispanic: 213
  bachelors_plus: 2952
districts:
  - to: "us/states/mi/districts/01"
    rel: in-district
    area_weight: 0.2658
  - to: "us/states/mi/districts/senate/36"
    rel: in-district
    area_weight: 0.2655
  - to: "us/states/mi/districts/house/106"
    rel: in-district
    area_weight: 0.2655
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Presque Isle County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13209 |
| Under 18 | 2033 |
| 18–64 | 6726 |
| 65+ | 4450 |
| Median household income | 59321 |
| Poverty rate | 13.96 |
| Homeownership rate | 88.73 |
| Unemployment rate | 6.53 |
| Median home value | 151300 |
| Gini index | 0.4385 |
| Vacancy rate | 32.11 |
| White | 12521 |
| Black | 48 |
| Asian | 30 |
| Native | 32 |
| Hispanic/Latino | 213 |
| Bachelor's or higher | 2952 |

## Districts

- [MI-01](/us/states/mi/districts/01.md) — 27% (congressional)
- [MI Senate District 36](/us/states/mi/districts/senate/36.md) — 27% (state senate)
- [MI House District 106](/us/states/mi/districts/house/106.md) — 27% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
