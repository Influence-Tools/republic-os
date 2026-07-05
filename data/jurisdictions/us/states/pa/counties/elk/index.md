---
type: Jurisdiction
title: "Elk County, PA"
classification: county
fips: "42047"
state: "PA"
demographics:
  population: 30506
  population_under_18: 5785
  population_18_64: 17355
  population_65_plus: 7366
  median_household_income: 66380
  poverty_rate: 8.69
  homeownership_rate: 79.55
  unemployment_rate: 5.65
  median_home_value: 133600
  gini_index: 0.4213
  vacancy_rate: 21.06
  race_white: 28966
  race_black: 184
  race_asian: 130
  race_native: 4
  hispanic: 314
  bachelors_plus: 6398
districts:
  - to: "us/states/pa/districts/15"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/pa/districts/senate/25"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/pa/districts/house/75"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Elk County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 30506 |
| Under 18 | 5785 |
| 18–64 | 17355 |
| 65+ | 7366 |
| Median household income | 66380 |
| Poverty rate | 8.69 |
| Homeownership rate | 79.55 |
| Unemployment rate | 5.65 |
| Median home value | 133600 |
| Gini index | 0.4213 |
| Vacancy rate | 21.06 |
| White | 28966 |
| Black | 184 |
| Asian | 130 |
| Native | 4 |
| Hispanic/Latino | 314 |
| Bachelor's or higher | 6398 |

## Districts

- [PA-15](/us/states/pa/districts/15.md) — 100% (congressional)
- [PA Senate District 25](/us/states/pa/districts/senate/25.md) — 100% (state senate)
- [PA House District 75](/us/states/pa/districts/house/75.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
