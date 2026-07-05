---
type: Jurisdiction
title: "Hickman County, KY"
classification: county
fips: "21105"
state: "KY"
demographics:
  population: 4439
  population_under_18: 855
  population_18_64: 2464
  population_65_plus: 1120
  median_household_income: 60867
  poverty_rate: 20.48
  homeownership_rate: 70.83
  unemployment_rate: 3.06
  median_home_value: 115700
  gini_index: 0.4511
  vacancy_rate: 19.71
  race_white: 3838
  race_black: 362
  race_asian: 12
  race_native: 2
  hispanic: 116
  bachelors_plus: 671
districts:
  - to: "us/states/ky/districts/01"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ky/districts/senate/1"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/ky/districts/house/1"
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

# Hickman County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4439 |
| Under 18 | 855 |
| 18–64 | 2464 |
| 65+ | 1120 |
| Median household income | 60867 |
| Poverty rate | 20.48 |
| Homeownership rate | 70.83 |
| Unemployment rate | 3.06 |
| Median home value | 115700 |
| Gini index | 0.4511 |
| Vacancy rate | 19.71 |
| White | 3838 |
| Black | 362 |
| Asian | 12 |
| Native | 2 |
| Hispanic/Latino | 116 |
| Bachelor's or higher | 671 |

## Districts

- [KY-01](/us/states/ky/districts/01.md) — 100% (congressional)
- [KY Senate District 1](/us/states/ky/districts/senate/1.md) — 100% (state senate)
- [KY House District 1](/us/states/ky/districts/house/1.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
