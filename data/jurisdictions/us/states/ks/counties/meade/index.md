---
type: Jurisdiction
title: "Meade County, KS"
classification: county
fips: "20119"
state: "KS"
demographics:
  population: 3903
  population_under_18: 1014
  population_18_64: 2179
  population_65_plus: 710
  median_household_income: 71852
  poverty_rate: 11.04
  homeownership_rate: 73.97
  unemployment_rate: 1.53
  median_home_value: 148900
  gini_index: 0.5213
  vacancy_rate: 20.86
  race_white: 2908
  race_black: 15
  race_asian: 85
  race_native: 78
  hispanic: 950
  bachelors_plus: 898
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/38"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/house/115"
    rel: in-district
    area_weight: 0.7428
  - to: "us/states/ks/districts/house/125"
    rel: in-district
    area_weight: 0.2571
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Meade County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3903 |
| Under 18 | 1014 |
| 18–64 | 2179 |
| 65+ | 710 |
| Median household income | 71852 |
| Poverty rate | 11.04 |
| Homeownership rate | 73.97 |
| Unemployment rate | 1.53 |
| Median home value | 148900 |
| Gini index | 0.5213 |
| Vacancy rate | 20.86 |
| White | 2908 |
| Black | 15 |
| Asian | 85 |
| Native | 78 |
| Hispanic/Latino | 950 |
| Bachelor's or higher | 898 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 38](/us/states/ks/districts/senate/38.md) — 100% (state senate)
- [KS House District 115](/us/states/ks/districts/house/115.md) — 74% (state house)
- [KS House District 125](/us/states/ks/districts/house/125.md) — 26% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
