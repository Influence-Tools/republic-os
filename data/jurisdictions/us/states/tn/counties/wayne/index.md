---
type: Jurisdiction
title: "Wayne County, TN"
classification: county
fips: "47181"
state: "TN"
demographics:
  population: 16168
  population_under_18: 2665
  population_18_64: 10313
  population_65_plus: 3190
  median_household_income: 52294
  poverty_rate: 19.96
  homeownership_rate: 80.17
  unemployment_rate: 3.39
  median_home_value: 130700
  gini_index: 0.4668
  vacancy_rate: 17.04
  race_white: 14431
  race_black: 692
  race_asian: 0
  race_native: 26
  hispanic: 441
  bachelors_plus: 2306
districts:
  - to: "us/states/tn/districts/07"
    rel: in-district
    area_weight: 0.9986
  - to: "us/states/tn/districts/senate/26"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tn/districts/house/71"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Wayne County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16168 |
| Under 18 | 2665 |
| 18–64 | 10313 |
| 65+ | 3190 |
| Median household income | 52294 |
| Poverty rate | 19.96 |
| Homeownership rate | 80.17 |
| Unemployment rate | 3.39 |
| Median home value | 130700 |
| Gini index | 0.4668 |
| Vacancy rate | 17.04 |
| White | 14431 |
| Black | 692 |
| Asian | 0 |
| Native | 26 |
| Hispanic/Latino | 441 |
| Bachelor's or higher | 2306 |

## Districts

- [TN-07](/us/states/tn/districts/07.md) — 100% (congressional)
- [TN Senate District 26](/us/states/tn/districts/senate/26.md) — 100% (state senate)
- [TN House District 71](/us/states/tn/districts/house/71.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
