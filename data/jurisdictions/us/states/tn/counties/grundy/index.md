---
type: Jurisdiction
title: "Grundy County, TN"
classification: county
fips: "47061"
state: "TN"
demographics:
  population: 13819
  population_under_18: 2977
  population_18_64: 7980
  population_65_plus: 2862
  median_household_income: 47593
  poverty_rate: 18.87
  homeownership_rate: 83.7
  unemployment_rate: 8.96
  median_home_value: 154000
  gini_index: 0.4366
  vacancy_rate: 17.29
  race_white: 12962
  race_black: 62
  race_asian: 105
  race_native: 16
  hispanic: 56
  bachelors_plus: 2029
districts:
  - to: "us/states/tn/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tn/districts/senate/16"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tn/districts/house/47"
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

# Grundy County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13819 |
| Under 18 | 2977 |
| 18–64 | 7980 |
| 65+ | 2862 |
| Median household income | 47593 |
| Poverty rate | 18.87 |
| Homeownership rate | 83.7 |
| Unemployment rate | 8.96 |
| Median home value | 154000 |
| Gini index | 0.4366 |
| Vacancy rate | 17.29 |
| White | 12962 |
| Black | 62 |
| Asian | 105 |
| Native | 16 |
| Hispanic/Latino | 56 |
| Bachelor's or higher | 2029 |

## Districts

- [TN-04](/us/states/tn/districts/04.md) — 100% (congressional)
- [TN Senate District 16](/us/states/tn/districts/senate/16.md) — 100% (state senate)
- [TN House District 47](/us/states/tn/districts/house/47.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
