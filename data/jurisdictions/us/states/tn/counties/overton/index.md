---
type: Jurisdiction
title: "Overton County, TN"
classification: county
fips: "47133"
state: "TN"
demographics:
  population: 23065
  population_under_18: 4758
  population_18_64: 13572
  population_65_plus: 4735
  median_household_income: 48959
  poverty_rate: 16.3
  homeownership_rate: 76.93
  unemployment_rate: 3.17
  median_home_value: 173200
  gini_index: 0.4964
  vacancy_rate: 12.83
  race_white: 21856
  race_black: 318
  race_asian: 56
  race_native: 28
  hispanic: 512
  bachelors_plus: 3233
districts:
  - to: "us/states/tn/districts/06"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tn/districts/senate/12"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tn/districts/house/41"
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

# Overton County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 23065 |
| Under 18 | 4758 |
| 18–64 | 13572 |
| 65+ | 4735 |
| Median household income | 48959 |
| Poverty rate | 16.3 |
| Homeownership rate | 76.93 |
| Unemployment rate | 3.17 |
| Median home value | 173200 |
| Gini index | 0.4964 |
| Vacancy rate | 12.83 |
| White | 21856 |
| Black | 318 |
| Asian | 56 |
| Native | 28 |
| Hispanic/Latino | 512 |
| Bachelor's or higher | 3233 |

## Districts

- [TN-06](/us/states/tn/districts/06.md) — 100% (congressional)
- [TN Senate District 12](/us/states/tn/districts/senate/12.md) — 100% (state senate)
- [TN House District 41](/us/states/tn/districts/house/41.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
