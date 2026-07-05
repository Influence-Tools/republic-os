---
type: Jurisdiction
title: "Itawamba County, MS"
classification: county
fips: "28057"
state: "MS"
demographics:
  population: 24036
  population_under_18: 5112
  population_18_64: 14725
  population_65_plus: 4199
  median_household_income: 55546
  poverty_rate: 15.52
  homeownership_rate: 78.96
  unemployment_rate: 5.1
  median_home_value: 142400
  gini_index: 0.5214
  vacancy_rate: 8.73
  race_white: 21328
  race_black: 1240
  race_asian: 111
  race_native: 19
  hispanic: 446
  bachelors_plus: 3621
districts:
  - to: "us/states/ms/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ms/districts/senate/5"
    rel: in-district
    area_weight: 0.6482
  - to: "us/states/ms/districts/senate/7"
    rel: in-district
    area_weight: 0.3518
  - to: "us/states/ms/districts/house/21"
    rel: in-district
    area_weight: 0.8424
  - to: "us/states/ms/districts/house/19"
    rel: in-district
    area_weight: 0.1574
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Itawamba County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 24036 |
| Under 18 | 5112 |
| 18–64 | 14725 |
| 65+ | 4199 |
| Median household income | 55546 |
| Poverty rate | 15.52 |
| Homeownership rate | 78.96 |
| Unemployment rate | 5.1 |
| Median home value | 142400 |
| Gini index | 0.5214 |
| Vacancy rate | 8.73 |
| White | 21328 |
| Black | 1240 |
| Asian | 111 |
| Native | 19 |
| Hispanic/Latino | 446 |
| Bachelor's or higher | 3621 |

## Districts

- [MS-01](/us/states/ms/districts/01.md) — 100% (congressional)
- [MS Senate District 5](/us/states/ms/districts/senate/5.md) — 65% (state senate)
- [MS Senate District 7](/us/states/ms/districts/senate/7.md) — 35% (state senate)
- [MS House District 21](/us/states/ms/districts/house/21.md) — 84% (state house)
- [MS House District 19](/us/states/ms/districts/house/19.md) — 16% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
