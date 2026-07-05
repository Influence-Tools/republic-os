---
type: Jurisdiction
title: "Carter County, KY"
classification: county
fips: "21043"
state: "KY"
demographics:
  population: 26341
  population_under_18: 5941
  population_18_64: 15150
  population_65_plus: 5250
  median_household_income: 51235
  poverty_rate: 19.18
  homeownership_rate: 80.04
  unemployment_rate: 5.31
  median_home_value: 132800
  gini_index: 0.4563
  vacancy_rate: 12.36
  race_white: 25142
  race_black: 104
  race_asian: 70
  race_native: 6
  hispanic: 227
  bachelors_plus: 4282
districts:
  - to: "us/states/ky/districts/05"
    rel: in-district
    area_weight: 0.7447
  - to: "us/states/ky/districts/04"
    rel: in-district
    area_weight: 0.2553
  - to: "us/states/ky/districts/senate/18"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ky/districts/house/96"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Carter County, KY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 26341 |
| Under 18 | 5941 |
| 18–64 | 15150 |
| 65+ | 5250 |
| Median household income | 51235 |
| Poverty rate | 19.18 |
| Homeownership rate | 80.04 |
| Unemployment rate | 5.31 |
| Median home value | 132800 |
| Gini index | 0.4563 |
| Vacancy rate | 12.36 |
| White | 25142 |
| Black | 104 |
| Asian | 70 |
| Native | 6 |
| Hispanic/Latino | 227 |
| Bachelor's or higher | 4282 |

## Districts

- [KY-05](/us/states/ky/districts/05.md) — 74% (congressional)
- [KY-04](/us/states/ky/districts/04.md) — 26% (congressional)
- [KY Senate District 18](/us/states/ky/districts/senate/18.md) — 100% (state senate)
- [KY House District 96](/us/states/ky/districts/house/96.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
