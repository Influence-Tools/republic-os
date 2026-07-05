---
type: Jurisdiction
title: "Montgomery County, AR"
classification: county
fips: "05097"
state: "AR"
demographics:
  population: 8553
  population_under_18: 1601
  population_18_64: 4621
  population_65_plus: 2331
  median_household_income: 48906
  poverty_rate: 22.39
  homeownership_rate: 80.57
  unemployment_rate: 5.78
  median_home_value: 151900
  gini_index: 0.4631
  vacancy_rate: 32.27
  race_white: 7740
  race_black: 72
  race_asian: 81
  race_native: 113
  hispanic: 424
  bachelors_plus: 1406
districts:
  - to: "us/states/ar/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ar/districts/senate/5"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ar/districts/house/86"
    rel: in-district
    area_weight: 0.9992
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Montgomery County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8553 |
| Under 18 | 1601 |
| 18–64 | 4621 |
| 65+ | 2331 |
| Median household income | 48906 |
| Poverty rate | 22.39 |
| Homeownership rate | 80.57 |
| Unemployment rate | 5.78 |
| Median home value | 151900 |
| Gini index | 0.4631 |
| Vacancy rate | 32.27 |
| White | 7740 |
| Black | 72 |
| Asian | 81 |
| Native | 113 |
| Hispanic/Latino | 424 |
| Bachelor's or higher | 1406 |

## Districts

- [AR-04](/us/states/ar/districts/04.md) — 100% (congressional)
- [AR Senate District 5](/us/states/ar/districts/senate/5.md) — 100% (state senate)
- [AR House District 86](/us/states/ar/districts/house/86.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
