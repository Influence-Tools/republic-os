---
type: Jurisdiction
title: "Val Verde County, TX"
classification: county
fips: "48465"
state: "TX"
demographics:
  population: 47741
  population_under_18: 13288
  population_18_64: 27806
  population_65_plus: 6647
  median_household_income: 66100
  poverty_rate: 16.57
  homeownership_rate: 69.05
  unemployment_rate: 5.94
  median_home_value: 164600
  gini_index: 0.4375
  vacancy_rate: 10.16
  race_white: 23381
  race_black: 672
  race_asian: 381
  race_native: 242
  hispanic: 38761
  bachelors_plus: 9357
districts:
  - to: "us/states/tx/districts/23"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/tx/districts/senate/19"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/74"
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

# Val Verde County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 47741 |
| Under 18 | 13288 |
| 18–64 | 27806 |
| 65+ | 6647 |
| Median household income | 66100 |
| Poverty rate | 16.57 |
| Homeownership rate | 69.05 |
| Unemployment rate | 5.94 |
| Median home value | 164600 |
| Gini index | 0.4375 |
| Vacancy rate | 10.16 |
| White | 23381 |
| Black | 672 |
| Asian | 381 |
| Native | 242 |
| Hispanic/Latino | 38761 |
| Bachelor's or higher | 9357 |

## Districts

- [TX-23](/us/states/tx/districts/23.md) — 100% (congressional)
- [TX Senate District 19](/us/states/tx/districts/senate/19.md) — 100% (state senate)
- [TX House District 74](/us/states/tx/districts/house/74.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
