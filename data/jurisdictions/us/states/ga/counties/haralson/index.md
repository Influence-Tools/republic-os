---
type: Jurisdiction
title: "Haralson County, GA"
classification: county
fips: "13143"
state: "GA"
demographics:
  population: 31285
  population_under_18: 7429
  population_18_64: 19016
  population_65_plus: 4840
  median_household_income: 72127
  poverty_rate: 15.35
  homeownership_rate: 71.61
  unemployment_rate: 4.45
  median_home_value: 227500
  gini_index: 0.445
  vacancy_rate: 8.38
  race_white: 28190
  race_black: 1550
  race_asian: 203
  race_native: 10
  hispanic: 665
  bachelors_plus: 4880
districts:
  - to: "us/states/ga/districts/03"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ga/districts/senate/30"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ga/districts/house/18"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Haralson County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 31285 |
| Under 18 | 7429 |
| 18–64 | 19016 |
| 65+ | 4840 |
| Median household income | 72127 |
| Poverty rate | 15.35 |
| Homeownership rate | 71.61 |
| Unemployment rate | 4.45 |
| Median home value | 227500 |
| Gini index | 0.445 |
| Vacancy rate | 8.38 |
| White | 28190 |
| Black | 1550 |
| Asian | 203 |
| Native | 10 |
| Hispanic/Latino | 665 |
| Bachelor's or higher | 4880 |

## Districts

- [GA-03](/us/states/ga/districts/03.md) — 100% (congressional)
- [GA Senate District 30](/us/states/ga/districts/senate/30.md) — 100% (state senate)
- [GA House District 18](/us/states/ga/districts/house/18.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
