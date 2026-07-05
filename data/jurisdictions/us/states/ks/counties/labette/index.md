---
type: Jurisdiction
title: "Labette County, KS"
classification: county
fips: "20099"
state: "KS"
demographics:
  population: 19869
  population_under_18: 4838
  population_18_64: 10998
  population_65_plus: 4033
  median_household_income: 56325
  poverty_rate: 16.05
  homeownership_rate: 74.0
  unemployment_rate: 3.1
  median_home_value: 94600
  gini_index: 0.4308
  vacancy_rate: 15.06
  race_white: 16747
  race_black: 658
  race_asian: 2
  race_native: 186
  hispanic: 1010
  bachelors_plus: 3609
districts:
  - to: "us/states/ks/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/15"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/house/7"
    rel: in-district
    area_weight: 0.7431
  - to: "us/states/ks/districts/house/1"
    rel: in-district
    area_weight: 0.2567
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Labette County, KS

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19869 |
| Under 18 | 4838 |
| 18–64 | 10998 |
| 65+ | 4033 |
| Median household income | 56325 |
| Poverty rate | 16.05 |
| Homeownership rate | 74.0 |
| Unemployment rate | 3.1 |
| Median home value | 94600 |
| Gini index | 0.4308 |
| Vacancy rate | 15.06 |
| White | 16747 |
| Black | 658 |
| Asian | 2 |
| Native | 186 |
| Hispanic/Latino | 1010 |
| Bachelor's or higher | 3609 |

## Districts

- [KS-02](/us/states/ks/districts/02.md) — 100% (congressional)
- [KS Senate District 15](/us/states/ks/districts/senate/15.md) — 100% (state senate)
- [KS House District 7](/us/states/ks/districts/house/7.md) — 74% (state house)
- [KS House District 1](/us/states/ks/districts/house/1.md) — 26% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
