---
type: Jurisdiction
title: "Yoakum County, TX"
classification: county
fips: "48501"
state: "TX"
demographics:
  population: 7571
  population_under_18: 2482
  population_18_64: 4118
  population_65_plus: 971
  median_household_income: 84925
  poverty_rate: 16.78
  homeownership_rate: 66.77
  unemployment_rate: 6.86
  median_home_value: 182600
  gini_index: 0.3954
  vacancy_rate: 13.74
  race_white: 3425
  race_black: 11
  race_asian: 71
  race_native: 98
  hispanic: 4966
  bachelors_plus: 1125
districts:
  - to: "us/states/tx/districts/19"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/88"
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

# Yoakum County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7571 |
| Under 18 | 2482 |
| 18–64 | 4118 |
| 65+ | 971 |
| Median household income | 84925 |
| Poverty rate | 16.78 |
| Homeownership rate | 66.77 |
| Unemployment rate | 6.86 |
| Median home value | 182600 |
| Gini index | 0.3954 |
| Vacancy rate | 13.74 |
| White | 3425 |
| Black | 11 |
| Asian | 71 |
| Native | 98 |
| Hispanic/Latino | 4966 |
| Bachelor's or higher | 1125 |

## Districts

- [TX-19](/us/states/tx/districts/19.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 88](/us/states/tx/districts/house/88.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
