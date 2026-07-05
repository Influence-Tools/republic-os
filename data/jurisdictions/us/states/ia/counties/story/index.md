---
type: Jurisdiction
title: "Story County, IA"
classification: county
fips: "19169"
state: "IA"
demographics:
  population: 100466
  population_under_18: 16276
  population_18_64: 70915
  population_65_plus: 13275
  median_household_income: 69685
  poverty_rate: 18.24
  homeownership_rate: 55.52
  unemployment_rate: 4.76
  median_home_value: 258700
  gini_index: 0.469
  vacancy_rate: 7.12
  race_white: 82831
  race_black: 2796
  race_asian: 6641
  race_native: 465
  hispanic: 5184
  bachelors_plus: 41629
districts:
  - to: "us/states/ia/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/senate/26"
    rel: in-district
    area_weight: 0.7399
  - to: "us/states/ia/districts/senate/28"
    rel: in-district
    area_weight: 0.126
  - to: "us/states/ia/districts/senate/25"
    rel: in-district
    area_weight: 0.0927
  - to: "us/states/ia/districts/senate/24"
    rel: in-district
    area_weight: 0.0414
  - to: "us/states/ia/districts/house/51"
    rel: in-district
    area_weight: 0.7399
  - to: "us/states/ia/districts/house/55"
    rel: in-district
    area_weight: 0.126
  - to: "us/states/ia/districts/house/49"
    rel: in-district
    area_weight: 0.0757
  - to: "us/states/ia/districts/house/48"
    rel: in-district
    area_weight: 0.0414
  - to: "us/states/ia/districts/house/50"
    rel: in-district
    area_weight: 0.017
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Story County, IA

County jurisdiction — 8 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 100466 |
| Under 18 | 16276 |
| 18–64 | 70915 |
| 65+ | 13275 |
| Median household income | 69685 |
| Poverty rate | 18.24 |
| Homeownership rate | 55.52 |
| Unemployment rate | 4.76 |
| Median home value | 258700 |
| Gini index | 0.469 |
| Vacancy rate | 7.12 |
| White | 82831 |
| Black | 2796 |
| Asian | 6641 |
| Native | 465 |
| Hispanic/Latino | 5184 |
| Bachelor's or higher | 41629 |

## Districts

- [IA-04](/us/states/ia/districts/04.md) — 100% (congressional)
- [IA Senate District 26](/us/states/ia/districts/senate/26.md) — 74% (state senate)
- [IA Senate District 28](/us/states/ia/districts/senate/28.md) — 13% (state senate)
- [IA Senate District 25](/us/states/ia/districts/senate/25.md) — 9% (state senate)
- [IA Senate District 24](/us/states/ia/districts/senate/24.md) — 4% (state senate)
- [IA House District 51](/us/states/ia/districts/house/51.md) — 74% (state house)
- [IA House District 55](/us/states/ia/districts/house/55.md) — 13% (state house)
- [IA House District 49](/us/states/ia/districts/house/49.md) — 8% (state house)
- [IA House District 48](/us/states/ia/districts/house/48.md) — 4% (state house)
- [IA House District 50](/us/states/ia/districts/house/50.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
