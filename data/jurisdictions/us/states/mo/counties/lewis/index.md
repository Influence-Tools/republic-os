---
type: Jurisdiction
title: "Lewis County, MO"
classification: county
fips: "29111"
state: "MO"
demographics:
  population: 9924
  population_under_18: 2108
  population_18_64: 5904
  population_65_plus: 1912
  median_household_income: 59934
  poverty_rate: 12.69
  homeownership_rate: 76.3
  unemployment_rate: 5.11
  median_home_value: 130200
  gini_index: 0.4307
  vacancy_rate: 26.27
  race_white: 9100
  race_black: 383
  race_asian: 50
  race_native: 2
  hispanic: 111
  bachelors_plus: 1361
districts:
  - to: "us/states/mo/districts/06"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/senate/18"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/4"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Lewis County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9924 |
| Under 18 | 2108 |
| 18–64 | 5904 |
| 65+ | 1912 |
| Median household income | 59934 |
| Poverty rate | 12.69 |
| Homeownership rate | 76.3 |
| Unemployment rate | 5.11 |
| Median home value | 130200 |
| Gini index | 0.4307 |
| Vacancy rate | 26.27 |
| White | 9100 |
| Black | 383 |
| Asian | 50 |
| Native | 2 |
| Hispanic/Latino | 111 |
| Bachelor's or higher | 1361 |

## Districts

- [MO-06](/us/states/mo/districts/06.md) — 100% (congressional)
- [MO Senate District 18](/us/states/mo/districts/senate/18.md) — 100% (state senate)
- [MO House District 4](/us/states/mo/districts/house/4.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
