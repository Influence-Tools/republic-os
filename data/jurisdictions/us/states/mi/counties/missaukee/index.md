---
type: Jurisdiction
title: "Missaukee County, MI"
classification: county
fips: "26113"
state: "MI"
demographics:
  population: 15207
  population_under_18: 3382
  population_18_64: 8484
  population_65_plus: 3341
  median_household_income: 66194
  poverty_rate: 11.27
  homeownership_rate: 84.87
  unemployment_rate: 6.74
  median_home_value: 170400
  gini_index: 0.4366
  vacancy_rate: 31.92
  race_white: 13946
  race_black: 44
  race_asian: 72
  race_native: 27
  hispanic: 521
  bachelors_plus: 2688
districts:
  - to: "us/states/mi/districts/01"
    rel: in-district
    area_weight: 0.9996
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

# Missaukee County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15207 |
| Under 18 | 3382 |
| 18–64 | 8484 |
| 65+ | 3341 |
| Median household income | 66194 |
| Poverty rate | 11.27 |
| Homeownership rate | 84.87 |
| Unemployment rate | 6.74 |
| Median home value | 170400 |
| Gini index | 0.4366 |
| Vacancy rate | 31.92 |
| White | 13946 |
| Black | 44 |
| Asian | 72 |
| Native | 27 |
| Hispanic/Latino | 521 |
| Bachelor's or higher | 2688 |

## Districts

- [MI-01](/us/states/mi/districts/01.md) — 100% (congressional)
- [MI Senate District 36](/us/states/mi/districts/senate/36.md) — 100% (state senate)
- [MI House District 105](/us/states/mi/districts/house/105.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
