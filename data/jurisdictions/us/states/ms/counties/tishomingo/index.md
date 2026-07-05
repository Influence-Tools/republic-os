---
type: Jurisdiction
title: "Tishomingo County, MS"
classification: county
fips: "28141"
state: "MS"
demographics:
  population: 18660
  population_under_18: 4013
  population_18_64: 10698
  population_65_plus: 3949
  median_household_income: 53040
  poverty_rate: 18.0
  homeownership_rate: 79.54
  unemployment_rate: 3.15
  median_home_value: 145100
  gini_index: 0.4692
  vacancy_rate: 16.48
  race_white: 16988
  race_black: 222
  race_asian: 107
  race_native: 100
  hispanic: 605
  bachelors_plus: 3263
districts:
  - to: "us/states/ms/districts/01"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ms/districts/senate/5"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ms/districts/house/1"
    rel: in-district
    area_weight: 0.861
  - to: "us/states/ms/districts/house/3"
    rel: in-district
    area_weight: 0.1385
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Tishomingo County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18660 |
| Under 18 | 4013 |
| 18–64 | 10698 |
| 65+ | 3949 |
| Median household income | 53040 |
| Poverty rate | 18.0 |
| Homeownership rate | 79.54 |
| Unemployment rate | 3.15 |
| Median home value | 145100 |
| Gini index | 0.4692 |
| Vacancy rate | 16.48 |
| White | 16988 |
| Black | 222 |
| Asian | 107 |
| Native | 100 |
| Hispanic/Latino | 605 |
| Bachelor's or higher | 3263 |

## Districts

- [MS-01](/us/states/ms/districts/01.md) — 100% (congressional)
- [MS Senate District 5](/us/states/ms/districts/senate/5.md) — 100% (state senate)
- [MS House District 1](/us/states/ms/districts/house/1.md) — 86% (state house)
- [MS House District 3](/us/states/ms/districts/house/3.md) — 14% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
