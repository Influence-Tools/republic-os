---
type: Jurisdiction
title: "Allen County, KS"
classification: county
fips: "20001"
state: "KS"
demographics:
  population: 12483
  population_under_18: 2814
  population_18_64: 7050
  population_65_plus: 2619
  median_household_income: 60689
  poverty_rate: 9.92
  homeownership_rate: 75.43
  unemployment_rate: 7.91
  median_home_value: 107600
  gini_index: 0.3985
  vacancy_rate: 17.54
  race_white: 11273
  race_black: 352
  race_asian: 46
  race_native: 76
  hispanic: 533
  bachelors_plus: 2573
districts:
  - to: "us/states/ks/districts/02"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ks/districts/senate/12"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/house/9"
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

# Allen County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12483 |
| Under 18 | 2814 |
| 18–64 | 7050 |
| 65+ | 2619 |
| Median household income | 60689 |
| Poverty rate | 9.92 |
| Homeownership rate | 75.43 |
| Unemployment rate | 7.91 |
| Median home value | 107600 |
| Gini index | 0.3985 |
| Vacancy rate | 17.54 |
| White | 11273 |
| Black | 352 |
| Asian | 46 |
| Native | 76 |
| Hispanic/Latino | 533 |
| Bachelor's or higher | 2573 |

## Districts

- [KS-02](/us/states/ks/districts/02.md) — 100% (congressional)
- [KS Senate District 12](/us/states/ks/districts/senate/12.md) — 100% (state senate)
- [KS House District 9](/us/states/ks/districts/house/9.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
