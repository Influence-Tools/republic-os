---
type: Jurisdiction
title: "McPherson County, SD"
classification: county
fips: "46089"
state: "SD"
demographics:
  population: 2145
  population_under_18: 430
  population_18_64: 530
  population_65_plus: 1185
  median_household_income: 66906
  poverty_rate: 12.86
  homeownership_rate: 81.31
  unemployment_rate: 1.08
  median_home_value: 85600
  gini_index: 0.5256
  vacancy_rate: 24.07
  race_white: 2076
  race_black: 0
  race_asian: 0
  race_native: 3
  hispanic: 3
  bachelors_plus: 488
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/23"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/sd/districts/house/23"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# McPherson County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2145 |
| Under 18 | 430 |
| 18–64 | 530 |
| 65+ | 1185 |
| Median household income | 66906 |
| Poverty rate | 12.86 |
| Homeownership rate | 81.31 |
| Unemployment rate | 1.08 |
| Median home value | 85600 |
| Gini index | 0.5256 |
| Vacancy rate | 24.07 |
| White | 2076 |
| Black | 0 |
| Asian | 0 |
| Native | 3 |
| Hispanic/Latino | 3 |
| Bachelor's or higher | 488 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 23](/us/states/sd/districts/senate/23.md) — 100% (state senate)
- [SD House District 23](/us/states/sd/districts/house/23.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
