---
type: Jurisdiction
title: "Crane County, TX"
classification: county
fips: "48103"
state: "TX"
demographics:
  population: 4610
  population_under_18: 1363
  population_18_64: 2528
  population_65_plus: 719
  median_household_income: 62212
  poverty_rate: 10.89
  homeownership_rate: 83.76
  unemployment_rate: 4.57
  median_home_value: 129400
  gini_index: 0.4175
  vacancy_rate: 11.3
  race_white: 1849
  race_black: 145
  race_asian: 72
  race_native: 8
  hispanic: 3177
  bachelors_plus: 440
districts:
  - to: "us/states/tx/districts/23"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tx/districts/house/53"
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

# Crane County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4610 |
| Under 18 | 1363 |
| 18–64 | 2528 |
| 65+ | 719 |
| Median household income | 62212 |
| Poverty rate | 10.89 |
| Homeownership rate | 83.76 |
| Unemployment rate | 4.57 |
| Median home value | 129400 |
| Gini index | 0.4175 |
| Vacancy rate | 11.3 |
| White | 1849 |
| Black | 145 |
| Asian | 72 |
| Native | 8 |
| Hispanic/Latino | 3177 |
| Bachelor's or higher | 440 |

## Districts

- [TX-23](/us/states/tx/districts/23.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 53](/us/states/tx/districts/house/53.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
