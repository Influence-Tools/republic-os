---
type: Jurisdiction
title: "Dewey County, OK"
classification: county
fips: "40043"
state: "OK"
demographics:
  population: 4360
  population_under_18: 1192
  population_18_64: 2315
  population_65_plus: 853
  median_household_income: 62569
  poverty_rate: 14.11
  homeownership_rate: 76.39
  unemployment_rate: 3.47
  median_home_value: 133600
  gini_index: 0.4261
  vacancy_rate: 25.32
  race_white: 3609
  race_black: 3
  race_asian: 4
  race_native: 161
  hispanic: 261
  bachelors_plus: 854
districts:
  - to: "us/states/ok/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ok/districts/senate/27"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/house/59"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Dewey County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4360 |
| Under 18 | 1192 |
| 18–64 | 2315 |
| 65+ | 853 |
| Median household income | 62569 |
| Poverty rate | 14.11 |
| Homeownership rate | 76.39 |
| Unemployment rate | 3.47 |
| Median home value | 133600 |
| Gini index | 0.4261 |
| Vacancy rate | 25.32 |
| White | 3609 |
| Black | 3 |
| Asian | 4 |
| Native | 161 |
| Hispanic/Latino | 261 |
| Bachelor's or higher | 854 |

## Districts

- [OK-03](/us/states/ok/districts/03.md) — 100% (congressional)
- [OK Senate District 27](/us/states/ok/districts/senate/27.md) — 100% (state senate)
- [OK House District 59](/us/states/ok/districts/house/59.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
