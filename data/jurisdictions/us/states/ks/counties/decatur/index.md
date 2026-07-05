---
type: Jurisdiction
title: "Decatur County, KS"
classification: county
fips: "20039"
state: "KS"
demographics:
  population: 2726
  population_under_18: 568
  population_18_64: 1347
  population_65_plus: 811
  median_household_income: 53870
  poverty_rate: 12.73
  homeownership_rate: 77.69
  unemployment_rate: 4.11
  median_home_value: 89500
  gini_index: 0.4175
  vacancy_rate: 18.79
  race_white: 2527
  race_black: 31
  race_asian: 0
  race_native: 14
  hispanic: 130
  bachelors_plus: 715
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/senate/40"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/house/120"
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

# Decatur County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2726 |
| Under 18 | 568 |
| 18–64 | 1347 |
| 65+ | 811 |
| Median household income | 53870 |
| Poverty rate | 12.73 |
| Homeownership rate | 77.69 |
| Unemployment rate | 4.11 |
| Median home value | 89500 |
| Gini index | 0.4175 |
| Vacancy rate | 18.79 |
| White | 2527 |
| Black | 31 |
| Asian | 0 |
| Native | 14 |
| Hispanic/Latino | 130 |
| Bachelor's or higher | 715 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 40](/us/states/ks/districts/senate/40.md) — 100% (state senate)
- [KS House District 120](/us/states/ks/districts/house/120.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
