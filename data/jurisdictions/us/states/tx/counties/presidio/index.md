---
type: Jurisdiction
title: "Presidio County, TX"
classification: county
fips: "48377"
state: "TX"
demographics:
  population: 5930
  population_under_18: 1521
  population_18_64: 3252
  population_65_plus: 1157
  median_household_income: 43802
  poverty_rate: 32.0
  homeownership_rate: 77.34
  unemployment_rate: 6.7
  median_home_value: 121300
  gini_index: 0.527
  vacancy_rate: 26.12
  race_white: 2683
  race_black: 42
  race_asian: 1
  race_native: 45
  hispanic: 4715
  bachelors_plus: 1362
districts:
  - to: "us/states/tx/districts/23"
    rel: in-district
    area_weight: 0.9981
  - to: "us/states/tx/districts/senate/29"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tx/districts/house/74"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Presidio County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5930 |
| Under 18 | 1521 |
| 18–64 | 3252 |
| 65+ | 1157 |
| Median household income | 43802 |
| Poverty rate | 32.0 |
| Homeownership rate | 77.34 |
| Unemployment rate | 6.7 |
| Median home value | 121300 |
| Gini index | 0.527 |
| Vacancy rate | 26.12 |
| White | 2683 |
| Black | 42 |
| Asian | 1 |
| Native | 45 |
| Hispanic/Latino | 4715 |
| Bachelor's or higher | 1362 |

## Districts

- [TX-23](/us/states/tx/districts/23.md) — 100% (congressional)
- [TX Senate District 29](/us/states/tx/districts/senate/29.md) — 100% (state senate)
- [TX House District 74](/us/states/tx/districts/house/74.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
