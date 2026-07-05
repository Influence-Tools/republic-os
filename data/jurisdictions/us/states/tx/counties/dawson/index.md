---
type: Jurisdiction
title: "Dawson County, TX"
classification: county
fips: "48115"
state: "TX"
demographics:
  population: 12134
  population_under_18: 2945
  population_18_64: 7502
  population_65_plus: 1687
  median_household_income: 54360
  poverty_rate: 19.57
  homeownership_rate: 70.64
  unemployment_rate: 6.39
  median_home_value: 103400
  gini_index: 0.5035
  vacancy_rate: 17.54
  race_white: 6001
  race_black: 815
  race_asian: 63
  race_native: 23
  hispanic: 6770
  bachelors_plus: 1225
districts:
  - to: "us/states/tx/districts/19"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/82"
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

# Dawson County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12134 |
| Under 18 | 2945 |
| 18–64 | 7502 |
| 65+ | 1687 |
| Median household income | 54360 |
| Poverty rate | 19.57 |
| Homeownership rate | 70.64 |
| Unemployment rate | 6.39 |
| Median home value | 103400 |
| Gini index | 0.5035 |
| Vacancy rate | 17.54 |
| White | 6001 |
| Black | 815 |
| Asian | 63 |
| Native | 23 |
| Hispanic/Latino | 6770 |
| Bachelor's or higher | 1225 |

## Districts

- [TX-19](/us/states/tx/districts/19.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 82](/us/states/tx/districts/house/82.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
