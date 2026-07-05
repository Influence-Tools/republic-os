---
type: Jurisdiction
title: "Lewis County, TN"
classification: county
fips: "47101"
state: "TN"
demographics:
  population: 12992
  population_under_18: 2746
  population_18_64: 7575
  population_65_plus: 2671
  median_household_income: 56285
  poverty_rate: 16.75
  homeownership_rate: 81.94
  unemployment_rate: 3.67
  median_home_value: 173400
  gini_index: 0.5018
  vacancy_rate: 7.18
  race_white: 12067
  race_black: 73
  race_asian: 47
  race_native: 0
  hispanic: 410
  bachelors_plus: 1178
districts:
  - to: "us/states/tn/districts/05"
    rel: in-district
    area_weight: 0.995
  - to: "us/states/tn/districts/senate/28"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/tn/districts/house/69"
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

# Lewis County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12992 |
| Under 18 | 2746 |
| 18–64 | 7575 |
| 65+ | 2671 |
| Median household income | 56285 |
| Poverty rate | 16.75 |
| Homeownership rate | 81.94 |
| Unemployment rate | 3.67 |
| Median home value | 173400 |
| Gini index | 0.5018 |
| Vacancy rate | 7.18 |
| White | 12067 |
| Black | 73 |
| Asian | 47 |
| Native | 0 |
| Hispanic/Latino | 410 |
| Bachelor's or higher | 1178 |

## Districts

- [TN-05](/us/states/tn/districts/05.md) — 100% (congressional)
- [TN Senate District 28](/us/states/tn/districts/senate/28.md) — 100% (state senate)
- [TN House District 69](/us/states/tn/districts/house/69.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
