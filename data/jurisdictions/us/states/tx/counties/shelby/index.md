---
type: Jurisdiction
title: "Shelby County, TX"
classification: county
fips: "48419"
state: "TX"
demographics:
  population: 24155
  population_under_18: 6280
  population_18_64: 13418
  population_65_plus: 4457
  median_household_income: 49776
  poverty_rate: 20.58
  homeownership_rate: 74.01
  unemployment_rate: 4.07
  median_home_value: 101500
  gini_index: 0.4752
  vacancy_rate: 19.15
  race_white: 15508
  race_black: 3649
  race_asian: 9
  race_native: 493
  hispanic: 4802
  bachelors_plus: 3032
districts:
  - to: "us/states/tx/districts/01"
    rel: in-district
    area_weight: 0.9955
  - to: "us/states/tx/districts/senate/3"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/tx/districts/house/11"
    rel: in-district
    area_weight: 0.9992
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Shelby County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 24155 |
| Under 18 | 6280 |
| 18–64 | 13418 |
| 65+ | 4457 |
| Median household income | 49776 |
| Poverty rate | 20.58 |
| Homeownership rate | 74.01 |
| Unemployment rate | 4.07 |
| Median home value | 101500 |
| Gini index | 0.4752 |
| Vacancy rate | 19.15 |
| White | 15508 |
| Black | 3649 |
| Asian | 9 |
| Native | 493 |
| Hispanic/Latino | 4802 |
| Bachelor's or higher | 3032 |

## Districts

- [TX-01](/us/states/tx/districts/01.md) — 100% (congressional)
- [TX Senate District 3](/us/states/tx/districts/senate/3.md) — 100% (state senate)
- [TX House District 11](/us/states/tx/districts/house/11.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
