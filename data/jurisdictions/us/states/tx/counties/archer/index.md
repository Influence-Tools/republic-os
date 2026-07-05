---
type: Jurisdiction
title: "Archer County, TX"
classification: county
fips: "48009"
state: "TX"
demographics:
  population: 8867
  population_under_18: 1965
  population_18_64: 4970
  population_65_plus: 1932
  median_household_income: 72159
  poverty_rate: 9.17
  homeownership_rate: 84.46
  unemployment_rate: 3.04
  median_home_value: 189100
  gini_index: 0.4511
  vacancy_rate: 12.56
  race_white: 7883
  race_black: 130
  race_asian: 50
  race_native: 85
  hispanic: 837
  bachelors_plus: 2084
districts:
  - to: "us/states/tx/districts/13"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/tx/districts/senate/30"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/69"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Archer County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8867 |
| Under 18 | 1965 |
| 18–64 | 4970 |
| 65+ | 1932 |
| Median household income | 72159 |
| Poverty rate | 9.17 |
| Homeownership rate | 84.46 |
| Unemployment rate | 3.04 |
| Median home value | 189100 |
| Gini index | 0.4511 |
| Vacancy rate | 12.56 |
| White | 7883 |
| Black | 130 |
| Asian | 50 |
| Native | 85 |
| Hispanic/Latino | 837 |
| Bachelor's or higher | 2084 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 100% (congressional)
- [TX Senate District 30](/us/states/tx/districts/senate/30.md) — 100% (state senate)
- [TX House District 69](/us/states/tx/districts/house/69.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
