---
type: Jurisdiction
title: "Ashley County, AR"
classification: county
fips: "05003"
state: "AR"
demographics:
  population: 18429
  population_under_18: 4141
  population_18_64: 10325
  population_65_plus: 3963
  median_household_income: 44266
  poverty_rate: 22.15
  homeownership_rate: 70.83
  unemployment_rate: 5.48
  median_home_value: 91900
  gini_index: 0.4654
  vacancy_rate: 21.68
  race_white: 12681
  race_black: 4366
  race_asian: 0
  race_native: 39
  hispanic: 1176
  bachelors_plus: 2154
districts:
  - to: "us/states/ar/districts/04"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ar/districts/senate/1"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ar/districts/house/95"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Ashley County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18429 |
| Under 18 | 4141 |
| 18–64 | 10325 |
| 65+ | 3963 |
| Median household income | 44266 |
| Poverty rate | 22.15 |
| Homeownership rate | 70.83 |
| Unemployment rate | 5.48 |
| Median home value | 91900 |
| Gini index | 0.4654 |
| Vacancy rate | 21.68 |
| White | 12681 |
| Black | 4366 |
| Asian | 0 |
| Native | 39 |
| Hispanic/Latino | 1176 |
| Bachelor's or higher | 2154 |

## Districts

- [AR-04](/us/states/ar/districts/04.md) — 100% (congressional)
- [AR Senate District 1](/us/states/ar/districts/senate/1.md) — 100% (state senate)
- [AR House District 95](/us/states/ar/districts/house/95.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
