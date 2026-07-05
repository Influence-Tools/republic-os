---
type: Jurisdiction
title: "Schleicher County, TX"
classification: county
fips: "48413"
state: "TX"
demographics:
  population: 2381
  population_under_18: 548
  population_18_64: 1288
  population_65_plus: 545
  median_household_income: 86694
  poverty_rate: 9.92
  homeownership_rate: 84.34
  unemployment_rate: 5.44
  median_home_value: 122700
  gini_index: 0.4227
  vacancy_rate: 25.1
  race_white: 1162
  race_black: 13
  race_asian: 0
  race_native: 1
  hispanic: 1266
  bachelors_plus: 372
districts:
  - to: "us/states/tx/districts/23"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/tx/districts/house/53"
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

# Schleicher County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2381 |
| Under 18 | 548 |
| 18–64 | 1288 |
| 65+ | 545 |
| Median household income | 86694 |
| Poverty rate | 9.92 |
| Homeownership rate | 84.34 |
| Unemployment rate | 5.44 |
| Median home value | 122700 |
| Gini index | 0.4227 |
| Vacancy rate | 25.1 |
| White | 1162 |
| Black | 13 |
| Asian | 0 |
| Native | 1 |
| Hispanic/Latino | 1266 |
| Bachelor's or higher | 372 |

## Districts

- [TX-23](/us/states/tx/districts/23.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 53](/us/states/tx/districts/house/53.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
