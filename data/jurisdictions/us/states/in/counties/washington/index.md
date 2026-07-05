---
type: Jurisdiction
title: "Washington County, IN"
classification: county
fips: "18175"
state: "IN"
demographics:
  population: 28212
  population_under_18: 6429
  population_18_64: 16549
  population_65_plus: 5234
  median_household_income: 64641
  poverty_rate: 14.45
  homeownership_rate: 82.06
  unemployment_rate: 3.18
  median_home_value: 172200
  gini_index: 0.4083
  vacancy_rate: 8.12
  race_white: 26962
  race_black: 97
  race_asian: 37
  race_native: 3
  hispanic: 433
  bachelors_plus: 3638
districts:
  - to: "us/states/in/districts/09"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/in/districts/senate/47"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/in/districts/house/69"
    rel: in-district
    area_weight: 0.4059
  - to: "us/states/in/districts/house/70"
    rel: in-district
    area_weight: 0.3231
  - to: "us/states/in/districts/house/65"
    rel: in-district
    area_weight: 0.271
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Washington County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 28212 |
| Under 18 | 6429 |
| 18–64 | 16549 |
| 65+ | 5234 |
| Median household income | 64641 |
| Poverty rate | 14.45 |
| Homeownership rate | 82.06 |
| Unemployment rate | 3.18 |
| Median home value | 172200 |
| Gini index | 0.4083 |
| Vacancy rate | 8.12 |
| White | 26962 |
| Black | 97 |
| Asian | 37 |
| Native | 3 |
| Hispanic/Latino | 433 |
| Bachelor's or higher | 3638 |

## Districts

- [IN-09](/us/states/in/districts/09.md) — 100% (congressional)
- [IN Senate District 47](/us/states/in/districts/senate/47.md) — 100% (state senate)
- [IN House District 69](/us/states/in/districts/house/69.md) — 41% (state house)
- [IN House District 70](/us/states/in/districts/house/70.md) — 32% (state house)
- [IN House District 65](/us/states/in/districts/house/65.md) — 27% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
