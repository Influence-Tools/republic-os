---
type: Jurisdiction
title: "Colleton County, SC"
classification: county
fips: "45029"
state: "SC"
demographics:
  population: 38783
  population_under_18: 8792
  population_18_64: 22062
  population_65_plus: 7929
  median_household_income: 51114
  poverty_rate: 19.58
  homeownership_rate: 73.29
  unemployment_rate: 9.87
  median_home_value: 162500
  gini_index: 0.465
  vacancy_rate: 18.3
  race_white: 22225
  race_black: 13094
  race_asian: 172
  race_native: 126
  hispanic: 1767
  bachelors_plus: 6303
districts:
  - to: "us/states/sc/districts/06"
    rel: in-district
    area_weight: 0.7718
  - to: "us/states/sc/districts/01"
    rel: in-district
    area_weight: 0.1776
  - to: "us/states/sc/districts/senate/45"
    rel: in-district
    area_weight: 0.4433
  - to: "us/states/sc/districts/senate/41"
    rel: in-district
    area_weight: 0.2136
  - to: "us/states/sc/districts/senate/40"
    rel: in-district
    area_weight: 0.2009
  - to: "us/states/sc/districts/senate/43"
    rel: in-district
    area_weight: 0.0916
  - to: "us/states/sc/districts/house/121"
    rel: in-district
    area_weight: 0.3699
  - to: "us/states/sc/districts/house/97"
    rel: in-district
    area_weight: 0.3105
  - to: "us/states/sc/districts/house/122"
    rel: in-district
    area_weight: 0.1432
  - to: "us/states/sc/districts/house/90"
    rel: in-district
    area_weight: 0.1199
  - to: "us/states/sc/districts/house/116"
    rel: in-district
    area_weight: 0.006
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Colleton County, SC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 38783 |
| Under 18 | 8792 |
| 18–64 | 22062 |
| 65+ | 7929 |
| Median household income | 51114 |
| Poverty rate | 19.58 |
| Homeownership rate | 73.29 |
| Unemployment rate | 9.87 |
| Median home value | 162500 |
| Gini index | 0.465 |
| Vacancy rate | 18.3 |
| White | 22225 |
| Black | 13094 |
| Asian | 172 |
| Native | 126 |
| Hispanic/Latino | 1767 |
| Bachelor's or higher | 6303 |

## Districts

- [SC-06](/us/states/sc/districts/06.md) — 77% (congressional)
- [SC-01](/us/states/sc/districts/01.md) — 18% (congressional)
- [SC Senate District 45](/us/states/sc/districts/senate/45.md) — 44% (state senate)
- [SC Senate District 41](/us/states/sc/districts/senate/41.md) — 21% (state senate)
- [SC Senate District 40](/us/states/sc/districts/senate/40.md) — 20% (state senate)
- [SC Senate District 43](/us/states/sc/districts/senate/43.md) — 9% (state senate)
- [SC House District 121](/us/states/sc/districts/house/121.md) — 37% (state house)
- [SC House District 97](/us/states/sc/districts/house/97.md) — 31% (state house)
- [SC House District 122](/us/states/sc/districts/house/122.md) — 14% (state house)
- [SC House District 90](/us/states/sc/districts/house/90.md) — 12% (state house)
- [SC House District 116](/us/states/sc/districts/house/116.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
