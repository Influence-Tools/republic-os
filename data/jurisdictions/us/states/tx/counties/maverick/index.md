---
type: Jurisdiction
title: "Maverick County, TX"
classification: county
fips: "48323"
state: "TX"
demographics:
  population: 58082
  population_under_18: 17898
  population_18_64: 33209
  population_65_plus: 6975
  median_household_income: 49568
  poverty_rate: 22.78
  homeownership_rate: 70.53
  unemployment_rate: 7.66
  median_home_value: 158700
  gini_index: 0.4556
  vacancy_rate: 11.57
  race_white: 9998
  race_black: 103
  race_asian: 270
  race_native: 1005
  hispanic: 55049
  bachelors_plus: 6269
districts:
  - to: "us/states/tx/districts/23"
    rel: in-district
    area_weight: 0.9989
  - to: "us/states/tx/districts/senate/19"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tx/districts/house/74"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Maverick County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 58082 |
| Under 18 | 17898 |
| 18–64 | 33209 |
| 65+ | 6975 |
| Median household income | 49568 |
| Poverty rate | 22.78 |
| Homeownership rate | 70.53 |
| Unemployment rate | 7.66 |
| Median home value | 158700 |
| Gini index | 0.4556 |
| Vacancy rate | 11.57 |
| White | 9998 |
| Black | 103 |
| Asian | 270 |
| Native | 1005 |
| Hispanic/Latino | 55049 |
| Bachelor's or higher | 6269 |

## Districts

- [TX-23](/us/states/tx/districts/23.md) — 100% (congressional)
- [TX Senate District 19](/us/states/tx/districts/senate/19.md) — 100% (state senate)
- [TX House District 74](/us/states/tx/districts/house/74.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
