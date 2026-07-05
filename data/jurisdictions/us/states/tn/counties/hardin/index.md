---
type: Jurisdiction
title: "Hardin County, TN"
classification: county
fips: "47071"
state: "TN"
demographics:
  population: 27249
  population_under_18: 5487
  population_18_64: 15367
  population_65_plus: 6395
  median_household_income: 49956
  poverty_rate: 21.53
  homeownership_rate: 77.99
  unemployment_rate: 4.72
  median_home_value: 160400
  gini_index: 0.4778
  vacancy_rate: 27.44
  race_white: 25121
  race_black: 956
  race_asian: 8
  race_native: 33
  hispanic: 678
  bachelors_plus: 4025
districts:
  - to: "us/states/tn/districts/08"
    rel: in-district
    area_weight: 0.9976
  - to: "us/states/tn/districts/senate/26"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tn/districts/house/72"
    rel: in-district
    area_weight: 0.87
  - to: "us/states/tn/districts/house/71"
    rel: in-district
    area_weight: 0.1297
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Hardin County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 27249 |
| Under 18 | 5487 |
| 18–64 | 15367 |
| 65+ | 6395 |
| Median household income | 49956 |
| Poverty rate | 21.53 |
| Homeownership rate | 77.99 |
| Unemployment rate | 4.72 |
| Median home value | 160400 |
| Gini index | 0.4778 |
| Vacancy rate | 27.44 |
| White | 25121 |
| Black | 956 |
| Asian | 8 |
| Native | 33 |
| Hispanic/Latino | 678 |
| Bachelor's or higher | 4025 |

## Districts

- [TN-08](/us/states/tn/districts/08.md) — 100% (congressional)
- [TN Senate District 26](/us/states/tn/districts/senate/26.md) — 100% (state senate)
- [TN House District 72](/us/states/tn/districts/house/72.md) — 87% (state house)
- [TN House District 71](/us/states/tn/districts/house/71.md) — 13% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
