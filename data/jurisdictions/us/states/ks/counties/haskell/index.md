---
type: Jurisdiction
title: "Haskell County, KS"
classification: county
fips: "20081"
state: "KS"
demographics:
  population: 3641
  population_under_18: 981
  population_18_64: 2084
  population_65_plus: 576
  median_household_income: 66162
  poverty_rate: 11.2
  homeownership_rate: 76.27
  unemployment_rate: 3.64
  median_home_value: 165100
  gini_index: 0.3882
  vacancy_rate: 9.25
  race_white: 2566
  race_black: 17
  race_asian: 0
  race_native: 26
  hispanic: 1126
  bachelors_plus: 625
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/38"
    rel: in-district
    area_weight: 0.9997
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

# Haskell County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3641 |
| Under 18 | 981 |
| 18–64 | 2084 |
| 65+ | 576 |
| Median household income | 66162 |
| Poverty rate | 11.2 |
| Homeownership rate | 76.27 |
| Unemployment rate | 3.64 |
| Median home value | 165100 |
| Gini index | 0.3882 |
| Vacancy rate | 9.25 |
| White | 2566 |
| Black | 17 |
| Asian | 0 |
| Native | 26 |
| Hispanic/Latino | 1126 |
| Bachelor's or higher | 625 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 38](/us/states/ks/districts/senate/38.md) — 100% (state senate)
- [KS House District 124](/us/states/ks/districts/house/124.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
