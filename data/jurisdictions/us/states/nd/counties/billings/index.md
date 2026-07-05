---
type: Jurisdiction
title: "Billings County, ND"
classification: county
fips: "38007"
state: "ND"
demographics:
  population: 1024
  population_under_18: 188
  population_18_64: 561
  population_65_plus: 275
  median_household_income: 86806
  poverty_rate: 10.81
  homeownership_rate: 77.89
  unemployment_rate: 2.09
  median_home_value: 331000
  gini_index: 0.4109
  vacancy_rate: 25.46
  race_white: 971
  race_black: 0
  race_asian: 0
  race_native: 40
  hispanic: 40
  bachelors_plus: 328
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/senate/39"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nd/districts/house/39"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Billings County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1024 |
| Under 18 | 188 |
| 18–64 | 561 |
| 65+ | 275 |
| Median household income | 86806 |
| Poverty rate | 10.81 |
| Homeownership rate | 77.89 |
| Unemployment rate | 2.09 |
| Median home value | 331000 |
| Gini index | 0.4109 |
| Vacancy rate | 25.46 |
| White | 971 |
| Black | 0 |
| Asian | 0 |
| Native | 40 |
| Hispanic/Latino | 40 |
| Bachelor's or higher | 328 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 39](/us/states/nd/districts/senate/39.md) — 100% (state senate)
- [ND House District 39](/us/states/nd/districts/house/39.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
