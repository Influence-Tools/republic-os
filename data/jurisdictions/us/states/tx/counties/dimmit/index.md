---
type: Jurisdiction
title: "Dimmit County, TX"
classification: county
fips: "48127"
state: "TX"
demographics:
  population: 8380
  population_under_18: 2178
  population_18_64: 4844
  population_65_plus: 1358
  median_household_income: 38808
  poverty_rate: 41.11
  homeownership_rate: 66.54
  unemployment_rate: 8.42
  median_home_value: 85500
  gini_index: 0.5213
  vacancy_rate: 25.48
  race_white: 1203
  race_black: 94
  race_asian: 46
  race_native: 234
  hispanic: 7303
  bachelors_plus: 661
districts:
  - to: "us/states/tx/districts/23"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tx/districts/senate/21"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/80"
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

# Dimmit County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8380 |
| Under 18 | 2178 |
| 18–64 | 4844 |
| 65+ | 1358 |
| Median household income | 38808 |
| Poverty rate | 41.11 |
| Homeownership rate | 66.54 |
| Unemployment rate | 8.42 |
| Median home value | 85500 |
| Gini index | 0.5213 |
| Vacancy rate | 25.48 |
| White | 1203 |
| Black | 94 |
| Asian | 46 |
| Native | 234 |
| Hispanic/Latino | 7303 |
| Bachelor's or higher | 661 |

## Districts

- [TX-23](/us/states/tx/districts/23.md) — 100% (congressional)
- [TX Senate District 21](/us/states/tx/districts/senate/21.md) — 100% (state senate)
- [TX House District 80](/us/states/tx/districts/house/80.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
