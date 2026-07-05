---
type: Jurisdiction
title: "Lafayette County, MS"
classification: county
fips: "28071"
state: "MS"
demographics:
  population: 58327
  population_under_18: 10537
  population_18_64: 39809
  population_65_plus: 7981
  median_household_income: 67185
  poverty_rate: 18.54
  homeownership_rate: 63.77
  unemployment_rate: 2.11
  median_home_value: 315400
  gini_index: 0.5232
  vacancy_rate: 33.68
  race_white: 40594
  race_black: 13220
  race_asian: 1317
  race_native: 58
  hispanic: 2151
  bachelors_plus: 23509
districts:
  - to: "us/states/ms/districts/01"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ms/districts/senate/9"
    rel: in-district
    area_weight: 0.6079
  - to: "us/states/ms/districts/senate/10"
    rel: in-district
    area_weight: 0.2019
  - to: "us/states/ms/districts/senate/8"
    rel: in-district
    area_weight: 0.1902
  - to: "us/states/ms/districts/house/13"
    rel: in-district
    area_weight: 0.3001
  - to: "us/states/ms/districts/house/23"
    rel: in-district
    area_weight: 0.2535
  - to: "us/states/ms/districts/house/10"
    rel: in-district
    area_weight: 0.187
  - to: "us/states/ms/districts/house/34"
    rel: in-district
    area_weight: 0.0757
  - to: "us/states/ms/districts/house/12"
    rel: in-district
    area_weight: 0.0727
  - to: "us/states/ms/districts/house/8"
    rel: in-district
    area_weight: 0.0644
  - to: "us/states/ms/districts/house/5"
    rel: in-district
    area_weight: 0.0465
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Lafayette County, MS

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 58327 |
| Under 18 | 10537 |
| 18–64 | 39809 |
| 65+ | 7981 |
| Median household income | 67185 |
| Poverty rate | 18.54 |
| Homeownership rate | 63.77 |
| Unemployment rate | 2.11 |
| Median home value | 315400 |
| Gini index | 0.5232 |
| Vacancy rate | 33.68 |
| White | 40594 |
| Black | 13220 |
| Asian | 1317 |
| Native | 58 |
| Hispanic/Latino | 2151 |
| Bachelor's or higher | 23509 |

## Districts

- [MS-01](/us/states/ms/districts/01.md) — 100% (congressional)
- [MS Senate District 9](/us/states/ms/districts/senate/9.md) — 61% (state senate)
- [MS Senate District 10](/us/states/ms/districts/senate/10.md) — 20% (state senate)
- [MS Senate District 8](/us/states/ms/districts/senate/8.md) — 19% (state senate)
- [MS House District 13](/us/states/ms/districts/house/13.md) — 30% (state house)
- [MS House District 23](/us/states/ms/districts/house/23.md) — 25% (state house)
- [MS House District 10](/us/states/ms/districts/house/10.md) — 19% (state house)
- [MS House District 34](/us/states/ms/districts/house/34.md) — 8% (state house)
- [MS House District 12](/us/states/ms/districts/house/12.md) — 7% (state house)
- [MS House District 8](/us/states/ms/districts/house/8.md) — 6% (state house)
- [MS House District 5](/us/states/ms/districts/house/5.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
