---
type: Jurisdiction
title: "Plumas County, CA"
classification: county
fips: "06063"
state: "CA"
demographics:
  population: 19423
  population_under_18: 3336
  population_18_64: 9973
  population_65_plus: 6114
  median_household_income: 66031
  poverty_rate: 10.6
  homeownership_rate: 74.57
  unemployment_rate: 9.15
  median_home_value: 360200
  gini_index: 0.4863
  vacancy_rate: 46.02
  race_white: 16266
  race_black: 315
  race_asian: 196
  race_native: 549
  hispanic: 1998
  bachelors_plus: 4673
districts:
  - to: "us/states/ca/districts/03"
    rel: in-district
    area_weight: 0.9976
  - to: "us/states/ca/districts/senate/1"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ca/districts/house/1"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Plumas County, CA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19423 |
| Under 18 | 3336 |
| 18–64 | 9973 |
| 65+ | 6114 |
| Median household income | 66031 |
| Poverty rate | 10.6 |
| Homeownership rate | 74.57 |
| Unemployment rate | 9.15 |
| Median home value | 360200 |
| Gini index | 0.4863 |
| Vacancy rate | 46.02 |
| White | 16266 |
| Black | 315 |
| Asian | 196 |
| Native | 549 |
| Hispanic/Latino | 1998 |
| Bachelor's or higher | 4673 |

## Districts

- [CA-03](/us/states/ca/districts/03.md) — 100% (congressional)
- [CA Senate District 1](/us/states/ca/districts/senate/1.md) — 100% (state senate)
- [CA House District 1](/us/states/ca/districts/house/1.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
