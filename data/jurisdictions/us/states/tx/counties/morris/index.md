---
type: Jurisdiction
title: "Morris County, TX"
classification: county
fips: "48343"
state: "TX"
demographics:
  population: 12076
  population_under_18: 2777
  population_18_64: 6656
  population_65_plus: 2643
  median_household_income: 58645
  poverty_rate: 19.46
  homeownership_rate: 73.89
  unemployment_rate: 7.11
  median_home_value: 120400
  gini_index: 0.3987
  vacancy_rate: 15.91
  race_white: 7586
  race_black: 2701
  race_asian: 144
  race_native: 88
  hispanic: 1355
  bachelors_plus: 1719
districts:
  - to: "us/states/tx/districts/01"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/tx/districts/senate/1"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/1"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Morris County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12076 |
| Under 18 | 2777 |
| 18–64 | 6656 |
| 65+ | 2643 |
| Median household income | 58645 |
| Poverty rate | 19.46 |
| Homeownership rate | 73.89 |
| Unemployment rate | 7.11 |
| Median home value | 120400 |
| Gini index | 0.3987 |
| Vacancy rate | 15.91 |
| White | 7586 |
| Black | 2701 |
| Asian | 144 |
| Native | 88 |
| Hispanic/Latino | 1355 |
| Bachelor's or higher | 1719 |

## Districts

- [TX-01](/us/states/tx/districts/01.md) — 100% (congressional)
- [TX Senate District 1](/us/states/tx/districts/senate/1.md) — 100% (state senate)
- [TX House District 1](/us/states/tx/districts/house/1.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
