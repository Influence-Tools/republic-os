---
type: Jurisdiction
title: "Crawford County, MI"
classification: county
fips: "26039"
state: "MI"
demographics:
  population: 13369
  population_under_18: 2334
  population_18_64: 7390
  population_65_plus: 3645
  median_household_income: 60392
  poverty_rate: 14.72
  homeownership_rate: 79.63
  unemployment_rate: 8.15
  median_home_value: 163000
  gini_index: 0.4018
  vacancy_rate: 39.68
  race_white: 12326
  race_black: 53
  race_asian: 111
  race_native: 32
  hispanic: 326
  bachelors_plus: 2968
districts:
  - to: "us/states/mi/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mi/districts/senate/36"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mi/districts/house/105"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Crawford County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13369 |
| Under 18 | 2334 |
| 18–64 | 7390 |
| 65+ | 3645 |
| Median household income | 60392 |
| Poverty rate | 14.72 |
| Homeownership rate | 79.63 |
| Unemployment rate | 8.15 |
| Median home value | 163000 |
| Gini index | 0.4018 |
| Vacancy rate | 39.68 |
| White | 12326 |
| Black | 53 |
| Asian | 111 |
| Native | 32 |
| Hispanic/Latino | 326 |
| Bachelor's or higher | 2968 |

## Districts

- [MI-01](/us/states/mi/districts/01.md) — 100% (congressional)
- [MI Senate District 36](/us/states/mi/districts/senate/36.md) — 100% (state senate)
- [MI House District 105](/us/states/mi/districts/house/105.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
