---
type: Jurisdiction
title: "Rawlins County, KS"
classification: county
fips: "20153"
state: "KS"
demographics:
  population: 2516
  population_under_18: 552
  population_18_64: 1263
  population_65_plus: 701
  median_household_income: 67742
  poverty_rate: 6.75
  homeownership_rate: 70.68
  unemployment_rate: 1.33
  median_home_value: 103800
  gini_index: 0.3739
  vacancy_rate: 14.6
  race_white: 2320
  race_black: 0
  race_asian: 20
  race_native: 29
  hispanic: 194
  bachelors_plus: 440
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/senate/40"
    rel: in-district
    area_weight: 0.9999
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

# Rawlins County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2516 |
| Under 18 | 552 |
| 18–64 | 1263 |
| 65+ | 701 |
| Median household income | 67742 |
| Poverty rate | 6.75 |
| Homeownership rate | 70.68 |
| Unemployment rate | 1.33 |
| Median home value | 103800 |
| Gini index | 0.3739 |
| Vacancy rate | 14.6 |
| White | 2320 |
| Black | 0 |
| Asian | 20 |
| Native | 29 |
| Hispanic/Latino | 194 |
| Bachelor's or higher | 440 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 40](/us/states/ks/districts/senate/40.md) — 100% (state senate)
- [KS House District 120](/us/states/ks/districts/house/120.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
