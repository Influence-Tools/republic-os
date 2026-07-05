---
type: Jurisdiction
title: "Adams County, ND"
classification: county
fips: "38001"
state: "ND"
demographics:
  population: 2145
  population_under_18: 485
  population_18_64: 1086
  population_65_plus: 574
  median_household_income: 62500
  poverty_rate: 14.79
  homeownership_rate: 71.84
  unemployment_rate: 2.23
  median_home_value: 113200
  gini_index: 0.4491
  vacancy_rate: 22.32
  race_white: 1858
  race_black: 14
  race_asian: 41
  race_native: 20
  hispanic: 99
  bachelors_plus: 482
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/nd/districts/senate/39"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/nd/districts/house/39"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Adams County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2145 |
| Under 18 | 485 |
| 18–64 | 1086 |
| 65+ | 574 |
| Median household income | 62500 |
| Poverty rate | 14.79 |
| Homeownership rate | 71.84 |
| Unemployment rate | 2.23 |
| Median home value | 113200 |
| Gini index | 0.4491 |
| Vacancy rate | 22.32 |
| White | 1858 |
| Black | 14 |
| Asian | 41 |
| Native | 20 |
| Hispanic/Latino | 99 |
| Bachelor's or higher | 482 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 39](/us/states/nd/districts/senate/39.md) — 100% (state senate)
- [ND House District 39](/us/states/nd/districts/house/39.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
