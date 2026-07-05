---
type: Jurisdiction
title: "Haakon County, SD"
classification: county
fips: "46055"
state: "SD"
demographics:
  population: 1722
  population_under_18: 350
  population_18_64: 871
  population_65_plus: 501
  median_household_income: 65625
  poverty_rate: 7.72
  homeownership_rate: 79.18
  unemployment_rate: 0.0
  median_home_value: 164200
  gini_index: 0.4245
  vacancy_rate: 23.24
  race_white: 1550
  race_black: 22
  race_asian: 0
  race_native: 108
  hispanic: 2
  bachelors_plus: 318
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/24"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/sd/districts/house/24"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Haakon County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1722 |
| Under 18 | 350 |
| 18–64 | 871 |
| 65+ | 501 |
| Median household income | 65625 |
| Poverty rate | 7.72 |
| Homeownership rate | 79.18 |
| Unemployment rate | 0.0 |
| Median home value | 164200 |
| Gini index | 0.4245 |
| Vacancy rate | 23.24 |
| White | 1550 |
| Black | 22 |
| Asian | 0 |
| Native | 108 |
| Hispanic/Latino | 2 |
| Bachelor's or higher | 318 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 24](/us/states/sd/districts/senate/24.md) — 100% (state senate)
- [SD House District 24](/us/states/sd/districts/house/24.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
