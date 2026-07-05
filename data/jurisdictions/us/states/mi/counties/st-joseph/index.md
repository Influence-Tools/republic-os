---
type: Jurisdiction
title: "St. Joseph County, MI"
classification: county
fips: "26149"
state: "MI"
demographics:
  population: 60969
  population_under_18: 14801
  population_18_64: 34765
  population_65_plus: 11403
  median_household_income: 66425
  poverty_rate: 11.41
  homeownership_rate: 76.12
  unemployment_rate: 5.9
  median_home_value: 178300
  gini_index: 0.4063
  vacancy_rate: 13.49
  race_white: 51897
  race_black: 1296
  race_asian: 397
  race_native: 209
  hispanic: 5739
  bachelors_plus: 9548
districts:
  - to: "us/states/mi/districts/05"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mi/districts/senate/17"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mi/districts/house/36"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# St. Joseph County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 60969 |
| Under 18 | 14801 |
| 18–64 | 34765 |
| 65+ | 11403 |
| Median household income | 66425 |
| Poverty rate | 11.41 |
| Homeownership rate | 76.12 |
| Unemployment rate | 5.9 |
| Median home value | 178300 |
| Gini index | 0.4063 |
| Vacancy rate | 13.49 |
| White | 51897 |
| Black | 1296 |
| Asian | 397 |
| Native | 209 |
| Hispanic/Latino | 5739 |
| Bachelor's or higher | 9548 |

## Districts

- [MI-05](/us/states/mi/districts/05.md) — 100% (congressional)
- [MI Senate District 17](/us/states/mi/districts/senate/17.md) — 100% (state senate)
- [MI House District 36](/us/states/mi/districts/house/36.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
