---
type: Jurisdiction
title: "Washington County, TN"
classification: county
fips: "47179"
state: "TN"
demographics:
  population: 136261
  population_under_18: 25446
  population_18_64: 85064
  population_65_plus: 25751
  median_household_income: 62809
  poverty_rate: 15.54
  homeownership_rate: 64.55
  unemployment_rate: 4.73
  median_home_value: 249000
  gini_index: 0.4718
  vacancy_rate: 8.57
  race_white: 118236
  race_black: 4835
  race_asian: 2135
  race_native: 259
  hispanic: 6679
  bachelors_plus: 45990
districts:
  - to: "us/states/tn/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tn/districts/senate/3"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tn/districts/house/7"
    rel: in-district
    area_weight: 0.5128
  - to: "us/states/tn/districts/house/6"
    rel: in-district
    area_weight: 0.4869
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Washington County, TN

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 136261 |
| Under 18 | 25446 |
| 18–64 | 85064 |
| 65+ | 25751 |
| Median household income | 62809 |
| Poverty rate | 15.54 |
| Homeownership rate | 64.55 |
| Unemployment rate | 4.73 |
| Median home value | 249000 |
| Gini index | 0.4718 |
| Vacancy rate | 8.57 |
| White | 118236 |
| Black | 4835 |
| Asian | 2135 |
| Native | 259 |
| Hispanic/Latino | 6679 |
| Bachelor's or higher | 45990 |

## Districts

- [TN-01](/us/states/tn/districts/01.md) — 100% (congressional)
- [TN Senate District 3](/us/states/tn/districts/senate/3.md) — 100% (state senate)
- [TN House District 7](/us/states/tn/districts/house/7.md) — 51% (state house)
- [TN House District 6](/us/states/tn/districts/house/6.md) — 49% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
