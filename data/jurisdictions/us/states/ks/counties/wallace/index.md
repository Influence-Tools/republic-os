---
type: Jurisdiction
title: "Wallace County, KS"
classification: county
fips: "20199"
state: "KS"
demographics:
  population: 1417
  population_under_18: 326
  population_18_64: 722
  population_65_plus: 369
  median_household_income: 63207
  poverty_rate: 12.28
  homeownership_rate: 74.79
  unemployment_rate: 1.33
  median_home_value: 105000
  gini_index: 0.4483
  vacancy_rate: 16.46
  race_white: 1268
  race_black: 12
  race_asian: 8
  race_native: 10
  hispanic: 105
  bachelors_plus: 288
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

# Wallace County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1417 |
| Under 18 | 326 |
| 18–64 | 722 |
| 65+ | 369 |
| Median household income | 63207 |
| Poverty rate | 12.28 |
| Homeownership rate | 74.79 |
| Unemployment rate | 1.33 |
| Median home value | 105000 |
| Gini index | 0.4483 |
| Vacancy rate | 16.46 |
| White | 1268 |
| Black | 12 |
| Asian | 8 |
| Native | 10 |
| Hispanic/Latino | 105 |
| Bachelor's or higher | 288 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 40](/us/states/ks/districts/senate/40.md) — 100% (state senate)
- [KS House District 120](/us/states/ks/districts/house/120.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
