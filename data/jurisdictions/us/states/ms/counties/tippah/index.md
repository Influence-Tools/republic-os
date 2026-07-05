---
type: Jurisdiction
title: "Tippah County, MS"
classification: county
fips: "28139"
state: "MS"
demographics:
  population: 21523
  population_under_18: 5080
  population_18_64: 12706
  population_65_plus: 3737
  median_household_income: 52542
  poverty_rate: 18.93
  homeownership_rate: 74.79
  unemployment_rate: 5.55
  median_home_value: 124100
  gini_index: 0.4411
  vacancy_rate: 19.5
  race_white: 16420
  race_black: 3009
  race_asian: 36
  race_native: 24
  hispanic: 1135
  bachelors_plus: 3377
districts:
  - to: "us/states/ms/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ms/districts/senate/4"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ms/districts/house/4"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Tippah County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21523 |
| Under 18 | 5080 |
| 18–64 | 12706 |
| 65+ | 3737 |
| Median household income | 52542 |
| Poverty rate | 18.93 |
| Homeownership rate | 74.79 |
| Unemployment rate | 5.55 |
| Median home value | 124100 |
| Gini index | 0.4411 |
| Vacancy rate | 19.5 |
| White | 16420 |
| Black | 3009 |
| Asian | 36 |
| Native | 24 |
| Hispanic/Latino | 1135 |
| Bachelor's or higher | 3377 |

## Districts

- [MS-01](/us/states/ms/districts/01.md) — 100% (congressional)
- [MS Senate District 4](/us/states/ms/districts/senate/4.md) — 100% (state senate)
- [MS House District 4](/us/states/ms/districts/house/4.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
