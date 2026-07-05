---
type: Jurisdiction
title: "Roberts County, SD"
classification: county
fips: "46109"
state: "SD"
demographics:
  population: 10221
  population_under_18: 3120
  population_18_64: 2616
  population_65_plus: 4485
  median_household_income: 65130
  poverty_rate: 15.72
  homeownership_rate: 71.17
  unemployment_rate: 5.99
  median_home_value: 154500
  gini_index: 0.4265
  vacancy_rate: 25.23
  race_white: 5830
  race_black: 33
  race_asian: 83
  race_native: 3544
  hispanic: 269
  bachelors_plus: 1562
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/sd/districts/senate/1"
    rel: in-district
    area_weight: 0.8081
  - to: "us/states/sd/districts/senate/4"
    rel: in-district
    area_weight: 0.1914
  - to: "us/states/sd/districts/house/1"
    rel: in-district
    area_weight: 0.8081
  - to: "us/states/sd/districts/house/4"
    rel: in-district
    area_weight: 0.1914
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Roberts County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10221 |
| Under 18 | 3120 |
| 18–64 | 2616 |
| 65+ | 4485 |
| Median household income | 65130 |
| Poverty rate | 15.72 |
| Homeownership rate | 71.17 |
| Unemployment rate | 5.99 |
| Median home value | 154500 |
| Gini index | 0.4265 |
| Vacancy rate | 25.23 |
| White | 5830 |
| Black | 33 |
| Asian | 83 |
| Native | 3544 |
| Hispanic/Latino | 269 |
| Bachelor's or higher | 1562 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 1](/us/states/sd/districts/senate/1.md) — 81% (state senate)
- [SD Senate District 4](/us/states/sd/districts/senate/4.md) — 19% (state senate)
- [SD House District 1](/us/states/sd/districts/house/1.md) — 81% (state house)
- [SD House District 4](/us/states/sd/districts/house/4.md) — 19% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
