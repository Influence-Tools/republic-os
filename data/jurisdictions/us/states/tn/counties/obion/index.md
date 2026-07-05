---
type: Jurisdiction
title: "Obion County, TN"
classification: county
fips: "47131"
state: "TN"
demographics:
  population: 30453
  population_under_18: 6646
  population_18_64: 17388
  population_65_plus: 6419
  median_household_income: 54613
  poverty_rate: 18.56
  homeownership_rate: 68.12
  unemployment_rate: 4.17
  median_home_value: 133600
  gini_index: 0.4749
  vacancy_rate: 12.56
  race_white: 24234
  race_black: 3198
  race_asian: 99
  race_native: 29
  hispanic: 1686
  bachelors_plus: 5436
districts:
  - to: "us/states/tn/districts/08"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tn/districts/senate/24"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tn/districts/house/77"
    rel: in-district
    area_weight: 0.7019
  - to: "us/states/tn/districts/house/82"
    rel: in-district
    area_weight: 0.2977
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Obion County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 30453 |
| Under 18 | 6646 |
| 18–64 | 17388 |
| 65+ | 6419 |
| Median household income | 54613 |
| Poverty rate | 18.56 |
| Homeownership rate | 68.12 |
| Unemployment rate | 4.17 |
| Median home value | 133600 |
| Gini index | 0.4749 |
| Vacancy rate | 12.56 |
| White | 24234 |
| Black | 3198 |
| Asian | 99 |
| Native | 29 |
| Hispanic/Latino | 1686 |
| Bachelor's or higher | 5436 |

## Districts

- [TN-08](/us/states/tn/districts/08.md) — 100% (congressional)
- [TN Senate District 24](/us/states/tn/districts/senate/24.md) — 100% (state senate)
- [TN House District 77](/us/states/tn/districts/house/77.md) — 70% (state house)
- [TN House District 82](/us/states/tn/districts/house/82.md) — 30% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
