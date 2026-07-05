---
type: Jurisdiction
title: "Navarro County, TX"
classification: county
fips: "48349"
state: "TX"
demographics:
  population: 54711
  population_under_18: 14591
  population_18_64: 30995
  population_65_plus: 9125
  median_household_income: 63111
  poverty_rate: 17.12
  homeownership_rate: 69.44
  unemployment_rate: 4.43
  median_home_value: 172600
  gini_index: 0.4367
  vacancy_rate: 14.18
  race_white: 31901
  race_black: 5149
  race_asian: 496
  race_native: 297
  hispanic: 17568
  bachelors_plus: 8357
districts:
  - to: "us/states/tx/districts/06"
    rel: in-district
    area_weight: 0.9976
  - to: "us/states/tx/districts/senate/2"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/house/8"
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

# Navarro County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 54711 |
| Under 18 | 14591 |
| 18–64 | 30995 |
| 65+ | 9125 |
| Median household income | 63111 |
| Poverty rate | 17.12 |
| Homeownership rate | 69.44 |
| Unemployment rate | 4.43 |
| Median home value | 172600 |
| Gini index | 0.4367 |
| Vacancy rate | 14.18 |
| White | 31901 |
| Black | 5149 |
| Asian | 496 |
| Native | 297 |
| Hispanic/Latino | 17568 |
| Bachelor's or higher | 8357 |

## Districts

- [TX-06](/us/states/tx/districts/06.md) — 100% (congressional)
- [TX Senate District 2](/us/states/tx/districts/senate/2.md) — 100% (state senate)
- [TX House District 8](/us/states/tx/districts/house/8.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
