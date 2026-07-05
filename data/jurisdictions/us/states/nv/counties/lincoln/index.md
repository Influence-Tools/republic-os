---
type: Jurisdiction
title: "Lincoln County, NV"
classification: county
fips: "32017"
state: "NV"
demographics:
  population: 4405
  population_under_18: 883
  population_18_64: 2391
  population_65_plus: 1131
  median_household_income: 72307
  poverty_rate: 5.04
  homeownership_rate: 74.96
  unemployment_rate: 1.88
  median_home_value: 219500
  gini_index: 0.3685
  vacancy_rate: 30.51
  race_white: 3761
  race_black: 123
  race_asian: 2
  race_native: 155
  hispanic: 292
  bachelors_plus: 909
districts:
  - to: "us/states/nv/districts/04"
    rel: in-district
    area_weight: 0.9949
  - to: "us/states/nv/districts/senate/19"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nv/districts/house/33"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nv]
timestamp: "2026-07-03"
---

# Lincoln County, NV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4405 |
| Under 18 | 883 |
| 18–64 | 2391 |
| 65+ | 1131 |
| Median household income | 72307 |
| Poverty rate | 5.04 |
| Homeownership rate | 74.96 |
| Unemployment rate | 1.88 |
| Median home value | 219500 |
| Gini index | 0.3685 |
| Vacancy rate | 30.51 |
| White | 3761 |
| Black | 123 |
| Asian | 2 |
| Native | 155 |
| Hispanic/Latino | 292 |
| Bachelor's or higher | 909 |

## Districts

- [NV-04](/us/states/nv/districts/04.md) — 99% (congressional)
- [NV Senate District 19](/us/states/nv/districts/senate/19.md) — 100% (state senate)
- [NV House District 33](/us/states/nv/districts/house/33.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
