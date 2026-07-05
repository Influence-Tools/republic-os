---
type: Jurisdiction
title: "Mills County, TX"
classification: county
fips: "48333"
state: "TX"
demographics:
  population: 4511
  population_under_18: 930
  population_18_64: 2413
  population_65_plus: 1168
  median_household_income: 67620
  poverty_rate: 7.2
  homeownership_rate: 80.27
  unemployment_rate: 3.19
  median_home_value: 223700
  gini_index: 0.4712
  vacancy_rate: 30.73
  race_white: 3474
  race_black: 30
  race_asian: 30
  race_native: 1
  hispanic: 947
  bachelors_plus: 1216
districts:
  - to: "us/states/tx/districts/11"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/68"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Mills County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4511 |
| Under 18 | 930 |
| 18–64 | 2413 |
| 65+ | 1168 |
| Median household income | 67620 |
| Poverty rate | 7.2 |
| Homeownership rate | 80.27 |
| Unemployment rate | 3.19 |
| Median home value | 223700 |
| Gini index | 0.4712 |
| Vacancy rate | 30.73 |
| White | 3474 |
| Black | 30 |
| Asian | 30 |
| Native | 1 |
| Hispanic/Latino | 947 |
| Bachelor's or higher | 1216 |

## Districts

- [TX-11](/us/states/tx/districts/11.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 68](/us/states/tx/districts/house/68.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
