---
type: Jurisdiction
title: "Cherokee County, TX"
classification: county
fips: "48073"
state: "TX"
demographics:
  population: 51886
  population_under_18: 13051
  population_18_64: 29308
  population_65_plus: 9527
  median_household_income: 61261
  poverty_rate: 18.16
  homeownership_rate: 73.98
  unemployment_rate: 5.2
  median_home_value: 169300
  gini_index: 0.4628
  vacancy_rate: 13.62
  race_white: 33771
  race_black: 6666
  race_asian: 231
  race_native: 791
  hispanic: 12422
  bachelors_plus: 8759
districts:
  - to: "us/states/tx/districts/06"
    rel: in-district
    area_weight: 0.9965
  - to: "us/states/tx/districts/senate/3"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/8"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Cherokee County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 51886 |
| Under 18 | 13051 |
| 18–64 | 29308 |
| 65+ | 9527 |
| Median household income | 61261 |
| Poverty rate | 18.16 |
| Homeownership rate | 73.98 |
| Unemployment rate | 5.2 |
| Median home value | 169300 |
| Gini index | 0.4628 |
| Vacancy rate | 13.62 |
| White | 33771 |
| Black | 6666 |
| Asian | 231 |
| Native | 791 |
| Hispanic/Latino | 12422 |
| Bachelor's or higher | 8759 |

## Districts

- [TX-06](/us/states/tx/districts/06.md) — 100% (congressional)
- [TX Senate District 3](/us/states/tx/districts/senate/3.md) — 100% (state senate)
- [TX House District 8](/us/states/tx/districts/house/8.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
