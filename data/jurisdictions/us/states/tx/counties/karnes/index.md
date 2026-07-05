---
type: Jurisdiction
title: "Karnes County, TX"
classification: county
fips: "48255"
state: "TX"
demographics:
  population: 14968
  population_under_18: 2908
  population_18_64: 9792
  population_65_plus: 2268
  median_household_income: 60214
  poverty_rate: 19.15
  homeownership_rate: 62.43
  unemployment_rate: 2.94
  median_home_value: 149000
  gini_index: 0.5542
  vacancy_rate: 20.84
  race_white: 7630
  race_black: 1424
  race_asian: 45
  race_native: 28
  hispanic: 7991
  bachelors_plus: 2063
districts:
  - to: "us/states/tx/districts/15"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/senate/21"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/31"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Karnes County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14968 |
| Under 18 | 2908 |
| 18–64 | 9792 |
| 65+ | 2268 |
| Median household income | 60214 |
| Poverty rate | 19.15 |
| Homeownership rate | 62.43 |
| Unemployment rate | 2.94 |
| Median home value | 149000 |
| Gini index | 0.5542 |
| Vacancy rate | 20.84 |
| White | 7630 |
| Black | 1424 |
| Asian | 45 |
| Native | 28 |
| Hispanic/Latino | 7991 |
| Bachelor's or higher | 2063 |

## Districts

- [TX-15](/us/states/tx/districts/15.md) — 100% (congressional)
- [TX Senate District 21](/us/states/tx/districts/senate/21.md) — 100% (state senate)
- [TX House District 31](/us/states/tx/districts/house/31.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
