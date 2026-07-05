---
type: Jurisdiction
title: "Chicot County, AR"
classification: county
fips: "05017"
state: "AR"
demographics:
  population: 9765
  population_under_18: 2117
  population_18_64: 5469
  population_65_plus: 2179
  median_household_income: 39045
  poverty_rate: 22.64
  homeownership_rate: 69.23
  unemployment_rate: 9.06
  median_home_value: 89100
  gini_index: 0.5025
  vacancy_rate: 22.38
  race_white: 3942
  race_black: 5204
  race_asian: 20
  race_native: 13
  hispanic: 624
  bachelors_plus: 1549
districts:
  - to: "us/states/ar/districts/01"
    rel: in-district
    area_weight: 0.9949
  - to: "us/states/ar/districts/senate/1"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/ar/districts/house/95"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Chicot County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9765 |
| Under 18 | 2117 |
| 18–64 | 5469 |
| 65+ | 2179 |
| Median household income | 39045 |
| Poverty rate | 22.64 |
| Homeownership rate | 69.23 |
| Unemployment rate | 9.06 |
| Median home value | 89100 |
| Gini index | 0.5025 |
| Vacancy rate | 22.38 |
| White | 3942 |
| Black | 5204 |
| Asian | 20 |
| Native | 13 |
| Hispanic/Latino | 624 |
| Bachelor's or higher | 1549 |

## Districts

- [AR-01](/us/states/ar/districts/01.md) — 99% (congressional)
- [AR Senate District 1](/us/states/ar/districts/senate/1.md) — 100% (state senate)
- [AR House District 95](/us/states/ar/districts/house/95.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
