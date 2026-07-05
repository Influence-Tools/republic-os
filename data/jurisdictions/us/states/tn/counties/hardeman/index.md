---
type: Jurisdiction
title: "Hardeman County, TN"
classification: county
fips: "47069"
state: "TN"
demographics:
  population: 25433
  population_under_18: 4913
  population_18_64: 15769
  population_65_plus: 4751
  median_household_income: 46069
  poverty_rate: 18.99
  homeownership_rate: 71.7
  unemployment_rate: 9.79
  median_home_value: 121700
  gini_index: 0.4361
  vacancy_rate: 15.26
  race_white: 13590
  race_black: 9758
  race_asian: 187
  race_native: 87
  hispanic: 560
  bachelors_plus: 2920
districts:
  - to: "us/states/tn/districts/08"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tn/districts/senate/26"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tn/districts/house/80"
    rel: in-district
    area_weight: 0.8718
  - to: "us/states/tn/districts/house/94"
    rel: in-district
    area_weight: 0.1281
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Hardeman County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25433 |
| Under 18 | 4913 |
| 18–64 | 15769 |
| 65+ | 4751 |
| Median household income | 46069 |
| Poverty rate | 18.99 |
| Homeownership rate | 71.7 |
| Unemployment rate | 9.79 |
| Median home value | 121700 |
| Gini index | 0.4361 |
| Vacancy rate | 15.26 |
| White | 13590 |
| Black | 9758 |
| Asian | 187 |
| Native | 87 |
| Hispanic/Latino | 560 |
| Bachelor's or higher | 2920 |

## Districts

- [TN-08](/us/states/tn/districts/08.md) — 100% (congressional)
- [TN Senate District 26](/us/states/tn/districts/senate/26.md) — 100% (state senate)
- [TN House District 80](/us/states/tn/districts/house/80.md) — 87% (state house)
- [TN House District 94](/us/states/tn/districts/house/94.md) — 13% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
