---
type: Jurisdiction
title: "Delta County, TX"
classification: county
fips: "48119"
state: "TX"
demographics:
  population: 5438
  population_under_18: 1308
  population_18_64: 3020
  population_65_plus: 1110
  median_household_income: 66575
  poverty_rate: 11.36
  homeownership_rate: 82.83
  unemployment_rate: 4.28
  median_home_value: 164300
  gini_index: 0.4225
  vacancy_rate: 11.31
  race_white: 4419
  race_black: 440
  race_asian: 24
  race_native: 13
  hispanic: 499
  bachelors_plus: 760
districts:
  - to: "us/states/tx/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/1"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/62"
    rel: in-district
    area_weight: 0.9981
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Delta County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5438 |
| Under 18 | 1308 |
| 18–64 | 3020 |
| 65+ | 1110 |
| Median household income | 66575 |
| Poverty rate | 11.36 |
| Homeownership rate | 82.83 |
| Unemployment rate | 4.28 |
| Median home value | 164300 |
| Gini index | 0.4225 |
| Vacancy rate | 11.31 |
| White | 4419 |
| Black | 440 |
| Asian | 24 |
| Native | 13 |
| Hispanic/Latino | 499 |
| Bachelor's or higher | 760 |

## Districts

- [TX-04](/us/states/tx/districts/04.md) — 100% (congressional)
- [TX Senate District 1](/us/states/tx/districts/senate/1.md) — 100% (state senate)
- [TX House District 62](/us/states/tx/districts/house/62.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
