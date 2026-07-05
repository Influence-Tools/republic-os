---
type: Jurisdiction
title: "McPherson County, KS"
classification: county
fips: "20113"
state: "KS"
demographics:
  population: 30205
  population_under_18: 6534
  population_18_64: 17631
  population_65_plus: 6040
  median_household_income: 78851
  poverty_rate: 9.46
  homeownership_rate: 75.47
  unemployment_rate: 1.85
  median_home_value: 211200
  gini_index: 0.4025
  vacancy_rate: 7.7
  race_white: 27879
  race_black: 558
  race_asian: 117
  race_native: 27
  hispanic: 1689
  bachelors_plus: 9284
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/14"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ks/districts/house/73"
    rel: in-district
    area_weight: 0.6411
  - to: "us/states/ks/districts/house/74"
    rel: in-district
    area_weight: 0.1991
  - to: "us/states/ks/districts/house/70"
    rel: in-district
    area_weight: 0.08
  - to: "us/states/ks/districts/house/104"
    rel: in-district
    area_weight: 0.0796
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# McPherson County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 30205 |
| Under 18 | 6534 |
| 18–64 | 17631 |
| 65+ | 6040 |
| Median household income | 78851 |
| Poverty rate | 9.46 |
| Homeownership rate | 75.47 |
| Unemployment rate | 1.85 |
| Median home value | 211200 |
| Gini index | 0.4025 |
| Vacancy rate | 7.7 |
| White | 27879 |
| Black | 558 |
| Asian | 117 |
| Native | 27 |
| Hispanic/Latino | 1689 |
| Bachelor's or higher | 9284 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 14](/us/states/ks/districts/senate/14.md) — 100% (state senate)
- [KS House District 73](/us/states/ks/districts/house/73.md) — 64% (state house)
- [KS House District 74](/us/states/ks/districts/house/74.md) — 20% (state house)
- [KS House District 70](/us/states/ks/districts/house/70.md) — 8% (state house)
- [KS House District 104](/us/states/ks/districts/house/104.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
