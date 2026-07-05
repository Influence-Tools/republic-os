---
type: Jurisdiction
title: "Tunica County, MS"
classification: county
fips: "28143"
state: "MS"
demographics:
  population: 9475
  population_under_18: 2626
  population_18_64: 5457
  population_65_plus: 1392
  median_household_income: 39364
  poverty_rate: 31.1
  homeownership_rate: 39.53
  unemployment_rate: 13.27
  median_home_value: 175900
  gini_index: 0.5023
  vacancy_rate: 21.03
  race_white: 1724
  race_black: 7566
  race_asian: 0
  race_native: 0
  hispanic: 171
  bachelors_plus: 993
districts:
  - to: "us/states/ms/districts/02"
    rel: in-district
    area_weight: 0.9948
  - to: "us/states/ms/districts/senate/11"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/ms/districts/house/9"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Tunica County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9475 |
| Under 18 | 2626 |
| 18–64 | 5457 |
| 65+ | 1392 |
| Median household income | 39364 |
| Poverty rate | 31.1 |
| Homeownership rate | 39.53 |
| Unemployment rate | 13.27 |
| Median home value | 175900 |
| Gini index | 0.5023 |
| Vacancy rate | 21.03 |
| White | 1724 |
| Black | 7566 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 171 |
| Bachelor's or higher | 993 |

## Districts

- [MS-02](/us/states/ms/districts/02.md) — 99% (congressional)
- [MS Senate District 11](/us/states/ms/districts/senate/11.md) — 100% (state senate)
- [MS House District 9](/us/states/ms/districts/house/9.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
