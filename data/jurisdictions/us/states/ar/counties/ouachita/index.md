---
type: Jurisdiction
title: "Ouachita County, AR"
classification: county
fips: "05103"
state: "AR"
demographics:
  population: 22085
  population_under_18: 4909
  population_18_64: 12457
  population_65_plus: 4719
  median_household_income: 49268
  poverty_rate: 18.87
  homeownership_rate: 70.93
  unemployment_rate: 5.16
  median_home_value: 102100
  gini_index: 0.462
  vacancy_rate: 27.34
  race_white: 12052
  race_black: 9010
  race_asian: 71
  race_native: 49
  hispanic: 575
  bachelors_plus: 3441
districts:
  - to: "us/states/ar/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ar/districts/senate/2"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ar/districts/house/98"
    rel: in-district
    area_weight: 0.7098
  - to: "us/states/ar/districts/house/96"
    rel: in-district
    area_weight: 0.2901
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Ouachita County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 22085 |
| Under 18 | 4909 |
| 18–64 | 12457 |
| 65+ | 4719 |
| Median household income | 49268 |
| Poverty rate | 18.87 |
| Homeownership rate | 70.93 |
| Unemployment rate | 5.16 |
| Median home value | 102100 |
| Gini index | 0.462 |
| Vacancy rate | 27.34 |
| White | 12052 |
| Black | 9010 |
| Asian | 71 |
| Native | 49 |
| Hispanic/Latino | 575 |
| Bachelor's or higher | 3441 |

## Districts

- [AR-04](/us/states/ar/districts/04.md) — 100% (congressional)
- [AR Senate District 2](/us/states/ar/districts/senate/2.md) — 100% (state senate)
- [AR House District 98](/us/states/ar/districts/house/98.md) — 71% (state house)
- [AR House District 96](/us/states/ar/districts/house/96.md) — 29% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
