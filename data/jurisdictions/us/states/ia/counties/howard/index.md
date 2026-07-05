---
type: Jurisdiction
title: "Howard County, IA"
classification: county
fips: "19089"
state: "IA"
demographics:
  population: 9445
  population_under_18: 2441
  population_18_64: 5072
  population_65_plus: 1932
  median_household_income: 67446
  poverty_rate: 8.93
  homeownership_rate: 77.42
  unemployment_rate: 1.85
  median_home_value: 147800
  gini_index: 0.4254
  vacancy_rate: 12.66
  race_white: 8800
  race_black: 79
  race_asian: 31
  race_native: 23
  hispanic: 312
  bachelors_plus: 1480
districts:
  - to: "us/states/ia/districts/02"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ia/districts/senate/32"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ia/districts/house/63"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Howard County, IA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9445 |
| Under 18 | 2441 |
| 18–64 | 5072 |
| 65+ | 1932 |
| Median household income | 67446 |
| Poverty rate | 8.93 |
| Homeownership rate | 77.42 |
| Unemployment rate | 1.85 |
| Median home value | 147800 |
| Gini index | 0.4254 |
| Vacancy rate | 12.66 |
| White | 8800 |
| Black | 79 |
| Asian | 31 |
| Native | 23 |
| Hispanic/Latino | 312 |
| Bachelor's or higher | 1480 |

## Districts

- [IA-02](/us/states/ia/districts/02.md) — 100% (congressional)
- [IA Senate District 32](/us/states/ia/districts/senate/32.md) — 100% (state senate)
- [IA House District 63](/us/states/ia/districts/house/63.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
