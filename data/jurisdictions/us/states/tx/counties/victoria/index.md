---
type: Jurisdiction
title: "Victoria County, TX"
classification: county
fips: "48469"
state: "TX"
demographics:
  population: 91413
  population_under_18: 22924
  population_18_64: 52864
  population_65_plus: 15625
  median_household_income: 70896
  poverty_rate: 16.25
  homeownership_rate: 65.27
  unemployment_rate: 4.38
  median_home_value: 209900
  gini_index: 0.435
  vacancy_rate: 11.72
  race_white: 51754
  race_black: 5430
  race_asian: 1160
  race_native: 223
  hispanic: 43995
  bachelors_plus: 15515
districts:
  - to: "us/states/tx/districts/27"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/18"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/30"
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

# Victoria County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 91413 |
| Under 18 | 22924 |
| 18–64 | 52864 |
| 65+ | 15625 |
| Median household income | 70896 |
| Poverty rate | 16.25 |
| Homeownership rate | 65.27 |
| Unemployment rate | 4.38 |
| Median home value | 209900 |
| Gini index | 0.435 |
| Vacancy rate | 11.72 |
| White | 51754 |
| Black | 5430 |
| Asian | 1160 |
| Native | 223 |
| Hispanic/Latino | 43995 |
| Bachelor's or higher | 15515 |

## Districts

- [TX-27](/us/states/tx/districts/27.md) — 100% (congressional)
- [TX Senate District 18](/us/states/tx/districts/senate/18.md) — 100% (state senate)
- [TX House District 30](/us/states/tx/districts/house/30.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
