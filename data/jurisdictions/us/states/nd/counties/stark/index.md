---
type: Jurisdiction
title: "Stark County, ND"
classification: county
fips: "38089"
state: "ND"
demographics:
  population: 33302
  population_under_18: 9201
  population_18_64: 19440
  population_65_plus: 4661
  median_household_income: 84449
  poverty_rate: 12.08
  homeownership_rate: 66.79
  unemployment_rate: 2.99
  median_home_value: 271700
  gini_index: 0.4232
  vacancy_rate: 12.74
  race_white: 28513
  race_black: 786
  race_asian: 374
  race_native: 315
  hispanic: 2429
  bachelors_plus: 7936
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/senate/39"
    rel: in-district
    area_weight: 0.5031
  - to: "us/states/nd/districts/senate/36"
    rel: in-district
    area_weight: 0.4905
  - to: "us/states/nd/districts/senate/37"
    rel: in-district
    area_weight: 0.0064
  - to: "us/states/nd/districts/house/39"
    rel: in-district
    area_weight: 0.5031
  - to: "us/states/nd/districts/house/36"
    rel: in-district
    area_weight: 0.4905
  - to: "us/states/nd/districts/house/37"
    rel: in-district
    area_weight: 0.0064
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Stark County, ND

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 33302 |
| Under 18 | 9201 |
| 18–64 | 19440 |
| 65+ | 4661 |
| Median household income | 84449 |
| Poverty rate | 12.08 |
| Homeownership rate | 66.79 |
| Unemployment rate | 2.99 |
| Median home value | 271700 |
| Gini index | 0.4232 |
| Vacancy rate | 12.74 |
| White | 28513 |
| Black | 786 |
| Asian | 374 |
| Native | 315 |
| Hispanic/Latino | 2429 |
| Bachelor's or higher | 7936 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 39](/us/states/nd/districts/senate/39.md) — 50% (state senate)
- [ND Senate District 36](/us/states/nd/districts/senate/36.md) — 49% (state senate)
- [ND Senate District 37](/us/states/nd/districts/senate/37.md) — 1% (state senate)
- [ND House District 39](/us/states/nd/districts/house/39.md) — 50% (state house)
- [ND House District 36](/us/states/nd/districts/house/36.md) — 49% (state house)
- [ND House District 37](/us/states/nd/districts/house/37.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
