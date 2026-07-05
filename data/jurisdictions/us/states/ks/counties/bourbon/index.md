---
type: Jurisdiction
title: "Bourbon County, KS"
classification: county
fips: "20011"
state: "KS"
demographics:
  population: 14394
  population_under_18: 3601
  population_18_64: 7913
  population_65_plus: 2880
  median_household_income: 59238
  poverty_rate: 13.64
  homeownership_rate: 74.04
  unemployment_rate: 5.28
  median_home_value: 113800
  gini_index: 0.4106
  vacancy_rate: 13.56
  race_white: 13033
  race_black: 245
  race_asian: 116
  race_native: 12
  hispanic: 452
  bachelors_plus: 2901
districts:
  - to: "us/states/ks/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/senate/13"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ks/districts/house/4"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Bourbon County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14394 |
| Under 18 | 3601 |
| 18–64 | 7913 |
| 65+ | 2880 |
| Median household income | 59238 |
| Poverty rate | 13.64 |
| Homeownership rate | 74.04 |
| Unemployment rate | 5.28 |
| Median home value | 113800 |
| Gini index | 0.4106 |
| Vacancy rate | 13.56 |
| White | 13033 |
| Black | 245 |
| Asian | 116 |
| Native | 12 |
| Hispanic/Latino | 452 |
| Bachelor's or higher | 2901 |

## Districts

- [KS-02](/us/states/ks/districts/02.md) — 100% (congressional)
- [KS Senate District 13](/us/states/ks/districts/senate/13.md) — 100% (state senate)
- [KS House District 4](/us/states/ks/districts/house/4.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
