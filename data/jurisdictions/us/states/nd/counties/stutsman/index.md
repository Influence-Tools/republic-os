---
type: Jurisdiction
title: "Stutsman County, ND"
classification: county
fips: "38093"
state: "ND"
demographics:
  population: 21549
  population_under_18: 4331
  population_18_64: 12816
  population_65_plus: 4402
  median_household_income: 61856
  poverty_rate: 12.61
  homeownership_rate: 63.06
  unemployment_rate: 3.99
  median_home_value: 208400
  gini_index: 0.4974
  vacancy_rate: 9.37
  race_white: 19542
  race_black: 558
  race_asian: 122
  race_native: 363
  hispanic: 696
  bachelors_plus: 4938
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/senate/29"
    rel: in-district
    area_weight: 0.8228
  - to: "us/states/nd/districts/senate/12"
    rel: in-district
    area_weight: 0.1771
  - to: "us/states/nd/districts/house/29"
    rel: in-district
    area_weight: 0.8228
  - to: "us/states/nd/districts/house/12"
    rel: in-district
    area_weight: 0.1771
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Stutsman County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21549 |
| Under 18 | 4331 |
| 18–64 | 12816 |
| 65+ | 4402 |
| Median household income | 61856 |
| Poverty rate | 12.61 |
| Homeownership rate | 63.06 |
| Unemployment rate | 3.99 |
| Median home value | 208400 |
| Gini index | 0.4974 |
| Vacancy rate | 9.37 |
| White | 19542 |
| Black | 558 |
| Asian | 122 |
| Native | 363 |
| Hispanic/Latino | 696 |
| Bachelor's or higher | 4938 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 29](/us/states/nd/districts/senate/29.md) — 82% (state senate)
- [ND Senate District 12](/us/states/nd/districts/senate/12.md) — 18% (state senate)
- [ND House District 29](/us/states/nd/districts/house/29.md) — 82% (state house)
- [ND House District 12](/us/states/nd/districts/house/12.md) — 18% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
