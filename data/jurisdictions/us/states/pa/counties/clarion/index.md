---
type: Jurisdiction
title: "Clarion County, PA"
classification: county
fips: "42031"
state: "PA"
demographics:
  population: 37179
  population_under_18: 7058
  population_18_64: 22463
  population_65_plus: 7658
  median_household_income: 62649
  poverty_rate: 13.11
  homeownership_rate: 72.49
  unemployment_rate: 5.07
  median_home_value: 155700
  gini_index: 0.4287
  vacancy_rate: 20.19
  race_white: 35093
  race_black: 625
  race_asian: 255
  race_native: 5
  hispanic: 435
  bachelors_plus: 8160
districts:
  - to: "us/states/pa/districts/15"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/pa/districts/senate/21"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/pa/districts/house/63"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Clarion County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 37179 |
| Under 18 | 7058 |
| 18–64 | 22463 |
| 65+ | 7658 |
| Median household income | 62649 |
| Poverty rate | 13.11 |
| Homeownership rate | 72.49 |
| Unemployment rate | 5.07 |
| Median home value | 155700 |
| Gini index | 0.4287 |
| Vacancy rate | 20.19 |
| White | 35093 |
| Black | 625 |
| Asian | 255 |
| Native | 5 |
| Hispanic/Latino | 435 |
| Bachelor's or higher | 8160 |

## Districts

- [PA-15](/us/states/pa/districts/15.md) — 100% (congressional)
- [PA Senate District 21](/us/states/pa/districts/senate/21.md) — 100% (state senate)
- [PA House District 63](/us/states/pa/districts/house/63.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
