---
type: Jurisdiction
title: "Sherman County, TX"
classification: county
fips: "48421"
state: "TX"
demographics:
  population: 2295
  population_under_18: 399
  population_18_64: 1474
  population_65_plus: 422
  median_household_income: 61250
  poverty_rate: 10.36
  homeownership_rate: 76.28
  unemployment_rate: 1.93
  median_home_value: 146900
  gini_index: 0.4467
  vacancy_rate: 25.73
  race_white: 1318
  race_black: 3
  race_asian: 12
  race_native: 1
  hispanic: 1070
  bachelors_plus: 621
districts:
  - to: "us/states/tx/districts/13"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/87"
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

# Sherman County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2295 |
| Under 18 | 399 |
| 18–64 | 1474 |
| 65+ | 422 |
| Median household income | 61250 |
| Poverty rate | 10.36 |
| Homeownership rate | 76.28 |
| Unemployment rate | 1.93 |
| Median home value | 146900 |
| Gini index | 0.4467 |
| Vacancy rate | 25.73 |
| White | 1318 |
| Black | 3 |
| Asian | 12 |
| Native | 1 |
| Hispanic/Latino | 1070 |
| Bachelor's or higher | 621 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 87](/us/states/tx/districts/house/87.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
