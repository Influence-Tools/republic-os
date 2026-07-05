---
type: Jurisdiction
title: "Lake County, TN"
classification: county
fips: "47095"
state: "TN"
demographics:
  population: 6579
  population_under_18: 978
  population_18_64: 4522
  population_65_plus: 1079
  median_household_income: 28814
  poverty_rate: 32.18
  homeownership_rate: 47.75
  unemployment_rate: 4.91
  median_home_value: 97900
  gini_index: 0.5417
  vacancy_rate: 17.12
  race_white: 4285
  race_black: 1477
  race_asian: 34
  race_native: 58
  hispanic: 206
  bachelors_plus: 717
districts:
  - to: "us/states/tn/districts/08"
    rel: in-district
    area_weight: 0.9985
  - to: "us/states/tn/districts/senate/25"
    rel: in-district
    area_weight: 0.9985
  - to: "us/states/tn/districts/house/77"
    rel: in-district
    area_weight: 0.9985
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Lake County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6579 |
| Under 18 | 978 |
| 18–64 | 4522 |
| 65+ | 1079 |
| Median household income | 28814 |
| Poverty rate | 32.18 |
| Homeownership rate | 47.75 |
| Unemployment rate | 4.91 |
| Median home value | 97900 |
| Gini index | 0.5417 |
| Vacancy rate | 17.12 |
| White | 4285 |
| Black | 1477 |
| Asian | 34 |
| Native | 58 |
| Hispanic/Latino | 206 |
| Bachelor's or higher | 717 |

## Districts

- [TN-08](/us/states/tn/districts/08.md) — 100% (congressional)
- [TN Senate District 25](/us/states/tn/districts/senate/25.md) — 100% (state senate)
- [TN House District 77](/us/states/tn/districts/house/77.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
