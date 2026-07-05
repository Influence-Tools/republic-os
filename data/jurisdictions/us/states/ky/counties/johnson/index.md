---
type: Jurisdiction
title: "Johnson County, KY"
classification: county
fips: "21115"
state: "KY"
demographics:
  population: 22334
  population_under_18: 4966
  population_18_64: 13090
  population_65_plus: 4278
  median_household_income: 44904
  poverty_rate: 22.79
  homeownership_rate: 68.29
  unemployment_rate: 4.23
  median_home_value: 120200
  gini_index: 0.4781
  vacancy_rate: 14.58
  race_white: 20983
  race_black: 123
  race_asian: 312
  race_native: 30
  hispanic: 110
  bachelors_plus: 3777
districts:
  - to: "us/states/ky/districts/05"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ky/districts/senate/31"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ky/districts/house/97"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Johnson County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 22334 |
| Under 18 | 4966 |
| 18–64 | 13090 |
| 65+ | 4278 |
| Median household income | 44904 |
| Poverty rate | 22.79 |
| Homeownership rate | 68.29 |
| Unemployment rate | 4.23 |
| Median home value | 120200 |
| Gini index | 0.4781 |
| Vacancy rate | 14.58 |
| White | 20983 |
| Black | 123 |
| Asian | 312 |
| Native | 30 |
| Hispanic/Latino | 110 |
| Bachelor's or higher | 3777 |

## Districts

- [KY-05](/us/states/ky/districts/05.md) — 100% (congressional)
- [KY Senate District 31](/us/states/ky/districts/senate/31.md) — 100% (state senate)
- [KY House District 97](/us/states/ky/districts/house/97.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
