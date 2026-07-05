---
type: Jurisdiction
title: "Barber County, KS"
classification: county
fips: "20007"
state: "KS"
demographics:
  population: 4069
  population_under_18: 932
  population_18_64: 2170
  population_65_plus: 967
  median_household_income: 61926
  poverty_rate: 11.78
  homeownership_rate: 80.96
  unemployment_rate: 1.25
  median_home_value: 97000
  gini_index: 0.4339
  vacancy_rate: 26.29
  race_white: 3671
  race_black: 3
  race_asian: 0
  race_native: 92
  hispanic: 258
  bachelors_plus: 915
districts:
  - to: "us/states/ks/districts/04"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ks/districts/senate/34"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ks/districts/house/116"
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

# Barber County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4069 |
| Under 18 | 932 |
| 18–64 | 2170 |
| 65+ | 967 |
| Median household income | 61926 |
| Poverty rate | 11.78 |
| Homeownership rate | 80.96 |
| Unemployment rate | 1.25 |
| Median home value | 97000 |
| Gini index | 0.4339 |
| Vacancy rate | 26.29 |
| White | 3671 |
| Black | 3 |
| Asian | 0 |
| Native | 92 |
| Hispanic/Latino | 258 |
| Bachelor's or higher | 915 |

## Districts

- [KS-04](/us/states/ks/districts/04.md) — 100% (congressional)
- [KS Senate District 34](/us/states/ks/districts/senate/34.md) — 100% (state senate)
- [KS House District 116](/us/states/ks/districts/house/116.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
