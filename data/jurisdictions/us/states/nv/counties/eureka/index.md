---
type: Jurisdiction
title: "Eureka County, NV"
classification: county
fips: "32011"
state: "NV"
demographics:
  population: 1585
  population_under_18: 310
  population_18_64: 928
  population_65_plus: 347
  median_household_income: 70473
  poverty_rate: 24.89
  homeownership_rate: 82.96
  unemployment_rate: 0.0
  median_home_value: 82600
  gini_index: 0.3943
  vacancy_rate: 36.27
  race_white: 1323
  race_black: 2
  race_asian: 43
  race_native: 76
  hispanic: 86
  bachelors_plus: 252
districts:
  - to: "us/states/nv/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nv/districts/senate/19"
    rel: in-district
    area_weight: 0.8741
  - to: "us/states/nv/districts/senate/14"
    rel: in-district
    area_weight: 0.1259
  - to: "us/states/nv/districts/house/33"
    rel: in-district
    area_weight: 0.8741
  - to: "us/states/nv/districts/house/32"
    rel: in-district
    area_weight: 0.1259
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nv]
timestamp: "2026-07-03"
---

# Eureka County, NV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1585 |
| Under 18 | 310 |
| 18–64 | 928 |
| 65+ | 347 |
| Median household income | 70473 |
| Poverty rate | 24.89 |
| Homeownership rate | 82.96 |
| Unemployment rate | 0.0 |
| Median home value | 82600 |
| Gini index | 0.3943 |
| Vacancy rate | 36.27 |
| White | 1323 |
| Black | 2 |
| Asian | 43 |
| Native | 76 |
| Hispanic/Latino | 86 |
| Bachelor's or higher | 252 |

## Districts

- [NV-02](/us/states/nv/districts/02.md) — 100% (congressional)
- [NV Senate District 19](/us/states/nv/districts/senate/19.md) — 87% (state senate)
- [NV Senate District 14](/us/states/nv/districts/senate/14.md) — 13% (state senate)
- [NV House District 33](/us/states/nv/districts/house/33.md) — 87% (state house)
- [NV House District 32](/us/states/nv/districts/house/32.md) — 13% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
