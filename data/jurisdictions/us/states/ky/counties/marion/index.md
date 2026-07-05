---
type: Jurisdiction
title: "Marion County, KY"
classification: county
fips: "21155"
state: "KY"
demographics:
  population: 19749
  population_under_18: 4700
  population_18_64: 11625
  population_65_plus: 3424
  median_household_income: 59627
  poverty_rate: 16.97
  homeownership_rate: 77.67
  unemployment_rate: 4.2
  median_home_value: 168100
  gini_index: 0.4317
  vacancy_rate: 8.88
  race_white: 17389
  race_black: 1493
  race_asian: 125
  race_native: 22
  hispanic: 723
  bachelors_plus: 3118
districts:
  - to: "us/states/ky/districts/01"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/ky/districts/senate/14"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ky/districts/house/51"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Marion County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19749 |
| Under 18 | 4700 |
| 18–64 | 11625 |
| 65+ | 3424 |
| Median household income | 59627 |
| Poverty rate | 16.97 |
| Homeownership rate | 77.67 |
| Unemployment rate | 4.2 |
| Median home value | 168100 |
| Gini index | 0.4317 |
| Vacancy rate | 8.88 |
| White | 17389 |
| Black | 1493 |
| Asian | 125 |
| Native | 22 |
| Hispanic/Latino | 723 |
| Bachelor's or higher | 3118 |

## Districts

- [KY-01](/us/states/ky/districts/01.md) — 100% (congressional)
- [KY Senate District 14](/us/states/ky/districts/senate/14.md) — 100% (state senate)
- [KY House District 51](/us/states/ky/districts/house/51.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
