---
type: Jurisdiction
title: "Marion County, KS"
classification: county
fips: "20115"
state: "KS"
demographics:
  population: 11754
  population_under_18: 2476
  population_18_64: 6494
  population_65_plus: 2784
  median_household_income: 64695
  poverty_rate: 9.15
  homeownership_rate: 81.31
  unemployment_rate: 3.43
  median_home_value: 124200
  gini_index: 0.4395
  vacancy_rate: 16.56
  race_white: 10893
  race_black: 113
  race_asian: 54
  race_native: 65
  hispanic: 494
  bachelors_plus: 3213
districts:
  - to: "us/states/ks/districts/02"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ks/districts/senate/14"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ks/districts/house/70"
    rel: in-district
    area_weight: 0.6609
  - to: "us/states/ks/districts/house/74"
    rel: in-district
    area_weight: 0.3389
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Marion County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11754 |
| Under 18 | 2476 |
| 18–64 | 6494 |
| 65+ | 2784 |
| Median household income | 64695 |
| Poverty rate | 9.15 |
| Homeownership rate | 81.31 |
| Unemployment rate | 3.43 |
| Median home value | 124200 |
| Gini index | 0.4395 |
| Vacancy rate | 16.56 |
| White | 10893 |
| Black | 113 |
| Asian | 54 |
| Native | 65 |
| Hispanic/Latino | 494 |
| Bachelor's or higher | 3213 |

## Districts

- [KS-02](/us/states/ks/districts/02.md) — 100% (congressional)
- [KS Senate District 14](/us/states/ks/districts/senate/14.md) — 100% (state senate)
- [KS House District 70](/us/states/ks/districts/house/70.md) — 66% (state house)
- [KS House District 74](/us/states/ks/districts/house/74.md) — 34% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
