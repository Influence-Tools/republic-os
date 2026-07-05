---
type: Jurisdiction
title: "Stephens County, TX"
classification: county
fips: "48429"
state: "TX"
demographics:
  population: 9351
  population_under_18: 1941
  population_18_64: 5506
  population_65_plus: 1904
  median_household_income: 58008
  poverty_rate: 14.65
  homeownership_rate: 79.16
  unemployment_rate: 5.45
  median_home_value: 110200
  gini_index: 0.4249
  vacancy_rate: 22.52
  race_white: 7308
  race_black: 289
  race_asian: 98
  race_native: 55
  hispanic: 2349
  bachelors_plus: 1492
districts:
  - to: "us/states/tx/districts/25"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/10"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/60"
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

# Stephens County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9351 |
| Under 18 | 1941 |
| 18–64 | 5506 |
| 65+ | 1904 |
| Median household income | 58008 |
| Poverty rate | 14.65 |
| Homeownership rate | 79.16 |
| Unemployment rate | 5.45 |
| Median home value | 110200 |
| Gini index | 0.4249 |
| Vacancy rate | 22.52 |
| White | 7308 |
| Black | 289 |
| Asian | 98 |
| Native | 55 |
| Hispanic/Latino | 2349 |
| Bachelor's or higher | 1492 |

## Districts

- [TX-25](/us/states/tx/districts/25.md) — 100% (congressional)
- [TX Senate District 10](/us/states/tx/districts/senate/10.md) — 100% (state senate)
- [TX House District 60](/us/states/tx/districts/house/60.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
