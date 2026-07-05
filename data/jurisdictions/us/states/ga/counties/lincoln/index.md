---
type: Jurisdiction
title: "Lincoln County, GA"
classification: county
fips: "13181"
state: "GA"
demographics:
  population: 7854
  population_under_18: 1472
  population_18_64: 4358
  population_65_plus: 2024
  median_household_income: 56907
  poverty_rate: 17.01
  homeownership_rate: 76.58
  unemployment_rate: 2.84
  median_home_value: 165900
  gini_index: 0.4046
  vacancy_rate: 33.83
  race_white: 5401
  race_black: 2139
  race_asian: 11
  race_native: 0
  hispanic: 114
  bachelors_plus: 1320
districts:
  - to: "us/states/ga/districts/12"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/ga/districts/senate/24"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ga/districts/house/123"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Lincoln County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7854 |
| Under 18 | 1472 |
| 18–64 | 4358 |
| 65+ | 2024 |
| Median household income | 56907 |
| Poverty rate | 17.01 |
| Homeownership rate | 76.58 |
| Unemployment rate | 2.84 |
| Median home value | 165900 |
| Gini index | 0.4046 |
| Vacancy rate | 33.83 |
| White | 5401 |
| Black | 2139 |
| Asian | 11 |
| Native | 0 |
| Hispanic/Latino | 114 |
| Bachelor's or higher | 1320 |

## Districts

- [GA-12](/us/states/ga/districts/12.md) — 100% (congressional)
- [GA Senate District 24](/us/states/ga/districts/senate/24.md) — 100% (state senate)
- [GA House District 123](/us/states/ga/districts/house/123.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
