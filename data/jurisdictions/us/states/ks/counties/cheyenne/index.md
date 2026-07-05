---
type: Jurisdiction
title: "Cheyenne County, KS"
classification: county
fips: "20023"
state: "KS"
demographics:
  population: 2628
  population_under_18: 598
  population_18_64: 1341
  population_65_plus: 689
  median_household_income: 55429
  poverty_rate: 17.01
  homeownership_rate: 77.85
  unemployment_rate: 2.45
  median_home_value: 125900
  gini_index: 0.4713
  vacancy_rate: 16.84
  race_white: 2321
  race_black: 3
  race_asian: 0
  race_native: 23
  hispanic: 246
  bachelors_plus: 519
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ks/districts/senate/40"
    rel: in-district
    area_weight: 0.9998
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

# Cheyenne County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2628 |
| Under 18 | 598 |
| 18–64 | 1341 |
| 65+ | 689 |
| Median household income | 55429 |
| Poverty rate | 17.01 |
| Homeownership rate | 77.85 |
| Unemployment rate | 2.45 |
| Median home value | 125900 |
| Gini index | 0.4713 |
| Vacancy rate | 16.84 |
| White | 2321 |
| Black | 3 |
| Asian | 0 |
| Native | 23 |
| Hispanic/Latino | 246 |
| Bachelor's or higher | 519 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 40](/us/states/ks/districts/senate/40.md) — 100% (state senate)
- [KS House District 120](/us/states/ks/districts/house/120.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
