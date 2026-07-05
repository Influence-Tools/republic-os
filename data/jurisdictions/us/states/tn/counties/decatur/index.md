---
type: Jurisdiction
title: "Decatur County, TN"
classification: county
fips: "47039"
state: "TN"
demographics:
  population: 11579
  population_under_18: 2584
  population_18_64: 3027
  population_65_plus: 5968
  median_household_income: 45375
  poverty_rate: 22.15
  homeownership_rate: 74.34
  unemployment_rate: 7.16
  median_home_value: 139600
  gini_index: 0.461
  vacancy_rate: 30.69
  race_white: 10592
  race_black: 315
  race_asian: 161
  race_native: 8
  hispanic: 429
  bachelors_plus: 1419
districts:
  - to: "us/states/tn/districts/07"
    rel: in-district
    area_weight: 0.9972
  - to: "us/states/tn/districts/senate/25"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tn/districts/house/72"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Decatur County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11579 |
| Under 18 | 2584 |
| 18–64 | 3027 |
| 65+ | 5968 |
| Median household income | 45375 |
| Poverty rate | 22.15 |
| Homeownership rate | 74.34 |
| Unemployment rate | 7.16 |
| Median home value | 139600 |
| Gini index | 0.461 |
| Vacancy rate | 30.69 |
| White | 10592 |
| Black | 315 |
| Asian | 161 |
| Native | 8 |
| Hispanic/Latino | 429 |
| Bachelor's or higher | 1419 |

## Districts

- [TN-07](/us/states/tn/districts/07.md) — 100% (congressional)
- [TN Senate District 25](/us/states/tn/districts/senate/25.md) — 100% (state senate)
- [TN House District 72](/us/states/tn/districts/house/72.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
