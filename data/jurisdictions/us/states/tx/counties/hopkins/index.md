---
type: Jurisdiction
title: "Hopkins County, TX"
classification: county
fips: "48223"
state: "TX"
demographics:
  population: 37784
  population_under_18: 9172
  population_18_64: 21538
  population_65_plus: 7074
  median_household_income: 70888
  poverty_rate: 11.88
  homeownership_rate: 71.11
  unemployment_rate: 4.01
  median_home_value: 221100
  gini_index: 0.4691
  vacancy_rate: 11.84
  race_white: 30095
  race_black: 2652
  race_asian: 327
  race_native: 227
  hispanic: 7066
  bachelors_plus: 7513
districts:
  - to: "us/states/tx/districts/04"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/tx/districts/senate/1"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/2"
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

# Hopkins County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 37784 |
| Under 18 | 9172 |
| 18–64 | 21538 |
| 65+ | 7074 |
| Median household income | 70888 |
| Poverty rate | 11.88 |
| Homeownership rate | 71.11 |
| Unemployment rate | 4.01 |
| Median home value | 221100 |
| Gini index | 0.4691 |
| Vacancy rate | 11.84 |
| White | 30095 |
| Black | 2652 |
| Asian | 327 |
| Native | 227 |
| Hispanic/Latino | 7066 |
| Bachelor's or higher | 7513 |

## Districts

- [TX-04](/us/states/tx/districts/04.md) — 100% (congressional)
- [TX Senate District 1](/us/states/tx/districts/senate/1.md) — 100% (state senate)
- [TX House District 2](/us/states/tx/districts/house/2.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
