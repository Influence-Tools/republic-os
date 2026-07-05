---
type: Jurisdiction
title: "Cherokee County, SC"
classification: county
fips: "45021"
state: "SC"
demographics:
  population: 56647
  population_under_18: 12874
  population_18_64: 33842
  population_65_plus: 9931
  median_household_income: 50288
  poverty_rate: 18.42
  homeownership_rate: 73.83
  unemployment_rate: 6.26
  median_home_value: 142000
  gini_index: 0.4545
  vacancy_rate: 12.27
  race_white: 39840
  race_black: 10628
  race_asian: 324
  race_native: 141
  hispanic: 3137
  bachelors_plus: 9885
districts:
  - to: "us/states/sc/districts/05"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/sc/districts/senate/14"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/sc/districts/house/29"
    rel: in-district
    area_weight: 0.5016
  - to: "us/states/sc/districts/house/30"
    rel: in-district
    area_weight: 0.4978
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Cherokee County, SC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 56647 |
| Under 18 | 12874 |
| 18–64 | 33842 |
| 65+ | 9931 |
| Median household income | 50288 |
| Poverty rate | 18.42 |
| Homeownership rate | 73.83 |
| Unemployment rate | 6.26 |
| Median home value | 142000 |
| Gini index | 0.4545 |
| Vacancy rate | 12.27 |
| White | 39840 |
| Black | 10628 |
| Asian | 324 |
| Native | 141 |
| Hispanic/Latino | 3137 |
| Bachelor's or higher | 9885 |

## Districts

- [SC-05](/us/states/sc/districts/05.md) — 100% (congressional)
- [SC Senate District 14](/us/states/sc/districts/senate/14.md) — 100% (state senate)
- [SC House District 29](/us/states/sc/districts/house/29.md) — 50% (state house)
- [SC House District 30](/us/states/sc/districts/house/30.md) — 50% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
