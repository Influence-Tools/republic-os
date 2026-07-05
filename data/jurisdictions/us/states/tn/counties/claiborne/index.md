---
type: Jurisdiction
title: "Claiborne County, TN"
classification: county
fips: "47025"
state: "TN"
demographics:
  population: 32466
  population_under_18: 6927
  population_18_64: 10052
  population_65_plus: 15487
  median_household_income: 49379
  poverty_rate: 17.36
  homeownership_rate: 72.18
  unemployment_rate: 4.5
  median_home_value: 159900
  gini_index: 0.4688
  vacancy_rate: 11.53
  race_white: 30577
  race_black: 191
  race_asian: 220
  race_native: 22
  hispanic: 560
  bachelors_plus: 6375
districts:
  - to: "us/states/tn/districts/02"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/tn/districts/senate/8"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tn/districts/house/9"
    rel: in-district
    area_weight: 0.5206
  - to: "us/states/tn/districts/house/36"
    rel: in-district
    area_weight: 0.4792
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Claiborne County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 32466 |
| Under 18 | 6927 |
| 18–64 | 10052 |
| 65+ | 15487 |
| Median household income | 49379 |
| Poverty rate | 17.36 |
| Homeownership rate | 72.18 |
| Unemployment rate | 4.5 |
| Median home value | 159900 |
| Gini index | 0.4688 |
| Vacancy rate | 11.53 |
| White | 30577 |
| Black | 191 |
| Asian | 220 |
| Native | 22 |
| Hispanic/Latino | 560 |
| Bachelor's or higher | 6375 |

## Districts

- [TN-02](/us/states/tn/districts/02.md) — 100% (congressional)
- [TN Senate District 8](/us/states/tn/districts/senate/8.md) — 100% (state senate)
- [TN House District 9](/us/states/tn/districts/house/9.md) — 52% (state house)
- [TN House District 36](/us/states/tn/districts/house/36.md) — 48% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
