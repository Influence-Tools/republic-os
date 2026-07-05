---
type: Jurisdiction
title: "Calhoun County, AR"
classification: county
fips: "05013"
state: "AR"
demographics:
  population: 4704
  population_under_18: 903
  population_18_64: 2683
  population_65_plus: 1118
  median_household_income: 66809
  poverty_rate: 10.17
  homeownership_rate: 87.81
  unemployment_rate: 5.59
  median_home_value: 110700
  gini_index: 0.3965
  vacancy_rate: 31.47
  race_white: 3458
  race_black: 809
  race_asian: 8
  race_native: 30
  hispanic: 140
  bachelors_plus: 926
districts:
  - to: "us/states/ar/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ar/districts/senate/2"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ar/districts/house/96"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Calhoun County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4704 |
| Under 18 | 903 |
| 18–64 | 2683 |
| 65+ | 1118 |
| Median household income | 66809 |
| Poverty rate | 10.17 |
| Homeownership rate | 87.81 |
| Unemployment rate | 5.59 |
| Median home value | 110700 |
| Gini index | 0.3965 |
| Vacancy rate | 31.47 |
| White | 3458 |
| Black | 809 |
| Asian | 8 |
| Native | 30 |
| Hispanic/Latino | 140 |
| Bachelor's or higher | 926 |

## Districts

- [AR-04](/us/states/ar/districts/04.md) — 100% (congressional)
- [AR Senate District 2](/us/states/ar/districts/senate/2.md) — 100% (state senate)
- [AR House District 96](/us/states/ar/districts/house/96.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
