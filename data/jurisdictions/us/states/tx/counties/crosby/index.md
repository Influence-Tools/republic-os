---
type: Jurisdiction
title: "Crosby County, TX"
classification: county
fips: "48107"
state: "TX"
demographics:
  population: 5041
  population_under_18: 1287
  population_18_64: 2787
  population_65_plus: 967
  median_household_income: 52188
  poverty_rate: 20.08
  homeownership_rate: 68.84
  unemployment_rate: 8.25
  median_home_value: 80900
  gini_index: 0.5185
  vacancy_rate: 27.45
  race_white: 3319
  race_black: 175
  race_asian: 35
  race_native: 11
  hispanic: 2837
  bachelors_plus: 604
districts:
  - to: "us/states/tx/districts/19"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/83"
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

# Crosby County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5041 |
| Under 18 | 1287 |
| 18–64 | 2787 |
| 65+ | 967 |
| Median household income | 52188 |
| Poverty rate | 20.08 |
| Homeownership rate | 68.84 |
| Unemployment rate | 8.25 |
| Median home value | 80900 |
| Gini index | 0.5185 |
| Vacancy rate | 27.45 |
| White | 3319 |
| Black | 175 |
| Asian | 35 |
| Native | 11 |
| Hispanic/Latino | 2837 |
| Bachelor's or higher | 604 |

## Districts

- [TX-19](/us/states/tx/districts/19.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 83](/us/states/tx/districts/house/83.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
