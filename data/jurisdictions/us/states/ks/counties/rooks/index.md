---
type: Jurisdiction
title: "Rooks County, KS"
classification: county
fips: "20163"
state: "KS"
demographics:
  population: 4813
  population_under_18: 1001
  population_18_64: 2661
  population_65_plus: 1151
  median_household_income: 62500
  poverty_rate: 5.53
  homeownership_rate: 74.3
  unemployment_rate: 2.0
  median_home_value: 89000
  gini_index: 0.3679
  vacancy_rate: 18.94
  race_white: 4438
  race_black: 92
  race_asian: 33
  race_native: 23
  hispanic: 156
  bachelors_plus: 1013
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/36"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/house/110"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Rooks County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4813 |
| Under 18 | 1001 |
| 18–64 | 2661 |
| 65+ | 1151 |
| Median household income | 62500 |
| Poverty rate | 5.53 |
| Homeownership rate | 74.3 |
| Unemployment rate | 2.0 |
| Median home value | 89000 |
| Gini index | 0.3679 |
| Vacancy rate | 18.94 |
| White | 4438 |
| Black | 92 |
| Asian | 33 |
| Native | 23 |
| Hispanic/Latino | 156 |
| Bachelor's or higher | 1013 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 36](/us/states/ks/districts/senate/36.md) — 100% (state senate)
- [KS House District 110](/us/states/ks/districts/house/110.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
