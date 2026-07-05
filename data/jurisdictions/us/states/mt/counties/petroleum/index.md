---
type: Jurisdiction
title: "Petroleum County, MT"
classification: county
fips: "30069"
state: "MT"
demographics:
  population: 447
  population_under_18: 66
  population_18_64: 255
  population_65_plus: 126
  median_household_income: 60208
  poverty_rate: 8.05
  homeownership_rate: 72.85
  unemployment_rate: 0.0
  median_home_value: 201400
  gini_index: 0.4271
  vacancy_rate: 28.94
  race_white: 442
  race_black: 0
  race_asian: 3
  race_native: 2
  hispanic: 0
  bachelors_plus: 148
districts:
  - to: "us/states/mt/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mt/districts/senate/19"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mt/districts/house/37"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Petroleum County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 447 |
| Under 18 | 66 |
| 18–64 | 255 |
| 65+ | 126 |
| Median household income | 60208 |
| Poverty rate | 8.05 |
| Homeownership rate | 72.85 |
| Unemployment rate | 0.0 |
| Median home value | 201400 |
| Gini index | 0.4271 |
| Vacancy rate | 28.94 |
| White | 442 |
| Black | 0 |
| Asian | 3 |
| Native | 2 |
| Hispanic/Latino | 0 |
| Bachelor's or higher | 148 |

## Districts

- [MT-02](/us/states/mt/districts/02.md) — 100% (congressional)
- [MT Senate District 19](/us/states/mt/districts/senate/19.md) — 100% (state senate)
- [MT House District 37](/us/states/mt/districts/house/37.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
