---
type: Jurisdiction
title: "Cavalier County, ND"
classification: county
fips: "38019"
state: "ND"
demographics:
  population: 3633
  population_under_18: 797
  population_18_64: 1823
  population_65_plus: 1013
  median_household_income: 69531
  poverty_rate: 8.51
  homeownership_rate: 81.35
  unemployment_rate: 1.03
  median_home_value: 125800
  gini_index: 0.4967
  vacancy_rate: 26.03
  race_white: 3342
  race_black: 0
  race_asian: 26
  race_native: 24
  hispanic: 84
  bachelors_plus: 643
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/senate/15"
    rel: in-district
    area_weight: 0.7504
  - to: "us/states/nd/districts/senate/19"
    rel: in-district
    area_weight: 0.2496
  - to: "us/states/nd/districts/house/15"
    rel: in-district
    area_weight: 0.7504
  - to: "us/states/nd/districts/house/19"
    rel: in-district
    area_weight: 0.2496
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Cavalier County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3633 |
| Under 18 | 797 |
| 18–64 | 1823 |
| 65+ | 1013 |
| Median household income | 69531 |
| Poverty rate | 8.51 |
| Homeownership rate | 81.35 |
| Unemployment rate | 1.03 |
| Median home value | 125800 |
| Gini index | 0.4967 |
| Vacancy rate | 26.03 |
| White | 3342 |
| Black | 0 |
| Asian | 26 |
| Native | 24 |
| Hispanic/Latino | 84 |
| Bachelor's or higher | 643 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 15](/us/states/nd/districts/senate/15.md) — 75% (state senate)
- [ND Senate District 19](/us/states/nd/districts/senate/19.md) — 25% (state senate)
- [ND House District 15](/us/states/nd/districts/house/15.md) — 75% (state house)
- [ND House District 19](/us/states/nd/districts/house/19.md) — 25% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
