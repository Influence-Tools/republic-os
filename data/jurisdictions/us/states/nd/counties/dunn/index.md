---
type: Jurisdiction
title: "Dunn County, ND"
classification: county
fips: "38025"
state: "ND"
demographics:
  population: 4040
  population_under_18: 1053
  population_18_64: 2201
  population_65_plus: 786
  median_household_income: 97689
  poverty_rate: 7.4
  homeownership_rate: 74.35
  unemployment_rate: 3.42
  median_home_value: 275000
  gini_index: 0.488
  vacancy_rate: 24.76
  race_white: 3244
  race_black: 9
  race_asian: 38
  race_native: 384
  hispanic: 182
  bachelors_plus: 924
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/senate/26"
    rel: in-district
    area_weight: 0.59
  - to: "us/states/nd/districts/senate/4"
    rel: in-district
    area_weight: 0.2018
  - to: "us/states/nd/districts/senate/39"
    rel: in-district
    area_weight: 0.1853
  - to: "us/states/nd/districts/senate/36"
    rel: in-district
    area_weight: 0.0229
  - to: "us/states/nd/districts/house/26"
    rel: in-district
    area_weight: 0.59
  - to: "us/states/nd/districts/house/4a"
    rel: in-district
    area_weight: 0.2018
  - to: "us/states/nd/districts/house/39"
    rel: in-district
    area_weight: 0.1853
  - to: "us/states/nd/districts/house/36"
    rel: in-district
    area_weight: 0.0229
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Dunn County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4040 |
| Under 18 | 1053 |
| 18–64 | 2201 |
| 65+ | 786 |
| Median household income | 97689 |
| Poverty rate | 7.4 |
| Homeownership rate | 74.35 |
| Unemployment rate | 3.42 |
| Median home value | 275000 |
| Gini index | 0.488 |
| Vacancy rate | 24.76 |
| White | 3244 |
| Black | 9 |
| Asian | 38 |
| Native | 384 |
| Hispanic/Latino | 182 |
| Bachelor's or higher | 924 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 26](/us/states/nd/districts/senate/26.md) — 59% (state senate)
- [ND Senate District 4](/us/states/nd/districts/senate/4.md) — 20% (state senate)
- [ND Senate District 39](/us/states/nd/districts/senate/39.md) — 19% (state senate)
- [ND Senate District 36](/us/states/nd/districts/senate/36.md) — 2% (state senate)
- [ND House District 26](/us/states/nd/districts/house/26.md) — 59% (state house)
- [ND House District 4A](/us/states/nd/districts/house/4a.md) — 20% (state house)
- [ND House District 39](/us/states/nd/districts/house/39.md) — 19% (state house)
- [ND House District 36](/us/states/nd/districts/house/36.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
