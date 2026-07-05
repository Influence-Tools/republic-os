---
type: Jurisdiction
title: "Panola County, TX"
classification: county
fips: "48365"
state: "TX"
demographics:
  population: 22726
  population_under_18: 5244
  population_18_64: 12869
  population_65_plus: 4613
  median_household_income: 64894
  poverty_rate: 11.19
  homeownership_rate: 79.92
  unemployment_rate: 2.48
  median_home_value: 158100
  gini_index: 0.4729
  vacancy_rate: 18.01
  race_white: 16526
  race_black: 2575
  race_asian: 121
  race_native: 6
  hispanic: 2359
  bachelors_plus: 3568
districts:
  - to: "us/states/tx/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/senate/1"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/11"
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

# Panola County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 22726 |
| Under 18 | 5244 |
| 18–64 | 12869 |
| 65+ | 4613 |
| Median household income | 64894 |
| Poverty rate | 11.19 |
| Homeownership rate | 79.92 |
| Unemployment rate | 2.48 |
| Median home value | 158100 |
| Gini index | 0.4729 |
| Vacancy rate | 18.01 |
| White | 16526 |
| Black | 2575 |
| Asian | 121 |
| Native | 6 |
| Hispanic/Latino | 2359 |
| Bachelor's or higher | 3568 |

## Districts

- [TX-01](/us/states/tx/districts/01.md) — 100% (congressional)
- [TX Senate District 1](/us/states/tx/districts/senate/1.md) — 100% (state senate)
- [TX House District 11](/us/states/tx/districts/house/11.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
