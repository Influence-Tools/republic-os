---
type: Jurisdiction
title: "Day County, SD"
classification: county
fips: "46037"
state: "SD"
demographics:
  population: 5437
  population_under_18: 1217
  population_18_64: 2771
  population_65_plus: 1449
  median_household_income: 66033
  poverty_rate: 14.82
  homeownership_rate: 74.57
  unemployment_rate: 2.09
  median_home_value: 173600
  gini_index: 0.4578
  vacancy_rate: 31.08
  race_white: 4572
  race_black: 2
  race_asian: 4
  race_native: 534
  hispanic: 154
  bachelors_plus: 1088
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/1"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/house/1"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Day County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5437 |
| Under 18 | 1217 |
| 18–64 | 2771 |
| 65+ | 1449 |
| Median household income | 66033 |
| Poverty rate | 14.82 |
| Homeownership rate | 74.57 |
| Unemployment rate | 2.09 |
| Median home value | 173600 |
| Gini index | 0.4578 |
| Vacancy rate | 31.08 |
| White | 4572 |
| Black | 2 |
| Asian | 4 |
| Native | 534 |
| Hispanic/Latino | 154 |
| Bachelor's or higher | 1088 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 1](/us/states/sd/districts/senate/1.md) — 100% (state senate)
- [SD House District 1](/us/states/sd/districts/house/1.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
