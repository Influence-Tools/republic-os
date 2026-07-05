---
type: Jurisdiction
title: "Ward County, TX"
classification: county
fips: "48475"
state: "TX"
demographics:
  population: 11144
  population_under_18: 3255
  population_18_64: 6379
  population_65_plus: 1510
  median_household_income: 65952
  poverty_rate: 14.92
  homeownership_rate: 78.51
  unemployment_rate: 2.91
  median_home_value: 150700
  gini_index: 0.4365
  vacancy_rate: 15.04
  race_white: 6717
  race_black: 734
  race_asian: 92
  race_native: 97
  hispanic: 6263
  bachelors_plus: 1159
districts:
  - to: "us/states/tx/districts/23"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/tx/districts/house/81"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Ward County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11144 |
| Under 18 | 3255 |
| 18–64 | 6379 |
| 65+ | 1510 |
| Median household income | 65952 |
| Poverty rate | 14.92 |
| Homeownership rate | 78.51 |
| Unemployment rate | 2.91 |
| Median home value | 150700 |
| Gini index | 0.4365 |
| Vacancy rate | 15.04 |
| White | 6717 |
| Black | 734 |
| Asian | 92 |
| Native | 97 |
| Hispanic/Latino | 6263 |
| Bachelor's or higher | 1159 |

## Districts

- [TX-23](/us/states/tx/districts/23.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 81](/us/states/tx/districts/house/81.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
