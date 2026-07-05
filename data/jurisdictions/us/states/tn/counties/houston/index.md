---
type: Jurisdiction
title: "Houston County, TN"
classification: county
fips: "47083"
state: "TN"
demographics:
  population: 8353
  population_under_18: 1735
  population_18_64: 4937
  population_65_plus: 1681
  median_household_income: 59576
  poverty_rate: 11.06
  homeownership_rate: 80.97
  unemployment_rate: 3.88
  median_home_value: 172700
  gini_index: 0.379
  vacancy_rate: 15.2
  race_white: 7703
  race_black: 214
  race_asian: 22
  race_native: 10
  hispanic: 269
  bachelors_plus: 1057
districts:
  - to: "us/states/tn/districts/07"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tn/districts/senate/24"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/tn/districts/house/74"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Houston County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8353 |
| Under 18 | 1735 |
| 18–64 | 4937 |
| 65+ | 1681 |
| Median household income | 59576 |
| Poverty rate | 11.06 |
| Homeownership rate | 80.97 |
| Unemployment rate | 3.88 |
| Median home value | 172700 |
| Gini index | 0.379 |
| Vacancy rate | 15.2 |
| White | 7703 |
| Black | 214 |
| Asian | 22 |
| Native | 10 |
| Hispanic/Latino | 269 |
| Bachelor's or higher | 1057 |

## Districts

- [TN-07](/us/states/tn/districts/07.md) — 100% (congressional)
- [TN Senate District 24](/us/states/tn/districts/senate/24.md) — 100% (state senate)
- [TN House District 74](/us/states/tn/districts/house/74.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
