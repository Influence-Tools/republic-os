---
type: Jurisdiction
title: "Duval County, TX"
classification: county
fips: "48131"
state: "TX"
demographics:
  population: 9742
  population_under_18: 2454
  population_18_64: 5632
  population_65_plus: 1656
  median_household_income: 49038
  poverty_rate: 33.27
  homeownership_rate: 70.39
  unemployment_rate: 10.98
  median_home_value: 89400
  gini_index: 0.4593
  vacancy_rate: 30.93
  race_white: 5401
  race_black: 69
  race_asian: 117
  race_native: 82
  hispanic: 7950
  bachelors_plus: 598
districts:
  - to: "us/states/tx/districts/28"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/senate/21"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/31"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Duval County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9742 |
| Under 18 | 2454 |
| 18–64 | 5632 |
| 65+ | 1656 |
| Median household income | 49038 |
| Poverty rate | 33.27 |
| Homeownership rate | 70.39 |
| Unemployment rate | 10.98 |
| Median home value | 89400 |
| Gini index | 0.4593 |
| Vacancy rate | 30.93 |
| White | 5401 |
| Black | 69 |
| Asian | 117 |
| Native | 82 |
| Hispanic/Latino | 7950 |
| Bachelor's or higher | 598 |

## Districts

- [TX-28](/us/states/tx/districts/28.md) — 100% (congressional)
- [TX Senate District 21](/us/states/tx/districts/senate/21.md) — 100% (state senate)
- [TX House District 31](/us/states/tx/districts/house/31.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
