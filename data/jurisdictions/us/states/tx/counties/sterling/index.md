---
type: Jurisdiction
title: "Sterling County, TX"
classification: county
fips: "48431"
state: "TX"
demographics:
  population: 1468
  population_under_18: 509
  population_18_64: 729
  population_65_plus: 230
  median_household_income: 64954
  poverty_rate: 4.32
  homeownership_rate: 77.69
  unemployment_rate: 2.14
  median_home_value: 147000
  gini_index: 0.4118
  vacancy_rate: 23.85
  race_white: 1064
  race_black: 2
  race_asian: 2
  race_native: 4
  hispanic: 524
  bachelors_plus: 286
districts:
  - to: "us/states/tx/districts/11"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/72"
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

# Sterling County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1468 |
| Under 18 | 509 |
| 18–64 | 729 |
| 65+ | 230 |
| Median household income | 64954 |
| Poverty rate | 4.32 |
| Homeownership rate | 77.69 |
| Unemployment rate | 2.14 |
| Median home value | 147000 |
| Gini index | 0.4118 |
| Vacancy rate | 23.85 |
| White | 1064 |
| Black | 2 |
| Asian | 2 |
| Native | 4 |
| Hispanic/Latino | 524 |
| Bachelor's or higher | 286 |

## Districts

- [TX-11](/us/states/tx/districts/11.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 72](/us/states/tx/districts/house/72.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
