---
type: Jurisdiction
title: "Gray County, KS"
classification: county
fips: "20069"
state: "KS"
demographics:
  population: 5701
  population_under_18: 1625
  population_18_64: 3116
  population_65_plus: 960
  median_household_income: 79122
  poverty_rate: 8.52
  homeownership_rate: 77.06
  unemployment_rate: 2.65
  median_home_value: 206000
  gini_index: 0.411
  vacancy_rate: 9.26
  race_white: 5108
  race_black: 0
  race_asian: 36
  race_native: 10
  hispanic: 949
  bachelors_plus: 1083
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/38"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/house/115"
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

# Gray County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5701 |
| Under 18 | 1625 |
| 18–64 | 3116 |
| 65+ | 960 |
| Median household income | 79122 |
| Poverty rate | 8.52 |
| Homeownership rate | 77.06 |
| Unemployment rate | 2.65 |
| Median home value | 206000 |
| Gini index | 0.411 |
| Vacancy rate | 9.26 |
| White | 5108 |
| Black | 0 |
| Asian | 36 |
| Native | 10 |
| Hispanic/Latino | 949 |
| Bachelor's or higher | 1083 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 38](/us/states/ks/districts/senate/38.md) — 100% (state senate)
- [KS House District 115](/us/states/ks/districts/house/115.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
