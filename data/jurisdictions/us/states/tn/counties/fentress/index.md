---
type: Jurisdiction
title: "Fentress County, TN"
classification: county
fips: "47049"
state: "TN"
demographics:
  population: 19309
  population_under_18: 3935
  population_18_64: 10876
  population_65_plus: 4498
  median_household_income: 51149
  poverty_rate: 20.98
  homeownership_rate: 82.57
  unemployment_rate: 4.65
  median_home_value: 168200
  gini_index: 0.4191
  vacancy_rate: 15.43
  race_white: 18321
  race_black: 45
  race_asian: 42
  race_native: 0
  hispanic: 413
  bachelors_plus: 2862
districts:
  - to: "us/states/tn/districts/06"
    rel: in-district
    area_weight: 0.9979
  - to: "us/states/tn/districts/senate/12"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tn/districts/house/38"
    rel: in-district
    area_weight: 0.5761
  - to: "us/states/tn/districts/house/41"
    rel: in-district
    area_weight: 0.4238
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Fentress County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19309 |
| Under 18 | 3935 |
| 18–64 | 10876 |
| 65+ | 4498 |
| Median household income | 51149 |
| Poverty rate | 20.98 |
| Homeownership rate | 82.57 |
| Unemployment rate | 4.65 |
| Median home value | 168200 |
| Gini index | 0.4191 |
| Vacancy rate | 15.43 |
| White | 18321 |
| Black | 45 |
| Asian | 42 |
| Native | 0 |
| Hispanic/Latino | 413 |
| Bachelor's or higher | 2862 |

## Districts

- [TN-06](/us/states/tn/districts/06.md) — 100% (congressional)
- [TN Senate District 12](/us/states/tn/districts/senate/12.md) — 100% (state senate)
- [TN House District 38](/us/states/tn/districts/house/38.md) — 58% (state house)
- [TN House District 41](/us/states/tn/districts/house/41.md) — 42% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
