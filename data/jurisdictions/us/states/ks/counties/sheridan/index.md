---
type: Jurisdiction
title: "Sheridan County, KS"
classification: county
fips: "20179"
state: "KS"
demographics:
  population: 2426
  population_under_18: 614
  population_18_64: 1244
  population_65_plus: 568
  median_household_income: 73750
  poverty_rate: 8.93
  homeownership_rate: 76.8
  unemployment_rate: 0.69
  median_home_value: 167200
  gini_index: 0.4741
  vacancy_rate: 14.55
  race_white: 2246
  race_black: 1
  race_asian: 1
  race_native: 7
  hispanic: 143
  bachelors_plus: 535
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/40"
    rel: in-district
    area_weight: 1.0
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

# Sheridan County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2426 |
| Under 18 | 614 |
| 18–64 | 1244 |
| 65+ | 568 |
| Median household income | 73750 |
| Poverty rate | 8.93 |
| Homeownership rate | 76.8 |
| Unemployment rate | 0.69 |
| Median home value | 167200 |
| Gini index | 0.4741 |
| Vacancy rate | 14.55 |
| White | 2246 |
| Black | 1 |
| Asian | 1 |
| Native | 7 |
| Hispanic/Latino | 143 |
| Bachelor's or higher | 535 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 40](/us/states/ks/districts/senate/40.md) — 100% (state senate)
- [KS House District 118](/us/states/ks/districts/house/118.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
