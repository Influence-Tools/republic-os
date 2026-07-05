---
type: Jurisdiction
title: "Burleigh County, ND"
classification: county
fips: "38015"
state: "ND"
demographics:
  population: 100600
  population_under_18: 23364
  population_18_64: 59208
  population_65_plus: 18028
  median_household_income: 86851
  poverty_rate: 7.91
  homeownership_rate: 71.16
  unemployment_rate: 2.27
  median_home_value: 324000
  gini_index: 0.431
  vacancy_rate: 5.73
  race_white: 86404
  race_black: 2029
  race_asian: 991
  race_native: 3500
  hispanic: 3376
  bachelors_plus: 34715
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/senate/14"
    rel: in-district
    area_weight: 0.5802
  - to: "us/states/nd/districts/senate/8"
    rel: in-district
    area_weight: 0.3604
  - to: "us/states/nd/districts/senate/30"
    rel: in-district
    area_weight: 0.0317
  - to: "us/states/nd/districts/senate/7"
    rel: in-district
    area_weight: 0.0139
  - to: "us/states/nd/districts/senate/47"
    rel: in-district
    area_weight: 0.0075
  - to: "us/states/nd/districts/house/14"
    rel: in-district
    area_weight: 0.5802
  - to: "us/states/nd/districts/house/8"
    rel: in-district
    area_weight: 0.3604
  - to: "us/states/nd/districts/house/30"
    rel: in-district
    area_weight: 0.0317
  - to: "us/states/nd/districts/house/7"
    rel: in-district
    area_weight: 0.0139
  - to: "us/states/nd/districts/house/47"
    rel: in-district
    area_weight: 0.0075
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Burleigh County, ND

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 100600 |
| Under 18 | 23364 |
| 18–64 | 59208 |
| 65+ | 18028 |
| Median household income | 86851 |
| Poverty rate | 7.91 |
| Homeownership rate | 71.16 |
| Unemployment rate | 2.27 |
| Median home value | 324000 |
| Gini index | 0.431 |
| Vacancy rate | 5.73 |
| White | 86404 |
| Black | 2029 |
| Asian | 991 |
| Native | 3500 |
| Hispanic/Latino | 3376 |
| Bachelor's or higher | 34715 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 14](/us/states/nd/districts/senate/14.md) — 58% (state senate)
- [ND Senate District 8](/us/states/nd/districts/senate/8.md) — 36% (state senate)
- [ND Senate District 30](/us/states/nd/districts/senate/30.md) — 3% (state senate)
- [ND Senate District 7](/us/states/nd/districts/senate/7.md) — 1% (state senate)
- [ND Senate District 47](/us/states/nd/districts/senate/47.md) — 1% (state senate)
- [ND House District 14](/us/states/nd/districts/house/14.md) — 58% (state house)
- [ND House District 8](/us/states/nd/districts/house/8.md) — 36% (state house)
- [ND House District 30](/us/states/nd/districts/house/30.md) — 3% (state house)
- [ND House District 7](/us/states/nd/districts/house/7.md) — 1% (state house)
- [ND House District 47](/us/states/nd/districts/house/47.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
