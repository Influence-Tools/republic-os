---
type: Jurisdiction
title: "Llano County, TX"
classification: county
fips: "48299"
state: "TX"
demographics:
  population: 22424
  population_under_18: 3464
  population_18_64: 10661
  population_65_plus: 8299
  median_household_income: 67530
  poverty_rate: 12.0
  homeownership_rate: 76.52
  unemployment_rate: 4.36
  median_home_value: 356500
  gini_index: 0.5113
  vacancy_rate: 31.82
  race_white: 19606
  race_black: 65
  race_asian: 142
  race_native: 53
  hispanic: 2995
  bachelors_plus: 7512
districts:
  - to: "us/states/tx/districts/11"
    rel: in-district
    area_weight: 0.9969
  - to: "us/states/tx/districts/senate/24"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/house/53"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Llano County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 22424 |
| Under 18 | 3464 |
| 18–64 | 10661 |
| 65+ | 8299 |
| Median household income | 67530 |
| Poverty rate | 12.0 |
| Homeownership rate | 76.52 |
| Unemployment rate | 4.36 |
| Median home value | 356500 |
| Gini index | 0.5113 |
| Vacancy rate | 31.82 |
| White | 19606 |
| Black | 65 |
| Asian | 142 |
| Native | 53 |
| Hispanic/Latino | 2995 |
| Bachelor's or higher | 7512 |

## Districts

- [TX-11](/us/states/tx/districts/11.md) — 100% (congressional)
- [TX Senate District 24](/us/states/tx/districts/senate/24.md) — 100% (state senate)
- [TX House District 53](/us/states/tx/districts/house/53.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
