---
type: Jurisdiction
title: "Hodgeman County, KS"
classification: county
fips: "20083"
state: "KS"
demographics:
  population: 1652
  population_under_18: 424
  population_18_64: 861
  population_65_plus: 367
  median_household_income: 59955
  poverty_rate: 6.33
  homeownership_rate: 79.05
  unemployment_rate: 0.63
  median_home_value: 101600
  gini_index: 0.4058
  vacancy_rate: 15.31
  race_white: 1565
  race_black: 6
  race_asian: 0
  race_native: 1
  hispanic: 76
  bachelors_plus: 436
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/38"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/house/122"
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

# Hodgeman County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1652 |
| Under 18 | 424 |
| 18–64 | 861 |
| 65+ | 367 |
| Median household income | 59955 |
| Poverty rate | 6.33 |
| Homeownership rate | 79.05 |
| Unemployment rate | 0.63 |
| Median home value | 101600 |
| Gini index | 0.4058 |
| Vacancy rate | 15.31 |
| White | 1565 |
| Black | 6 |
| Asian | 0 |
| Native | 1 |
| Hispanic/Latino | 76 |
| Bachelor's or higher | 436 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 38](/us/states/ks/districts/senate/38.md) — 100% (state senate)
- [KS House District 122](/us/states/ks/districts/house/122.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
