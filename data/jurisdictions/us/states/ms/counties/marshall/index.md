---
type: Jurisdiction
title: "Marshall County, MS"
classification: county
fips: "28093"
state: "MS"
demographics:
  population: 33979
  population_under_18: 7056
  population_18_64: 20454
  population_65_plus: 6469
  median_household_income: 53458
  poverty_rate: 23.04
  homeownership_rate: 79.12
  unemployment_rate: 4.38
  median_home_value: 167900
  gini_index: 0.4687
  vacancy_rate: 15.03
  race_white: 16105
  race_black: 14570
  race_asian: 51
  race_native: 160
  hispanic: 1748
  bachelors_plus: 4765
districts:
  - to: "us/states/ms/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ms/districts/senate/10"
    rel: in-district
    area_weight: 0.8599
  - to: "us/states/ms/districts/senate/3"
    rel: in-district
    area_weight: 0.1401
  - to: "us/states/ms/districts/house/5"
    rel: in-district
    area_weight: 0.6482
  - to: "us/states/ms/districts/house/52"
    rel: in-district
    area_weight: 0.2153
  - to: "us/states/ms/districts/house/13"
    rel: in-district
    area_weight: 0.1364
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Marshall County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 33979 |
| Under 18 | 7056 |
| 18–64 | 20454 |
| 65+ | 6469 |
| Median household income | 53458 |
| Poverty rate | 23.04 |
| Homeownership rate | 79.12 |
| Unemployment rate | 4.38 |
| Median home value | 167900 |
| Gini index | 0.4687 |
| Vacancy rate | 15.03 |
| White | 16105 |
| Black | 14570 |
| Asian | 51 |
| Native | 160 |
| Hispanic/Latino | 1748 |
| Bachelor's or higher | 4765 |

## Districts

- [MS-01](/us/states/ms/districts/01.md) — 100% (congressional)
- [MS Senate District 10](/us/states/ms/districts/senate/10.md) — 86% (state senate)
- [MS Senate District 3](/us/states/ms/districts/senate/3.md) — 14% (state senate)
- [MS House District 5](/us/states/ms/districts/house/5.md) — 65% (state house)
- [MS House District 52](/us/states/ms/districts/house/52.md) — 22% (state house)
- [MS House District 13](/us/states/ms/districts/house/13.md) — 14% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
