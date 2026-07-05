---
type: Jurisdiction
title: "Sherman County, KS"
classification: county
fips: "20181"
state: "KS"
demographics:
  population: 5858
  population_under_18: 1350
  population_18_64: 3269
  population_65_plus: 1239
  median_household_income: 61750
  poverty_rate: 10.19
  homeownership_rate: 65.54
  unemployment_rate: 0.6
  median_home_value: 136700
  gini_index: 0.4621
  vacancy_rate: 16.59
  race_white: 5134
  race_black: 104
  race_asian: 7
  race_native: 0
  hispanic: 761
  bachelors_plus: 1126
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/40"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/house/120"
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

# Sherman County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5858 |
| Under 18 | 1350 |
| 18–64 | 3269 |
| 65+ | 1239 |
| Median household income | 61750 |
| Poverty rate | 10.19 |
| Homeownership rate | 65.54 |
| Unemployment rate | 0.6 |
| Median home value | 136700 |
| Gini index | 0.4621 |
| Vacancy rate | 16.59 |
| White | 5134 |
| Black | 104 |
| Asian | 7 |
| Native | 0 |
| Hispanic/Latino | 761 |
| Bachelor's or higher | 1126 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 40](/us/states/ks/districts/senate/40.md) — 100% (state senate)
- [KS House District 120](/us/states/ks/districts/house/120.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
