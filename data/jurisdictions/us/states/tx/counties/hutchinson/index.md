---
type: Jurisdiction
title: "Hutchinson County, TX"
classification: county
fips: "48233"
state: "TX"
demographics:
  population: 20184
  population_under_18: 5031
  population_18_64: 11529
  population_65_plus: 3624
  median_household_income: 67228
  poverty_rate: 13.32
  homeownership_rate: 83.27
  unemployment_rate: 3.6
  median_home_value: 119100
  gini_index: 0.419
  vacancy_rate: 31.17
  race_white: 14205
  race_black: 434
  race_asian: 127
  race_native: 404
  hispanic: 5012
  bachelors_plus: 2793
districts:
  - to: "us/states/tx/districts/13"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/87"
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

# Hutchinson County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20184 |
| Under 18 | 5031 |
| 18–64 | 11529 |
| 65+ | 3624 |
| Median household income | 67228 |
| Poverty rate | 13.32 |
| Homeownership rate | 83.27 |
| Unemployment rate | 3.6 |
| Median home value | 119100 |
| Gini index | 0.419 |
| Vacancy rate | 31.17 |
| White | 14205 |
| Black | 434 |
| Asian | 127 |
| Native | 404 |
| Hispanic/Latino | 5012 |
| Bachelor's or higher | 2793 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 87](/us/states/tx/districts/house/87.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
