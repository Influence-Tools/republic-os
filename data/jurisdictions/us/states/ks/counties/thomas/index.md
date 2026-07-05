---
type: Jurisdiction
title: "Thomas County, KS"
classification: county
fips: "20193"
state: "KS"
demographics:
  population: 7885
  population_under_18: 1942
  population_18_64: 4475
  population_65_plus: 1468
  median_household_income: 71325
  poverty_rate: 6.49
  homeownership_rate: 75.25
  unemployment_rate: 0.57
  median_home_value: 172700
  gini_index: 0.4479
  vacancy_rate: 12.2
  race_white: 7069
  race_black: 82
  race_asian: 11
  race_native: 1
  hispanic: 662
  bachelors_plus: 2131
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/40"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/house/120"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Thomas County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7885 |
| Under 18 | 1942 |
| 18–64 | 4475 |
| 65+ | 1468 |
| Median household income | 71325 |
| Poverty rate | 6.49 |
| Homeownership rate | 75.25 |
| Unemployment rate | 0.57 |
| Median home value | 172700 |
| Gini index | 0.4479 |
| Vacancy rate | 12.2 |
| White | 7069 |
| Black | 82 |
| Asian | 11 |
| Native | 1 |
| Hispanic/Latino | 662 |
| Bachelor's or higher | 2131 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 40](/us/states/ks/districts/senate/40.md) — 100% (state senate)
- [KS House District 120](/us/states/ks/districts/house/120.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
