---
type: Jurisdiction
title: "Atchison County, KS"
classification: county
fips: "20005"
state: "KS"
demographics:
  population: 16208
  population_under_18: 3537
  population_18_64: 9740
  population_65_plus: 2931
  median_household_income: 61112
  poverty_rate: 12.98
  homeownership_rate: 71.91
  unemployment_rate: 4.59
  median_home_value: 145700
  gini_index: 0.4414
  vacancy_rate: 15.87
  race_white: 14207
  race_black: 588
  race_asian: 55
  race_native: 42
  hispanic: 608
  bachelors_plus: 2976
districts:
  - to: "us/states/ks/districts/02"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ks/districts/senate/1"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ks/districts/house/63"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Atchison County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16208 |
| Under 18 | 3537 |
| 18–64 | 9740 |
| 65+ | 2931 |
| Median household income | 61112 |
| Poverty rate | 12.98 |
| Homeownership rate | 71.91 |
| Unemployment rate | 4.59 |
| Median home value | 145700 |
| Gini index | 0.4414 |
| Vacancy rate | 15.87 |
| White | 14207 |
| Black | 588 |
| Asian | 55 |
| Native | 42 |
| Hispanic/Latino | 608 |
| Bachelor's or higher | 2976 |

## Districts

- [KS-02](/us/states/ks/districts/02.md) — 100% (congressional)
- [KS Senate District 1](/us/states/ks/districts/senate/1.md) — 100% (state senate)
- [KS House District 63](/us/states/ks/districts/house/63.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
