---
type: Jurisdiction
title: "Ellsworth County, KS"
classification: county
fips: "20053"
state: "KS"
demographics:
  population: 6360
  population_under_18: 1122
  population_18_64: 3740
  population_65_plus: 1498
  median_household_income: 65560
  poverty_rate: 10.37
  homeownership_rate: 80.23
  unemployment_rate: 2.56
  median_home_value: 114900
  gini_index: 0.4659
  vacancy_rate: 21.55
  race_white: 5435
  race_black: 219
  race_asian: 29
  race_native: 10
  hispanic: 387
  bachelors_plus: 1506
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/33"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/house/109"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Ellsworth County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6360 |
| Under 18 | 1122 |
| 18–64 | 3740 |
| 65+ | 1498 |
| Median household income | 65560 |
| Poverty rate | 10.37 |
| Homeownership rate | 80.23 |
| Unemployment rate | 2.56 |
| Median home value | 114900 |
| Gini index | 0.4659 |
| Vacancy rate | 21.55 |
| White | 5435 |
| Black | 219 |
| Asian | 29 |
| Native | 10 |
| Hispanic/Latino | 387 |
| Bachelor's or higher | 1506 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 33](/us/states/ks/districts/senate/33.md) — 100% (state senate)
- [KS House District 109](/us/states/ks/districts/house/109.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
