---
type: Jurisdiction
title: "Cloud County, KS"
classification: county
fips: "20029"
state: "KS"
demographics:
  population: 8898
  population_under_18: 2062
  population_18_64: 4928
  population_65_plus: 1908
  median_household_income: 58770
  poverty_rate: 9.95
  homeownership_rate: 73.97
  unemployment_rate: 2.49
  median_home_value: 100000
  gini_index: 0.4014
  vacancy_rate: 14.51
  race_white: 8122
  race_black: 73
  race_asian: 8
  race_native: 44
  hispanic: 343
  bachelors_plus: 1671
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/36"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/house/64"
    rel: in-district
    area_weight: 0.5191
  - to: "us/states/ks/districts/house/107"
    rel: in-district
    area_weight: 0.4808
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Cloud County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8898 |
| Under 18 | 2062 |
| 18–64 | 4928 |
| 65+ | 1908 |
| Median household income | 58770 |
| Poverty rate | 9.95 |
| Homeownership rate | 73.97 |
| Unemployment rate | 2.49 |
| Median home value | 100000 |
| Gini index | 0.4014 |
| Vacancy rate | 14.51 |
| White | 8122 |
| Black | 73 |
| Asian | 8 |
| Native | 44 |
| Hispanic/Latino | 343 |
| Bachelor's or higher | 1671 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 36](/us/states/ks/districts/senate/36.md) — 100% (state senate)
- [KS House District 64](/us/states/ks/districts/house/64.md) — 52% (state house)
- [KS House District 107](/us/states/ks/districts/house/107.md) — 48% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
