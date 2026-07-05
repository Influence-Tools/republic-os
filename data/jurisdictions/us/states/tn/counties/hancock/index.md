---
type: Jurisdiction
title: "Hancock County, TN"
classification: county
fips: "47067"
state: "TN"
demographics:
  population: 6852
  population_under_18: 1450
  population_18_64: 3861
  population_65_plus: 1541
  median_household_income: 34960
  poverty_rate: 32.25
  homeownership_rate: 74.61
  unemployment_rate: 6.29
  median_home_value: 134500
  gini_index: 0.5228
  vacancy_rate: 23.05
  race_white: 6541
  race_black: 38
  race_asian: 23
  race_native: 0
  hispanic: 102
  bachelors_plus: 793
districts:
  - to: "us/states/tn/districts/01"
    rel: in-district
    area_weight: 0.9984
  - to: "us/states/tn/districts/senate/8"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/tn/districts/house/9"
    rel: in-district
    area_weight: 0.9992
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Hancock County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6852 |
| Under 18 | 1450 |
| 18–64 | 3861 |
| 65+ | 1541 |
| Median household income | 34960 |
| Poverty rate | 32.25 |
| Homeownership rate | 74.61 |
| Unemployment rate | 6.29 |
| Median home value | 134500 |
| Gini index | 0.5228 |
| Vacancy rate | 23.05 |
| White | 6541 |
| Black | 38 |
| Asian | 23 |
| Native | 0 |
| Hispanic/Latino | 102 |
| Bachelor's or higher | 793 |

## Districts

- [TN-01](/us/states/tn/districts/01.md) — 100% (congressional)
- [TN Senate District 8](/us/states/tn/districts/senate/8.md) — 100% (state senate)
- [TN House District 9](/us/states/tn/districts/house/9.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
