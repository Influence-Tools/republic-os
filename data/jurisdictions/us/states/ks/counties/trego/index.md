---
type: Jurisdiction
title: "Trego County, KS"
classification: county
fips: "20195"
state: "KS"
demographics:
  population: 2777
  population_under_18: 560
  population_18_64: 1441
  population_65_plus: 776
  median_household_income: 81528
  poverty_rate: 5.52
  homeownership_rate: 82.22
  unemployment_rate: 1.0
  median_home_value: 120900
  gini_index: 0.4105
  vacancy_rate: 20.01
  race_white: 2646
  race_black: 0
  race_asian: 45
  race_native: 14
  hispanic: 31
  bachelors_plus: 832
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/40"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/house/118"
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

# Trego County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2777 |
| Under 18 | 560 |
| 18–64 | 1441 |
| 65+ | 776 |
| Median household income | 81528 |
| Poverty rate | 5.52 |
| Homeownership rate | 82.22 |
| Unemployment rate | 1.0 |
| Median home value | 120900 |
| Gini index | 0.4105 |
| Vacancy rate | 20.01 |
| White | 2646 |
| Black | 0 |
| Asian | 45 |
| Native | 14 |
| Hispanic/Latino | 31 |
| Bachelor's or higher | 832 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 40](/us/states/ks/districts/senate/40.md) — 100% (state senate)
- [KS House District 118](/us/states/ks/districts/house/118.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
