---
type: Jurisdiction
title: "Elko County, NV"
classification: county
fips: "32007"
state: "NV"
demographics:
  population: 54047
  population_under_18: 14286
  population_18_64: 32660
  population_65_plus: 7101
  median_household_income: 86487
  poverty_rate: 9.83
  homeownership_rate: 71.35
  unemployment_rate: 4.5
  median_home_value: 301400
  gini_index: 0.4152
  vacancy_rate: 11.5
  race_white: 35597
  race_black: 436
  race_asian: 802
  race_native: 2441
  hispanic: 14063
  bachelors_plus: 8410
districts:
  - to: "us/states/nv/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nv/districts/senate/19"
    rel: in-district
    area_weight: 0.7977
  - to: "us/states/nv/districts/senate/14"
    rel: in-district
    area_weight: 0.2022
  - to: "us/states/nv/districts/house/33"
    rel: in-district
    area_weight: 0.7977
  - to: "us/states/nv/districts/house/32"
    rel: in-district
    area_weight: 0.2022
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nv]
timestamp: "2026-07-03"
---

# Elko County, NV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 54047 |
| Under 18 | 14286 |
| 18–64 | 32660 |
| 65+ | 7101 |
| Median household income | 86487 |
| Poverty rate | 9.83 |
| Homeownership rate | 71.35 |
| Unemployment rate | 4.5 |
| Median home value | 301400 |
| Gini index | 0.4152 |
| Vacancy rate | 11.5 |
| White | 35597 |
| Black | 436 |
| Asian | 802 |
| Native | 2441 |
| Hispanic/Latino | 14063 |
| Bachelor's or higher | 8410 |

## Districts

- [NV-02](/us/states/nv/districts/02.md) — 100% (congressional)
- [NV Senate District 19](/us/states/nv/districts/senate/19.md) — 80% (state senate)
- [NV Senate District 14](/us/states/nv/districts/senate/14.md) — 20% (state senate)
- [NV House District 33](/us/states/nv/districts/house/33.md) — 80% (state house)
- [NV House District 32](/us/states/nv/districts/house/32.md) — 20% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
