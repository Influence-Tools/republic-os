---
type: Jurisdiction
title: "Trinity County, TX"
classification: county
fips: "48455"
state: "TX"
demographics:
  population: 14046
  population_under_18: 2719
  population_18_64: 7512
  population_65_plus: 3815
  median_household_income: 52018
  poverty_rate: 17.61
  homeownership_rate: 79.37
  unemployment_rate: 6.52
  median_home_value: 119500
  gini_index: 0.4779
  vacancy_rate: 27.0
  race_white: 11070
  race_black: 1141
  race_asian: 26
  race_native: 22
  hispanic: 1569
  bachelors_plus: 2153
districts:
  - to: "us/states/tx/districts/17"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tx/districts/senate/3"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/9"
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

# Trinity County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14046 |
| Under 18 | 2719 |
| 18–64 | 7512 |
| 65+ | 3815 |
| Median household income | 52018 |
| Poverty rate | 17.61 |
| Homeownership rate | 79.37 |
| Unemployment rate | 6.52 |
| Median home value | 119500 |
| Gini index | 0.4779 |
| Vacancy rate | 27.0 |
| White | 11070 |
| Black | 1141 |
| Asian | 26 |
| Native | 22 |
| Hispanic/Latino | 1569 |
| Bachelor's or higher | 2153 |

## Districts

- [TX-17](/us/states/tx/districts/17.md) — 100% (congressional)
- [TX Senate District 3](/us/states/tx/districts/senate/3.md) — 100% (state senate)
- [TX House District 9](/us/states/tx/districts/house/9.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
