---
type: Jurisdiction
title: "Alcorn County, MS"
classification: county
fips: "28003"
state: "MS"
demographics:
  population: 34289
  population_under_18: 7661
  population_18_64: 20123
  population_65_plus: 6505
  median_household_income: 51260
  poverty_rate: 15.79
  homeownership_rate: 67.79
  unemployment_rate: 4.62
  median_home_value: 142100
  gini_index: 0.4516
  vacancy_rate: 11.22
  race_white: 27638
  race_black: 3486
  race_asian: 162
  race_native: 29
  hispanic: 1308
  bachelors_plus: 5962
districts:
  - to: "us/states/ms/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ms/districts/senate/4"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ms/districts/house/2"
    rel: in-district
    area_weight: 0.5395
  - to: "us/states/ms/districts/house/1"
    rel: in-district
    area_weight: 0.2023
  - to: "us/states/ms/districts/house/4"
    rel: in-district
    area_weight: 0.1606
  - to: "us/states/ms/districts/house/3"
    rel: in-district
    area_weight: 0.0975
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Alcorn County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 34289 |
| Under 18 | 7661 |
| 18–64 | 20123 |
| 65+ | 6505 |
| Median household income | 51260 |
| Poverty rate | 15.79 |
| Homeownership rate | 67.79 |
| Unemployment rate | 4.62 |
| Median home value | 142100 |
| Gini index | 0.4516 |
| Vacancy rate | 11.22 |
| White | 27638 |
| Black | 3486 |
| Asian | 162 |
| Native | 29 |
| Hispanic/Latino | 1308 |
| Bachelor's or higher | 5962 |

## Districts

- [MS-01](/us/states/ms/districts/01.md) — 100% (congressional)
- [MS Senate District 4](/us/states/ms/districts/senate/4.md) — 100% (state senate)
- [MS House District 2](/us/states/ms/districts/house/2.md) — 54% (state house)
- [MS House District 1](/us/states/ms/districts/house/1.md) — 20% (state house)
- [MS House District 4](/us/states/ms/districts/house/4.md) — 16% (state house)
- [MS House District 3](/us/states/ms/districts/house/3.md) — 10% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
