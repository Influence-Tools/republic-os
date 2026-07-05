---
type: Jurisdiction
title: "Robertson County, TX"
classification: county
fips: "48395"
state: "TX"
demographics:
  population: 17167
  population_under_18: 4114
  population_18_64: 9477
  population_65_plus: 3576
  median_household_income: 72236
  poverty_rate: 13.51
  homeownership_rate: 72.41
  unemployment_rate: 7.92
  median_home_value: 185900
  gini_index: 0.454
  vacancy_rate: 22.19
  race_white: 10556
  race_black: 2950
  race_asian: 110
  race_native: 68
  hispanic: 3805
  bachelors_plus: 3442
districts:
  - to: "us/states/tx/districts/17"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/senate/5"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/12"
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

# Robertson County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17167 |
| Under 18 | 4114 |
| 18–64 | 9477 |
| 65+ | 3576 |
| Median household income | 72236 |
| Poverty rate | 13.51 |
| Homeownership rate | 72.41 |
| Unemployment rate | 7.92 |
| Median home value | 185900 |
| Gini index | 0.454 |
| Vacancy rate | 22.19 |
| White | 10556 |
| Black | 2950 |
| Asian | 110 |
| Native | 68 |
| Hispanic/Latino | 3805 |
| Bachelor's or higher | 3442 |

## Districts

- [TX-17](/us/states/tx/districts/17.md) — 100% (congressional)
- [TX Senate District 5](/us/states/tx/districts/senate/5.md) — 100% (state senate)
- [TX House District 12](/us/states/tx/districts/house/12.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
