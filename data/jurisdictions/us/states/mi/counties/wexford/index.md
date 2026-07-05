---
type: Jurisdiction
title: "Wexford County, MI"
classification: county
fips: "26165"
state: "MI"
demographics:
  population: 34077
  population_under_18: 7784
  population_18_64: 19228
  population_65_plus: 7065
  median_household_income: 61085
  poverty_rate: 13.92
  homeownership_rate: 80.89
  unemployment_rate: 5.29
  median_home_value: 170400
  gini_index: 0.4351
  vacancy_rate: 17.42
  race_white: 31356
  race_black: 402
  race_asian: 218
  race_native: 87
  hispanic: 923
  bachelors_plus: 6904
districts:
  - to: "us/states/mi/districts/02"
    rel: in-district
    area_weight: 0.7797
  - to: "us/states/mi/districts/01"
    rel: in-district
    area_weight: 0.2203
  - to: "us/states/mi/districts/senate/36"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mi/districts/house/101"
    rel: in-district
    area_weight: 0.7481
  - to: "us/states/mi/districts/house/104"
    rel: in-district
    area_weight: 0.2516
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Wexford County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 34077 |
| Under 18 | 7784 |
| 18–64 | 19228 |
| 65+ | 7065 |
| Median household income | 61085 |
| Poverty rate | 13.92 |
| Homeownership rate | 80.89 |
| Unemployment rate | 5.29 |
| Median home value | 170400 |
| Gini index | 0.4351 |
| Vacancy rate | 17.42 |
| White | 31356 |
| Black | 402 |
| Asian | 218 |
| Native | 87 |
| Hispanic/Latino | 923 |
| Bachelor's or higher | 6904 |

## Districts

- [MI-02](/us/states/mi/districts/02.md) — 78% (congressional)
- [MI-01](/us/states/mi/districts/01.md) — 22% (congressional)
- [MI Senate District 36](/us/states/mi/districts/senate/36.md) — 100% (state senate)
- [MI House District 101](/us/states/mi/districts/house/101.md) — 75% (state house)
- [MI House District 104](/us/states/mi/districts/house/104.md) — 25% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
