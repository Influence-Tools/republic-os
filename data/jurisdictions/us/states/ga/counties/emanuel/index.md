---
type: Jurisdiction
title: "Emanuel County, GA"
classification: county
fips: "13107"
state: "GA"
demographics:
  population: 23026
  population_under_18: 5732
  population_18_64: 13518
  population_65_plus: 3776
  median_household_income: 52772
  poverty_rate: 25.69
  homeownership_rate: 60.78
  unemployment_rate: 8.85
  median_home_value: 94700
  gini_index: 0.4395
  vacancy_rate: 17.18
  race_white: 13461
  race_black: 7339
  race_asian: 199
  race_native: 10
  hispanic: 1112
  bachelors_plus: 2853
districts:
  - to: "us/states/ga/districts/12"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/senate/23"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ga/districts/house/158"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Emanuel County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 23026 |
| Under 18 | 5732 |
| 18–64 | 13518 |
| 65+ | 3776 |
| Median household income | 52772 |
| Poverty rate | 25.69 |
| Homeownership rate | 60.78 |
| Unemployment rate | 8.85 |
| Median home value | 94700 |
| Gini index | 0.4395 |
| Vacancy rate | 17.18 |
| White | 13461 |
| Black | 7339 |
| Asian | 199 |
| Native | 10 |
| Hispanic/Latino | 1112 |
| Bachelor's or higher | 2853 |

## Districts

- [GA-12](/us/states/ga/districts/12.md) — 100% (congressional)
- [GA Senate District 23](/us/states/ga/districts/senate/23.md) — 100% (state senate)
- [GA House District 158](/us/states/ga/districts/house/158.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
