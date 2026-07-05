---
type: Jurisdiction
title: "Pontotoc County, MS"
classification: county
fips: "28115"
state: "MS"
demographics:
  population: 31550
  population_under_18: 8237
  population_18_64: 18420
  population_65_plus: 4893
  median_household_income: 51484
  poverty_rate: 16.71
  homeownership_rate: 69.75
  unemployment_rate: 3.11
  median_home_value: 157100
  gini_index: 0.4373
  vacancy_rate: 16.89
  race_white: 23700
  race_black: 4639
  race_asian: 1
  race_native: 33
  hispanic: 2254
  bachelors_plus: 5372
districts:
  - to: "us/states/ms/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ms/districts/senate/8"
    rel: in-district
    area_weight: 0.6103
  - to: "us/states/ms/districts/senate/3"
    rel: in-district
    area_weight: 0.3896
  - to: "us/states/ms/districts/house/15"
    rel: in-district
    area_weight: 0.5228
  - to: "us/states/ms/districts/house/22"
    rel: in-district
    area_weight: 0.1863
  - to: "us/states/ms/districts/house/23"
    rel: in-district
    area_weight: 0.1618
  - to: "us/states/ms/districts/house/13"
    rel: in-district
    area_weight: 0.129
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Pontotoc County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 31550 |
| Under 18 | 8237 |
| 18–64 | 18420 |
| 65+ | 4893 |
| Median household income | 51484 |
| Poverty rate | 16.71 |
| Homeownership rate | 69.75 |
| Unemployment rate | 3.11 |
| Median home value | 157100 |
| Gini index | 0.4373 |
| Vacancy rate | 16.89 |
| White | 23700 |
| Black | 4639 |
| Asian | 1 |
| Native | 33 |
| Hispanic/Latino | 2254 |
| Bachelor's or higher | 5372 |

## Districts

- [MS-01](/us/states/ms/districts/01.md) — 100% (congressional)
- [MS Senate District 8](/us/states/ms/districts/senate/8.md) — 61% (state senate)
- [MS Senate District 3](/us/states/ms/districts/senate/3.md) — 39% (state senate)
- [MS House District 15](/us/states/ms/districts/house/15.md) — 52% (state house)
- [MS House District 22](/us/states/ms/districts/house/22.md) — 19% (state house)
- [MS House District 23](/us/states/ms/districts/house/23.md) — 16% (state house)
- [MS House District 13](/us/states/ms/districts/house/13.md) — 13% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
