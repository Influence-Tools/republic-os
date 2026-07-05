---
type: Jurisdiction
title: "McMullen County, TX"
classification: county
fips: "48311"
state: "TX"
demographics:
  population: 700
  population_under_18: 279
  population_18_64: 300
  population_65_plus: 121
  median_household_income: 43875
  poverty_rate: 12.29
  homeownership_rate: 78.26
  unemployment_rate: 0.0
  median_home_value: 97100
  gini_index: 0.4412
  vacancy_rate: 40.52
  race_white: 306
  race_black: 0
  race_asian: 0
  race_native: 3
  hispanic: 435
  bachelors_plus: 81
districts:
  - to: "us/states/tx/districts/28"
    rel: in-district
    area_weight: 0.9986
  - to: "us/states/tx/districts/senate/21"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/31"
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

# McMullen County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 700 |
| Under 18 | 279 |
| 18–64 | 300 |
| 65+ | 121 |
| Median household income | 43875 |
| Poverty rate | 12.29 |
| Homeownership rate | 78.26 |
| Unemployment rate | 0.0 |
| Median home value | 97100 |
| Gini index | 0.4412 |
| Vacancy rate | 40.52 |
| White | 306 |
| Black | 0 |
| Asian | 0 |
| Native | 3 |
| Hispanic/Latino | 435 |
| Bachelor's or higher | 81 |

## Districts

- [TX-28](/us/states/tx/districts/28.md) — 100% (congressional)
- [TX Senate District 21](/us/states/tx/districts/senate/21.md) — 100% (state senate)
- [TX House District 31](/us/states/tx/districts/house/31.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
