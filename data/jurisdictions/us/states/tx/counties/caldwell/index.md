---
type: Jurisdiction
title: "Caldwell County, TX"
classification: county
fips: "48055"
state: "TX"
demographics:
  population: 48669
  population_under_18: 11272
  population_18_64: 29951
  population_65_plus: 7446
  median_household_income: 69758
  poverty_rate: 13.18
  homeownership_rate: 75.31
  unemployment_rate: 3.41
  median_home_value: 240500
  gini_index: 0.4087
  vacancy_rate: 5.32
  race_white: 22908
  race_black: 2372
  race_asian: 370
  race_native: 575
  hispanic: 27728
  bachelors_plus: 8107
districts:
  - to: "us/states/tx/districts/27"
    rel: in-district
    area_weight: 0.996
  - to: "us/states/tx/districts/senate/21"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/house/17"
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

# Caldwell County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 48669 |
| Under 18 | 11272 |
| 18–64 | 29951 |
| 65+ | 7446 |
| Median household income | 69758 |
| Poverty rate | 13.18 |
| Homeownership rate | 75.31 |
| Unemployment rate | 3.41 |
| Median home value | 240500 |
| Gini index | 0.4087 |
| Vacancy rate | 5.32 |
| White | 22908 |
| Black | 2372 |
| Asian | 370 |
| Native | 575 |
| Hispanic/Latino | 27728 |
| Bachelor's or higher | 8107 |

## Districts

- [TX-27](/us/states/tx/districts/27.md) — 100% (congressional)
- [TX Senate District 21](/us/states/tx/districts/senate/21.md) — 100% (state senate)
- [TX House District 17](/us/states/tx/districts/house/17.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
