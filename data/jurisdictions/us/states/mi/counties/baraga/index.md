---
type: Jurisdiction
title: "Baraga County, MI"
classification: county
fips: "26013"
state: "MI"
demographics:
  population: 8191
  population_under_18: 1394
  population_18_64: 4896
  population_65_plus: 1901
  median_household_income: 55327
  poverty_rate: 15.23
  homeownership_rate: 78.5
  unemployment_rate: 5.14
  median_home_value: 138100
  gini_index: 0.4354
  vacancy_rate: 32.03
  race_white: 5950
  race_black: 513
  race_asian: 65
  race_native: 981
  hispanic: 143
  bachelors_plus: 1261
districts:
  - to: "us/states/mi/districts/01"
    rel: in-district
    area_weight: 0.8558
  - to: "us/states/mi/districts/senate/38"
    rel: in-district
    area_weight: 0.8579
  - to: "us/states/mi/districts/house/109"
    rel: in-district
    area_weight: 0.8578
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Baraga County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8191 |
| Under 18 | 1394 |
| 18–64 | 4896 |
| 65+ | 1901 |
| Median household income | 55327 |
| Poverty rate | 15.23 |
| Homeownership rate | 78.5 |
| Unemployment rate | 5.14 |
| Median home value | 138100 |
| Gini index | 0.4354 |
| Vacancy rate | 32.03 |
| White | 5950 |
| Black | 513 |
| Asian | 65 |
| Native | 981 |
| Hispanic/Latino | 143 |
| Bachelor's or higher | 1261 |

## Districts

- [MI-01](/us/states/mi/districts/01.md) — 86% (congressional)
- [MI Senate District 38](/us/states/mi/districts/senate/38.md) — 86% (state senate)
- [MI House District 109](/us/states/mi/districts/house/109.md) — 86% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
