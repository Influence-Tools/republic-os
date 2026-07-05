---
type: Jurisdiction
title: "Jefferson County, AR"
classification: county
fips: "05069"
state: "AR"
demographics:
  population: 64802
  population_under_18: 13906
  population_18_64: 38845
  population_65_plus: 12051
  median_household_income: 51096
  poverty_rate: 18.55
  homeownership_rate: 61.79
  unemployment_rate: 8.13
  median_home_value: 113400
  gini_index: 0.4684
  vacancy_rate: 21.72
  race_white: 24047
  race_black: 36593
  race_asian: 500
  race_native: 238
  hispanic: 1735
  bachelors_plus: 11473
districts:
  - to: "us/states/ar/districts/04"
    rel: in-district
    area_weight: 0.9973
  - to: "us/states/ar/districts/senate/8"
    rel: in-district
    area_weight: 0.8581
  - to: "us/states/ar/districts/senate/1"
    rel: in-district
    area_weight: 0.1419
  - to: "us/states/ar/districts/house/65"
    rel: in-district
    area_weight: 0.5754
  - to: "us/states/ar/districts/house/93"
    rel: in-district
    area_weight: 0.2552
  - to: "us/states/ar/districts/house/64"
    rel: in-district
    area_weight: 0.1692
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Jefferson County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 64802 |
| Under 18 | 13906 |
| 18–64 | 38845 |
| 65+ | 12051 |
| Median household income | 51096 |
| Poverty rate | 18.55 |
| Homeownership rate | 61.79 |
| Unemployment rate | 8.13 |
| Median home value | 113400 |
| Gini index | 0.4684 |
| Vacancy rate | 21.72 |
| White | 24047 |
| Black | 36593 |
| Asian | 500 |
| Native | 238 |
| Hispanic/Latino | 1735 |
| Bachelor's or higher | 11473 |

## Districts

- [AR-04](/us/states/ar/districts/04.md) — 100% (congressional)
- [AR Senate District 8](/us/states/ar/districts/senate/8.md) — 86% (state senate)
- [AR Senate District 1](/us/states/ar/districts/senate/1.md) — 14% (state senate)
- [AR House District 65](/us/states/ar/districts/house/65.md) — 58% (state house)
- [AR House District 93](/us/states/ar/districts/house/93.md) — 26% (state house)
- [AR House District 64](/us/states/ar/districts/house/64.md) — 17% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
