---
type: Jurisdiction
title: "Ramsey County, ND"
classification: county
fips: "38071"
state: "ND"
demographics:
  population: 11556
  population_under_18: 2681
  population_18_64: 6287
  population_65_plus: 2588
  median_household_income: 61006
  poverty_rate: 15.19
  homeownership_rate: 54.53
  unemployment_rate: 1.24
  median_home_value: 199300
  gini_index: 0.4762
  vacancy_rate: 7.87
  race_white: 9415
  race_black: 114
  race_asian: 99
  race_native: 1105
  hispanic: 328
  bachelors_plus: 2506
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/senate/15"
    rel: in-district
    area_weight: 0.9973
  - to: "us/states/nd/districts/house/15"
    rel: in-district
    area_weight: 0.9973
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Ramsey County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11556 |
| Under 18 | 2681 |
| 18–64 | 6287 |
| 65+ | 2588 |
| Median household income | 61006 |
| Poverty rate | 15.19 |
| Homeownership rate | 54.53 |
| Unemployment rate | 1.24 |
| Median home value | 199300 |
| Gini index | 0.4762 |
| Vacancy rate | 7.87 |
| White | 9415 |
| Black | 114 |
| Asian | 99 |
| Native | 1105 |
| Hispanic/Latino | 328 |
| Bachelor's or higher | 2506 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 15](/us/states/nd/districts/senate/15.md) — 100% (state senate)
- [ND House District 15](/us/states/nd/districts/house/15.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
