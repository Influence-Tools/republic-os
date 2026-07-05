---
type: Jurisdiction
title: "Sutton County, TX"
classification: county
fips: "48435"
state: "TX"
demographics:
  population: 3277
  population_under_18: 769
  population_18_64: 1877
  population_65_plus: 631
  median_household_income: 78906
  poverty_rate: 4.51
  homeownership_rate: 76.04
  unemployment_rate: 1.88
  median_home_value: 155700
  gini_index: 0.3887
  vacancy_rate: 27.92
  race_white: 1489
  race_black: 4
  race_asian: 0
  race_native: 22
  hispanic: 2077
  bachelors_plus: 517
districts:
  - to: "us/states/tx/districts/23"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/24"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/tx/districts/house/53"
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

# Sutton County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3277 |
| Under 18 | 769 |
| 18–64 | 1877 |
| 65+ | 631 |
| Median household income | 78906 |
| Poverty rate | 4.51 |
| Homeownership rate | 76.04 |
| Unemployment rate | 1.88 |
| Median home value | 155700 |
| Gini index | 0.3887 |
| Vacancy rate | 27.92 |
| White | 1489 |
| Black | 4 |
| Asian | 0 |
| Native | 22 |
| Hispanic/Latino | 2077 |
| Bachelor's or higher | 517 |

## Districts

- [TX-23](/us/states/tx/districts/23.md) — 100% (congressional)
- [TX Senate District 24](/us/states/tx/districts/senate/24.md) — 100% (state senate)
- [TX House District 53](/us/states/tx/districts/house/53.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
