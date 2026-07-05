---
type: Jurisdiction
title: "Leslie County, KY"
classification: county
fips: "21131"
state: "KY"
demographics:
  population: 10079
  population_under_18: 2085
  population_18_64: 6076
  population_65_plus: 1918
  median_household_income: 35934
  poverty_rate: 30.28
  homeownership_rate: 85.54
  unemployment_rate: 3.78
  median_home_value: 69000
  gini_index: 0.4684
  vacancy_rate: 14.09
  race_white: 9727
  race_black: 20
  race_asian: 10
  race_native: 0
  hispanic: 11
  bachelors_plus: 1113
districts:
  - to: "us/states/ky/districts/05"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ky/districts/senate/30"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ky/districts/house/90"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Leslie County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10079 |
| Under 18 | 2085 |
| 18–64 | 6076 |
| 65+ | 1918 |
| Median household income | 35934 |
| Poverty rate | 30.28 |
| Homeownership rate | 85.54 |
| Unemployment rate | 3.78 |
| Median home value | 69000 |
| Gini index | 0.4684 |
| Vacancy rate | 14.09 |
| White | 9727 |
| Black | 20 |
| Asian | 10 |
| Native | 0 |
| Hispanic/Latino | 11 |
| Bachelor's or higher | 1113 |

## Districts

- [KY-05](/us/states/ky/districts/05.md) — 100% (congressional)
- [KY Senate District 30](/us/states/ky/districts/senate/30.md) — 100% (state senate)
- [KY House District 90](/us/states/ky/districts/house/90.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
