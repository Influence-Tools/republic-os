---
type: Jurisdiction
title: "Kearny County, KS"
classification: county
fips: "20093"
state: "KS"
demographics:
  population: 3864
  population_under_18: 1099
  population_18_64: 2062
  population_65_plus: 703
  median_household_income: 89135
  poverty_rate: 4.51
  homeownership_rate: 71.69
  unemployment_rate: 2.21
  median_home_value: 200900
  gini_index: 0.3209
  vacancy_rate: 9.57
  race_white: 2540
  race_black: 0
  race_asian: 140
  race_native: 15
  hispanic: 1377
  bachelors_plus: 643
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/39"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/house/122"
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

# Kearny County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3864 |
| Under 18 | 1099 |
| 18–64 | 2062 |
| 65+ | 703 |
| Median household income | 89135 |
| Poverty rate | 4.51 |
| Homeownership rate | 71.69 |
| Unemployment rate | 2.21 |
| Median home value | 200900 |
| Gini index | 0.3209 |
| Vacancy rate | 9.57 |
| White | 2540 |
| Black | 0 |
| Asian | 140 |
| Native | 15 |
| Hispanic/Latino | 1377 |
| Bachelor's or higher | 643 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 39](/us/states/ks/districts/senate/39.md) — 100% (state senate)
- [KS House District 122](/us/states/ks/districts/house/122.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
