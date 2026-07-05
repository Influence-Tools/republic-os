---
type: Jurisdiction
title: "Callahan County, TX"
classification: county
fips: "48059"
state: "TX"
demographics:
  population: 14241
  population_under_18: 3102
  population_18_64: 8154
  population_65_plus: 2985
  median_household_income: 72436
  poverty_rate: 9.61
  homeownership_rate: 80.93
  unemployment_rate: 4.72
  median_home_value: 145500
  gini_index: 0.386
  vacancy_rate: 19.88
  race_white: 11886
  race_black: 165
  race_asian: 82
  race_native: 5
  hispanic: 1598
  bachelors_plus: 3055
districts:
  - to: "us/states/tx/districts/25"
    rel: in-district
    area_weight: 0.9169
  - to: "us/states/tx/districts/19"
    rel: in-district
    area_weight: 0.0828
  - to: "us/states/tx/districts/senate/10"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/71"
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

# Callahan County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14241 |
| Under 18 | 3102 |
| 18–64 | 8154 |
| 65+ | 2985 |
| Median household income | 72436 |
| Poverty rate | 9.61 |
| Homeownership rate | 80.93 |
| Unemployment rate | 4.72 |
| Median home value | 145500 |
| Gini index | 0.386 |
| Vacancy rate | 19.88 |
| White | 11886 |
| Black | 165 |
| Asian | 82 |
| Native | 5 |
| Hispanic/Latino | 1598 |
| Bachelor's or higher | 3055 |

## Districts

- [TX-25](/us/states/tx/districts/25.md) — 92% (congressional)
- [TX-19](/us/states/tx/districts/19.md) — 8% (congressional)
- [TX Senate District 10](/us/states/tx/districts/senate/10.md) — 100% (state senate)
- [TX House District 71](/us/states/tx/districts/house/71.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
