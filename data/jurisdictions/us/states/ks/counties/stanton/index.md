---
type: Jurisdiction
title: "Stanton County, KS"
classification: county
fips: "20187"
state: "KS"
demographics:
  population: 2038
  population_under_18: 443
  population_18_64: 1288
  population_65_plus: 307
  median_household_income: 71700
  poverty_rate: 1.49
  homeownership_rate: 76.52
  unemployment_rate: 1.75
  median_home_value: 67800
  gini_index: 0.5002
  vacancy_rate: 16.81
  race_white: 1032
  race_black: 2
  race_asian: 8
  race_native: 130
  hispanic: 929
  bachelors_plus: 435
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/senate/39"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/house/124"
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

# Stanton County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2038 |
| Under 18 | 443 |
| 18–64 | 1288 |
| 65+ | 307 |
| Median household income | 71700 |
| Poverty rate | 1.49 |
| Homeownership rate | 76.52 |
| Unemployment rate | 1.75 |
| Median home value | 67800 |
| Gini index | 0.5002 |
| Vacancy rate | 16.81 |
| White | 1032 |
| Black | 2 |
| Asian | 8 |
| Native | 130 |
| Hispanic/Latino | 929 |
| Bachelor's or higher | 435 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 39](/us/states/ks/districts/senate/39.md) — 100% (state senate)
- [KS House District 124](/us/states/ks/districts/house/124.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
