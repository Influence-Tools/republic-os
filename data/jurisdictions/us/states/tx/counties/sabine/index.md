---
type: Jurisdiction
title: "Sabine County, TX"
classification: county
fips: "48403"
state: "TX"
demographics:
  population: 10023
  population_under_18: 1784
  population_18_64: 5178
  population_65_plus: 3061
  median_household_income: 66585
  poverty_rate: 11.02
  homeownership_rate: 85.67
  unemployment_rate: 4.73
  median_home_value: 153100
  gini_index: 0.4599
  vacancy_rate: 39.6
  race_white: 8590
  race_black: 685
  race_asian: 71
  race_native: 4
  hispanic: 165
  bachelors_plus: 1473
districts:
  - to: "us/states/tx/districts/01"
    rel: in-district
    area_weight: 0.9909
  - to: "us/states/la/districts/04"
    rel: in-district
    area_weight: 0.009
  - to: "us/states/tx/districts/senate/3"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/tx/districts/house/11"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Sabine County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10023 |
| Under 18 | 1784 |
| 18–64 | 5178 |
| 65+ | 3061 |
| Median household income | 66585 |
| Poverty rate | 11.02 |
| Homeownership rate | 85.67 |
| Unemployment rate | 4.73 |
| Median home value | 153100 |
| Gini index | 0.4599 |
| Vacancy rate | 39.6 |
| White | 8590 |
| Black | 685 |
| Asian | 71 |
| Native | 4 |
| Hispanic/Latino | 165 |
| Bachelor's or higher | 1473 |

## Districts

- [TX-01](/us/states/tx/districts/01.md) — 99% (congressional)
- [LA-04](/us/states/la/districts/04.md) — 1% (congressional)
- [TX Senate District 3](/us/states/tx/districts/senate/3.md) — 100% (state senate)
- [TX House District 11](/us/states/tx/districts/house/11.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
