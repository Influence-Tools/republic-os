---
type: Jurisdiction
title: "Corson County, SD"
classification: county
fips: "46031"
state: "SD"
demographics:
  population: 3806
  population_under_18: 1345
  population_18_64: 1960
  population_65_plus: 501
  median_household_income: 46406
  poverty_rate: 44.25
  homeownership_rate: 59.13
  unemployment_rate: 23.55
  median_home_value: 69800
  gini_index: 0.5318
  vacancy_rate: 17.0
  race_white: 1138
  race_black: 0
  race_asian: 0
  race_native: 2538
  hispanic: 20
  bachelors_plus: 478
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/sd/districts/senate/28"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/sd/districts/house/28a"
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

# Corson County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3806 |
| Under 18 | 1345 |
| 18–64 | 1960 |
| 65+ | 501 |
| Median household income | 46406 |
| Poverty rate | 44.25 |
| Homeownership rate | 59.13 |
| Unemployment rate | 23.55 |
| Median home value | 69800 |
| Gini index | 0.5318 |
| Vacancy rate | 17.0 |
| White | 1138 |
| Black | 0 |
| Asian | 0 |
| Native | 2538 |
| Hispanic/Latino | 20 |
| Bachelor's or higher | 478 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 28](/us/states/sd/districts/senate/28.md) — 100% (state senate)
- [SD House District 28A](/us/states/sd/districts/house/28a.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
