---
type: Jurisdiction
title: "Leavenworth County, KS"
classification: county
fips: "20103"
state: "KS"
demographics:
  population: 83123
  population_under_18: 19651
  population_18_64: 50105
  population_65_plus: 13367
  median_household_income: 89218
  poverty_rate: 8.77
  homeownership_rate: 69.32
  unemployment_rate: 4.08
  median_home_value: 282900
  gini_index: 0.4177
  vacancy_rate: 5.34
  race_white: 66146
  race_black: 5844
  race_asian: 1177
  race_native: 304
  hispanic: 6278
  bachelors_plus: 29225
districts:
  - to: "us/states/ks/districts/02"
    rel: in-district
    area_weight: 0.997
  - to: "us/states/ks/districts/senate/9"
    rel: in-district
    area_weight: 0.4292
  - to: "us/states/ks/districts/senate/1"
    rel: in-district
    area_weight: 0.3891
  - to: "us/states/ks/districts/senate/5"
    rel: in-district
    area_weight: 0.1812
  - to: "us/states/ks/districts/house/42"
    rel: in-district
    area_weight: 0.4708
  - to: "us/states/ks/districts/house/38"
    rel: in-district
    area_weight: 0.2949
  - to: "us/states/ks/districts/house/41"
    rel: in-district
    area_weight: 0.1388
  - to: "us/states/ks/districts/house/40"
    rel: in-district
    area_weight: 0.0949
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Leavenworth County, KS

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 83123 |
| Under 18 | 19651 |
| 18–64 | 50105 |
| 65+ | 13367 |
| Median household income | 89218 |
| Poverty rate | 8.77 |
| Homeownership rate | 69.32 |
| Unemployment rate | 4.08 |
| Median home value | 282900 |
| Gini index | 0.4177 |
| Vacancy rate | 5.34 |
| White | 66146 |
| Black | 5844 |
| Asian | 1177 |
| Native | 304 |
| Hispanic/Latino | 6278 |
| Bachelor's or higher | 29225 |

## Districts

- [KS-02](/us/states/ks/districts/02.md) — 100% (congressional)
- [KS Senate District 9](/us/states/ks/districts/senate/9.md) — 43% (state senate)
- [KS Senate District 1](/us/states/ks/districts/senate/1.md) — 39% (state senate)
- [KS Senate District 5](/us/states/ks/districts/senate/5.md) — 18% (state senate)
- [KS House District 42](/us/states/ks/districts/house/42.md) — 47% (state house)
- [KS House District 38](/us/states/ks/districts/house/38.md) — 29% (state house)
- [KS House District 41](/us/states/ks/districts/house/41.md) — 14% (state house)
- [KS House District 40](/us/states/ks/districts/house/40.md) — 9% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
