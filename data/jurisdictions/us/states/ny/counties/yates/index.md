---
type: Jurisdiction
title: "Yates County, NY"
classification: county
fips: "36123"
state: "NY"
demographics:
  population: 24526
  population_under_18: 5445
  population_18_64: 13538
  population_65_plus: 5543
  median_household_income: 69701
  poverty_rate: 12.74
  homeownership_rate: 77.2
  unemployment_rate: 3.14
  median_home_value: 184700
  gini_index: 0.4663
  vacancy_rate: 28.17
  race_white: 23137
  race_black: 201
  race_asian: 215
  race_native: 13
  hispanic: 637
  bachelors_plus: 6209
districts:
  - to: "us/states/ny/districts/24"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ny/districts/senate/58"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ny/districts/house/132"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Yates County, NY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 24526 |
| Under 18 | 5445 |
| 18–64 | 13538 |
| 65+ | 5543 |
| Median household income | 69701 |
| Poverty rate | 12.74 |
| Homeownership rate | 77.2 |
| Unemployment rate | 3.14 |
| Median home value | 184700 |
| Gini index | 0.4663 |
| Vacancy rate | 28.17 |
| White | 23137 |
| Black | 201 |
| Asian | 215 |
| Native | 13 |
| Hispanic/Latino | 637 |
| Bachelor's or higher | 6209 |

## Districts

- [NY-24](/us/states/ny/districts/24.md) — 100% (congressional)
- [NY Senate District 58](/us/states/ny/districts/senate/58.md) — 100% (state senate)
- [NY House District 132](/us/states/ny/districts/house/132.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
