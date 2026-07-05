---
type: Jurisdiction
title: "Smith County, TX"
classification: county
fips: "48423"
state: "TX"
demographics:
  population: 241740
  population_under_18: 58485
  population_18_64: 141097
  population_65_plus: 42158
  median_household_income: 74192
  poverty_rate: 11.57
  homeownership_rate: 68.82
  unemployment_rate: 4.45
  median_home_value: 240700
  gini_index: 0.4479
  vacancy_rate: 16.59
  race_white: 160640
  race_black: 39393
  race_asian: 4265
  race_native: 991
  hispanic: 50591
  bachelors_plus: 61495
districts:
  - to: "us/states/tx/districts/01"
    rel: in-district
    area_weight: 0.9968
  - to: "us/states/tx/districts/senate/1"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/house/6"
    rel: in-district
    area_weight: 0.5003
  - to: "us/states/tx/districts/house/5"
    rel: in-district
    area_weight: 0.4995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Smith County, TX

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 241740 |
| Under 18 | 58485 |
| 18–64 | 141097 |
| 65+ | 42158 |
| Median household income | 74192 |
| Poverty rate | 11.57 |
| Homeownership rate | 68.82 |
| Unemployment rate | 4.45 |
| Median home value | 240700 |
| Gini index | 0.4479 |
| Vacancy rate | 16.59 |
| White | 160640 |
| Black | 39393 |
| Asian | 4265 |
| Native | 991 |
| Hispanic/Latino | 50591 |
| Bachelor's or higher | 61495 |

## Districts

- [TX-01](/us/states/tx/districts/01.md) — 100% (congressional)
- [TX Senate District 1](/us/states/tx/districts/senate/1.md) — 100% (state senate)
- [TX House District 6](/us/states/tx/districts/house/6.md) — 50% (state house)
- [TX House District 5](/us/states/tx/districts/house/5.md) — 50% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
