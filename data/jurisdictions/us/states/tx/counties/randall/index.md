---
type: Jurisdiction
title: "Randall County, TX"
classification: county
fips: "48381"
state: "TX"
demographics:
  population: 146070
  population_under_18: 34813
  population_18_64: 88044
  population_65_plus: 23213
  median_household_income: 83864
  poverty_rate: 9.72
  homeownership_rate: 67.87
  unemployment_rate: 2.91
  median_home_value: 238800
  gini_index: 0.4473
  vacancy_rate: 7.9
  race_white: 108479
  race_black: 5068
  race_asian: 2586
  race_native: 997
  hispanic: 35886
  bachelors_plus: 44059
districts:
  - to: "us/states/tx/districts/13"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/86"
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

# Randall County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 146070 |
| Under 18 | 34813 |
| 18–64 | 88044 |
| 65+ | 23213 |
| Median household income | 83864 |
| Poverty rate | 9.72 |
| Homeownership rate | 67.87 |
| Unemployment rate | 2.91 |
| Median home value | 238800 |
| Gini index | 0.4473 |
| Vacancy rate | 7.9 |
| White | 108479 |
| Black | 5068 |
| Asian | 2586 |
| Native | 997 |
| Hispanic/Latino | 35886 |
| Bachelor's or higher | 44059 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 86](/us/states/tx/districts/house/86.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
