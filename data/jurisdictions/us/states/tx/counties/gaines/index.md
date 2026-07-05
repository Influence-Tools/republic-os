---
type: Jurisdiction
title: "Gaines County, TX"
classification: county
fips: "48165"
state: "TX"
demographics:
  population: 22232
  population_under_18: 7961
  population_18_64: 12120
  population_65_plus: 2151
  median_household_income: 74132
  poverty_rate: 6.83
  homeownership_rate: 74.63
  unemployment_rate: 2.43
  median_home_value: 200700
  gini_index: 0.4284
  vacancy_rate: 10.23
  race_white: 15601
  race_black: 460
  race_asian: 124
  race_native: 0
  hispanic: 8954
  bachelors_plus: 1628
districts:
  - to: "us/states/tx/districts/19"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/88"
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

# Gaines County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 22232 |
| Under 18 | 7961 |
| 18–64 | 12120 |
| 65+ | 2151 |
| Median household income | 74132 |
| Poverty rate | 6.83 |
| Homeownership rate | 74.63 |
| Unemployment rate | 2.43 |
| Median home value | 200700 |
| Gini index | 0.4284 |
| Vacancy rate | 10.23 |
| White | 15601 |
| Black | 460 |
| Asian | 124 |
| Native | 0 |
| Hispanic/Latino | 8954 |
| Bachelor's or higher | 1628 |

## Districts

- [TX-19](/us/states/tx/districts/19.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 88](/us/states/tx/districts/house/88.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
