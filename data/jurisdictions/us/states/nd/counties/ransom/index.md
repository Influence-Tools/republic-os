---
type: Jurisdiction
title: "Ransom County, ND"
classification: county
fips: "38073"
state: "ND"
demographics:
  population: 5643
  population_under_18: 1217
  population_18_64: 3180
  population_65_plus: 1246
  median_household_income: 75736
  poverty_rate: 10.36
  homeownership_rate: 74.67
  unemployment_rate: 2.88
  median_home_value: 193000
  gini_index: 0.4061
  vacancy_rate: 8.21
  race_white: 5195
  race_black: 64
  race_asian: 37
  race_native: 17
  hispanic: 155
  bachelors_plus: 1154
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/senate/24"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nd/districts/house/24"
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

# Ransom County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5643 |
| Under 18 | 1217 |
| 18–64 | 3180 |
| 65+ | 1246 |
| Median household income | 75736 |
| Poverty rate | 10.36 |
| Homeownership rate | 74.67 |
| Unemployment rate | 2.88 |
| Median home value | 193000 |
| Gini index | 0.4061 |
| Vacancy rate | 8.21 |
| White | 5195 |
| Black | 64 |
| Asian | 37 |
| Native | 17 |
| Hispanic/Latino | 155 |
| Bachelor's or higher | 1154 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 24](/us/states/nd/districts/senate/24.md) — 100% (state senate)
- [ND House District 24](/us/states/nd/districts/house/24.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
