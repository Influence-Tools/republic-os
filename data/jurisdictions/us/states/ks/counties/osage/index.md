---
type: Jurisdiction
title: "Osage County, KS"
classification: county
fips: "20139"
state: "KS"
demographics:
  population: 15744
  population_under_18: 3625
  population_18_64: 8831
  population_65_plus: 3288
  median_household_income: 74467
  poverty_rate: 9.71
  homeownership_rate: 82.35
  unemployment_rate: 1.93
  median_home_value: 156800
  gini_index: 0.3807
  vacancy_rate: 12.33
  race_white: 14600
  race_black: 44
  race_asian: 23
  race_native: 46
  hispanic: 529
  bachelors_plus: 3127
districts:
  - to: "us/states/ks/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/3"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ks/districts/house/76"
    rel: in-district
    area_weight: 0.5917
  - to: "us/states/ks/districts/house/54"
    rel: in-district
    area_weight: 0.4082
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Osage County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15744 |
| Under 18 | 3625 |
| 18–64 | 8831 |
| 65+ | 3288 |
| Median household income | 74467 |
| Poverty rate | 9.71 |
| Homeownership rate | 82.35 |
| Unemployment rate | 1.93 |
| Median home value | 156800 |
| Gini index | 0.3807 |
| Vacancy rate | 12.33 |
| White | 14600 |
| Black | 44 |
| Asian | 23 |
| Native | 46 |
| Hispanic/Latino | 529 |
| Bachelor's or higher | 3127 |

## Districts

- [KS-02](/us/states/ks/districts/02.md) — 100% (congressional)
- [KS Senate District 3](/us/states/ks/districts/senate/3.md) — 100% (state senate)
- [KS House District 76](/us/states/ks/districts/house/76.md) — 59% (state house)
- [KS House District 54](/us/states/ks/districts/house/54.md) — 41% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
