---
type: Jurisdiction
title: "Seward County, KS"
classification: county
fips: "20175"
state: "KS"
demographics:
  population: 21486
  population_under_18: 6513
  population_18_64: 12673
  population_65_plus: 2300
  median_household_income: 63827
  poverty_rate: 12.21
  homeownership_rate: 61.8
  unemployment_rate: 4.94
  median_home_value: 136500
  gini_index: 0.401
  vacancy_rate: 12.65
  race_white: 7269
  race_black: 716
  race_asian: 513
  race_native: 621
  hispanic: 14486
  bachelors_plus: 1848
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/38"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/house/125"
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

# Seward County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21486 |
| Under 18 | 6513 |
| 18–64 | 12673 |
| 65+ | 2300 |
| Median household income | 63827 |
| Poverty rate | 12.21 |
| Homeownership rate | 61.8 |
| Unemployment rate | 4.94 |
| Median home value | 136500 |
| Gini index | 0.401 |
| Vacancy rate | 12.65 |
| White | 7269 |
| Black | 716 |
| Asian | 513 |
| Native | 621 |
| Hispanic/Latino | 14486 |
| Bachelor's or higher | 1848 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 38](/us/states/ks/districts/senate/38.md) — 100% (state senate)
- [KS House District 125](/us/states/ks/districts/house/125.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
