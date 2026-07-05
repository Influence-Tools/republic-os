---
type: Jurisdiction
title: "Codington County, SD"
classification: county
fips: "46029"
state: "SD"
demographics:
  population: 28767
  population_under_18: 6612
  population_18_64: 16530
  population_65_plus: 5625
  median_household_income: 72727
  poverty_rate: 8.83
  homeownership_rate: 69.83
  unemployment_rate: 1.92
  median_home_value: 237700
  gini_index: 0.4276
  vacancy_rate: 7.44
  race_white: 26037
  race_black: 303
  race_asian: 176
  race_native: 538
  hispanic: 946
  bachelors_plus: 5318
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/4"
    rel: in-district
    area_weight: 0.8005
  - to: "us/states/sd/districts/senate/5"
    rel: in-district
    area_weight: 0.1994
  - to: "us/states/sd/districts/house/4"
    rel: in-district
    area_weight: 0.8005
  - to: "us/states/sd/districts/house/5"
    rel: in-district
    area_weight: 0.1994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Codington County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 28767 |
| Under 18 | 6612 |
| 18–64 | 16530 |
| 65+ | 5625 |
| Median household income | 72727 |
| Poverty rate | 8.83 |
| Homeownership rate | 69.83 |
| Unemployment rate | 1.92 |
| Median home value | 237700 |
| Gini index | 0.4276 |
| Vacancy rate | 7.44 |
| White | 26037 |
| Black | 303 |
| Asian | 176 |
| Native | 538 |
| Hispanic/Latino | 946 |
| Bachelor's or higher | 5318 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 4](/us/states/sd/districts/senate/4.md) — 80% (state senate)
- [SD Senate District 5](/us/states/sd/districts/senate/5.md) — 20% (state senate)
- [SD House District 4](/us/states/sd/districts/house/4.md) — 80% (state house)
- [SD House District 5](/us/states/sd/districts/house/5.md) — 20% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
