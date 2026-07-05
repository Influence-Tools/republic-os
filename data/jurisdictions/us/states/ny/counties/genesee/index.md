---
type: Jurisdiction
title: "Genesee County, NY"
classification: county
fips: "36037"
state: "NY"
demographics:
  population: 57787
  population_under_18: 11800
  population_18_64: 34270
  population_65_plus: 11717
  median_household_income: 73314
  poverty_rate: 10.64
  homeownership_rate: 73.78
  unemployment_rate: 4.58
  median_home_value: 170500
  gini_index: 0.4037
  vacancy_rate: 4.98
  race_white: 51363
  race_black: 1315
  race_asian: 384
  race_native: 185
  hispanic: 2802
  bachelors_plus: 14278
districts:
  - to: "us/states/ny/districts/24"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ny/districts/senate/57"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ny/districts/house/139"
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

# Genesee County, NY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 57787 |
| Under 18 | 11800 |
| 18–64 | 34270 |
| 65+ | 11717 |
| Median household income | 73314 |
| Poverty rate | 10.64 |
| Homeownership rate | 73.78 |
| Unemployment rate | 4.58 |
| Median home value | 170500 |
| Gini index | 0.4037 |
| Vacancy rate | 4.98 |
| White | 51363 |
| Black | 1315 |
| Asian | 384 |
| Native | 185 |
| Hispanic/Latino | 2802 |
| Bachelor's or higher | 14278 |

## Districts

- [NY-24](/us/states/ny/districts/24.md) — 100% (congressional)
- [NY Senate District 57](/us/states/ny/districts/senate/57.md) — 100% (state senate)
- [NY House District 139](/us/states/ny/districts/house/139.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
