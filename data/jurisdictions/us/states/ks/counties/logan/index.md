---
type: Jurisdiction
title: "Logan County, KS"
classification: county
fips: "20109"
state: "KS"
demographics:
  population: 2707
  population_under_18: 629
  population_18_64: 1496
  population_65_plus: 582
  median_household_income: 75662
  poverty_rate: 15.03
  homeownership_rate: 64.87
  unemployment_rate: 1.83
  median_home_value: 117900
  gini_index: 0.4492
  vacancy_rate: 9.35
  race_white: 2405
  race_black: 0
  race_asian: 17
  race_native: 25
  hispanic: 200
  bachelors_plus: 606
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/40"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/house/118"
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

# Logan County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2707 |
| Under 18 | 629 |
| 18–64 | 1496 |
| 65+ | 582 |
| Median household income | 75662 |
| Poverty rate | 15.03 |
| Homeownership rate | 64.87 |
| Unemployment rate | 1.83 |
| Median home value | 117900 |
| Gini index | 0.4492 |
| Vacancy rate | 9.35 |
| White | 2405 |
| Black | 0 |
| Asian | 17 |
| Native | 25 |
| Hispanic/Latino | 200 |
| Bachelor's or higher | 606 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 40](/us/states/ks/districts/senate/40.md) — 100% (state senate)
- [KS House District 118](/us/states/ks/districts/house/118.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
