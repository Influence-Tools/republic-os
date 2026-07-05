---
type: Jurisdiction
title: "Hemphill County, TX"
classification: county
fips: "48211"
state: "TX"
demographics:
  population: 3234
  population_under_18: 663
  population_18_64: 1827
  population_65_plus: 744
  median_household_income: 61563
  poverty_rate: 6.19
  homeownership_rate: 71.07
  unemployment_rate: 5.86
  median_home_value: 205700
  gini_index: 0.415
  vacancy_rate: 16.28
  race_white: 2552
  race_black: 115
  race_asian: 0
  race_native: 19
  hispanic: 1054
  bachelors_plus: 581
districts:
  - to: "us/states/tx/districts/13"
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

# Hemphill County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3234 |
| Under 18 | 663 |
| 18–64 | 1827 |
| 65+ | 744 |
| Median household income | 61563 |
| Poverty rate | 6.19 |
| Homeownership rate | 71.07 |
| Unemployment rate | 5.86 |
| Median home value | 205700 |
| Gini index | 0.415 |
| Vacancy rate | 16.28 |
| White | 2552 |
| Black | 115 |
| Asian | 0 |
| Native | 19 |
| Hispanic/Latino | 1054 |
| Bachelor's or higher | 581 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 88](/us/states/tx/districts/house/88.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
