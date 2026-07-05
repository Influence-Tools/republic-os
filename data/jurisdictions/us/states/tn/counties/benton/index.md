---
type: Jurisdiction
title: "Benton County, TN"
classification: county
fips: "47005"
state: "TN"
demographics:
  population: 16006
  population_under_18: 3513
  population_18_64: 4024
  population_65_plus: 8469
  median_household_income: 51746
  poverty_rate: 17.85
  homeownership_rate: 75.14
  unemployment_rate: 5.29
  median_home_value: 153600
  gini_index: 0.4273
  vacancy_rate: 16.9
  race_white: 14473
  race_black: 233
  race_asian: 166
  race_native: 30
  hispanic: 454
  bachelors_plus: 2116
districts:
  - to: "us/states/tn/districts/07"
    rel: in-district
    area_weight: 0.8263
  - to: "us/states/tn/districts/08"
    rel: in-district
    area_weight: 0.1737
  - to: "us/states/tn/districts/senate/24"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tn/districts/house/74"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Benton County, TN

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16006 |
| Under 18 | 3513 |
| 18–64 | 4024 |
| 65+ | 8469 |
| Median household income | 51746 |
| Poverty rate | 17.85 |
| Homeownership rate | 75.14 |
| Unemployment rate | 5.29 |
| Median home value | 153600 |
| Gini index | 0.4273 |
| Vacancy rate | 16.9 |
| White | 14473 |
| Black | 233 |
| Asian | 166 |
| Native | 30 |
| Hispanic/Latino | 454 |
| Bachelor's or higher | 2116 |

## Districts

- [TN-07](/us/states/tn/districts/07.md) — 83% (congressional)
- [TN-08](/us/states/tn/districts/08.md) — 17% (congressional)
- [TN Senate District 24](/us/states/tn/districts/senate/24.md) — 100% (state senate)
- [TN House District 74](/us/states/tn/districts/house/74.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
