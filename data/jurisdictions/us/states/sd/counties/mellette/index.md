---
type: Jurisdiction
title: "Mellette County, SD"
classification: county
fips: "46095"
state: "SD"
demographics:
  population: 1943
  population_under_18: 588
  population_18_64: 549
  population_65_plus: 806
  median_household_income: 54076
  poverty_rate: 41.74
  homeownership_rate: 60.37
  unemployment_rate: 12.47
  median_home_value: 84100
  gini_index: 0.5013
  vacancy_rate: 17.72
  race_white: 674
  race_black: 0
  race_asian: 0
  race_native: 1096
  hispanic: 17
  bachelors_plus: 310
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/26"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/sd/districts/house/26a"
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

# Mellette County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1943 |
| Under 18 | 588 |
| 18–64 | 549 |
| 65+ | 806 |
| Median household income | 54076 |
| Poverty rate | 41.74 |
| Homeownership rate | 60.37 |
| Unemployment rate | 12.47 |
| Median home value | 84100 |
| Gini index | 0.5013 |
| Vacancy rate | 17.72 |
| White | 674 |
| Black | 0 |
| Asian | 0 |
| Native | 1096 |
| Hispanic/Latino | 17 |
| Bachelor's or higher | 310 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 26](/us/states/sd/districts/senate/26.md) — 100% (state senate)
- [SD House District 26A](/us/states/sd/districts/house/26a.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
