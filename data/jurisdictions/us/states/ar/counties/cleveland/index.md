---
type: Jurisdiction
title: "Cleveland County, AR"
classification: county
fips: "05025"
state: "AR"
demographics:
  population: 7453
  population_under_18: 1595
  population_18_64: 4278
  population_65_plus: 1580
  median_household_income: 54794
  poverty_rate: 15.78
  homeownership_rate: 82.63
  unemployment_rate: 2.18
  median_home_value: 137600
  gini_index: 0.4834
  vacancy_rate: 18.29
  race_white: 6231
  race_black: 935
  race_asian: 24
  race_native: 0
  hispanic: 108
  bachelors_plus: 1367
districts:
  - to: "us/states/ar/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ar/districts/senate/1"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ar/districts/house/96"
    rel: in-district
    area_weight: 0.6362
  - to: "us/states/ar/districts/house/93"
    rel: in-district
    area_weight: 0.3638
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Cleveland County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7453 |
| Under 18 | 1595 |
| 18–64 | 4278 |
| 65+ | 1580 |
| Median household income | 54794 |
| Poverty rate | 15.78 |
| Homeownership rate | 82.63 |
| Unemployment rate | 2.18 |
| Median home value | 137600 |
| Gini index | 0.4834 |
| Vacancy rate | 18.29 |
| White | 6231 |
| Black | 935 |
| Asian | 24 |
| Native | 0 |
| Hispanic/Latino | 108 |
| Bachelor's or higher | 1367 |

## Districts

- [AR-04](/us/states/ar/districts/04.md) — 100% (congressional)
- [AR Senate District 1](/us/states/ar/districts/senate/1.md) — 100% (state senate)
- [AR House District 96](/us/states/ar/districts/house/96.md) — 64% (state house)
- [AR House District 93](/us/states/ar/districts/house/93.md) — 36% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
