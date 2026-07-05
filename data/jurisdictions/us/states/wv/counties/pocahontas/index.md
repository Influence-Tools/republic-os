---
type: Jurisdiction
title: "Pocahontas County, WV"
classification: county
fips: "54075"
state: "WV"
demographics:
  population: 7784
  population_under_18: 1375
  population_18_64: 4301
  population_65_plus: 2108
  median_household_income: 42119
  poverty_rate: 22.55
  homeownership_rate: 83.62
  unemployment_rate: 11.9
  median_home_value: 152400
  gini_index: 0.4428
  vacancy_rate: 53.45
  race_white: 7295
  race_black: 42
  race_asian: 10
  race_native: 77
  hispanic: 131
  bachelors_plus: 1648
districts:
  - to: "us/states/wv/districts/01"
    rel: in-district
    area_weight: 0.9979
  - to: "us/states/wv/districts/senate/11"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/wv/districts/house/66"
    rel: in-district
    area_weight: 0.6296
  - to: "us/states/wv/districts/house/46"
    rel: in-district
    area_weight: 0.3699
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Pocahontas County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7784 |
| Under 18 | 1375 |
| 18–64 | 4301 |
| 65+ | 2108 |
| Median household income | 42119 |
| Poverty rate | 22.55 |
| Homeownership rate | 83.62 |
| Unemployment rate | 11.9 |
| Median home value | 152400 |
| Gini index | 0.4428 |
| Vacancy rate | 53.45 |
| White | 7295 |
| Black | 42 |
| Asian | 10 |
| Native | 77 |
| Hispanic/Latino | 131 |
| Bachelor's or higher | 1648 |

## Districts

- [WV-01](/us/states/wv/districts/01.md) — 100% (congressional)
- [WV Senate District 11](/us/states/wv/districts/senate/11.md) — 100% (state senate)
- [WV House District 66](/us/states/wv/districts/house/66.md) — 63% (state house)
- [WV House District 46](/us/states/wv/districts/house/46.md) — 37% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
