---
type: Jurisdiction
title: "Mitchell County, TX"
classification: county
fips: "48335"
state: "TX"
demographics:
  population: 9018
  population_under_18: 1847
  population_18_64: 5854
  population_65_plus: 1317
  median_household_income: 60550
  poverty_rate: 13.8
  homeownership_rate: 78.68
  unemployment_rate: 5.3
  median_home_value: 85800
  gini_index: 0.4542
  vacancy_rate: 25.28
  race_white: 5534
  race_black: 764
  race_asian: 87
  race_native: 73
  hispanic: 3500
  bachelors_plus: 932
districts:
  - to: "us/states/tx/districts/19"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/83"
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

# Mitchell County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9018 |
| Under 18 | 1847 |
| 18–64 | 5854 |
| 65+ | 1317 |
| Median household income | 60550 |
| Poverty rate | 13.8 |
| Homeownership rate | 78.68 |
| Unemployment rate | 5.3 |
| Median home value | 85800 |
| Gini index | 0.4542 |
| Vacancy rate | 25.28 |
| White | 5534 |
| Black | 764 |
| Asian | 87 |
| Native | 73 |
| Hispanic/Latino | 3500 |
| Bachelor's or higher | 932 |

## Districts

- [TX-19](/us/states/tx/districts/19.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 83](/us/states/tx/districts/house/83.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
