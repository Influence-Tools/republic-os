---
type: Jurisdiction
title: "Lynn County, TX"
classification: county
fips: "48305"
state: "TX"
demographics:
  population: 5752
  population_under_18: 1599
  population_18_64: 3238
  population_65_plus: 915
  median_household_income: 73679
  poverty_rate: 15.21
  homeownership_rate: 76.99
  unemployment_rate: 3.7
  median_home_value: 147300
  gini_index: 0.4722
  vacancy_rate: 16.74
  race_white: 3558
  race_black: 103
  race_asian: 28
  race_native: 88
  hispanic: 2370
  bachelors_plus: 1395
districts:
  - to: "us/states/tx/districts/19"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/83"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Lynn County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5752 |
| Under 18 | 1599 |
| 18–64 | 3238 |
| 65+ | 915 |
| Median household income | 73679 |
| Poverty rate | 15.21 |
| Homeownership rate | 76.99 |
| Unemployment rate | 3.7 |
| Median home value | 147300 |
| Gini index | 0.4722 |
| Vacancy rate | 16.74 |
| White | 3558 |
| Black | 103 |
| Asian | 28 |
| Native | 88 |
| Hispanic/Latino | 2370 |
| Bachelor's or higher | 1395 |

## Districts

- [TX-19](/us/states/tx/districts/19.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 83](/us/states/tx/districts/house/83.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
