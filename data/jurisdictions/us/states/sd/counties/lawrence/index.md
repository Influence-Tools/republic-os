---
type: Jurisdiction
title: "Lawrence County, SD"
classification: county
fips: "46081"
state: "SD"
demographics:
  population: 27233
  population_under_18: 5452
  population_18_64: 8222
  population_65_plus: 13559
  median_household_income: 73384
  poverty_rate: 11.56
  homeownership_rate: 65.09
  unemployment_rate: 1.75
  median_home_value: 346500
  gini_index: 0.4559
  vacancy_rate: 18.77
  race_white: 24620
  race_black: 107
  race_asian: 122
  race_native: 683
  hispanic: 1057
  bachelors_plus: 8891
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/31"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/sd/districts/house/31"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Lawrence County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 27233 |
| Under 18 | 5452 |
| 18–64 | 8222 |
| 65+ | 13559 |
| Median household income | 73384 |
| Poverty rate | 11.56 |
| Homeownership rate | 65.09 |
| Unemployment rate | 1.75 |
| Median home value | 346500 |
| Gini index | 0.4559 |
| Vacancy rate | 18.77 |
| White | 24620 |
| Black | 107 |
| Asian | 122 |
| Native | 683 |
| Hispanic/Latino | 1057 |
| Bachelor's or higher | 8891 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 31](/us/states/sd/districts/senate/31.md) — 100% (state senate)
- [SD House District 31](/us/states/sd/districts/house/31.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
