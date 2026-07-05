---
type: Jurisdiction
title: "Harlan County, KY"
classification: county
fips: "21095"
state: "KY"
demographics:
  population: 25772
  population_under_18: 6120
  population_18_64: 14632
  population_65_plus: 5020
  median_household_income: 41693
  poverty_rate: 27.37
  homeownership_rate: 71.57
  unemployment_rate: 9.53
  median_home_value: 73700
  gini_index: 0.4634
  vacancy_rate: 17.68
  race_white: 24269
  race_black: 328
  race_asian: 58
  race_native: 56
  hispanic: 135
  bachelors_plus: 3542
districts:
  - to: "us/states/ky/districts/05"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/ky/districts/senate/29"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/ky/districts/house/87"
    rel: in-district
    area_weight: 0.7149
  - to: "us/states/ky/districts/house/94"
    rel: in-district
    area_weight: 0.284
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Harlan County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25772 |
| Under 18 | 6120 |
| 18–64 | 14632 |
| 65+ | 5020 |
| Median household income | 41693 |
| Poverty rate | 27.37 |
| Homeownership rate | 71.57 |
| Unemployment rate | 9.53 |
| Median home value | 73700 |
| Gini index | 0.4634 |
| Vacancy rate | 17.68 |
| White | 24269 |
| Black | 328 |
| Asian | 58 |
| Native | 56 |
| Hispanic/Latino | 135 |
| Bachelor's or higher | 3542 |

## Districts

- [KY-05](/us/states/ky/districts/05.md) — 100% (congressional)
- [KY Senate District 29](/us/states/ky/districts/senate/29.md) — 100% (state senate)
- [KY House District 87](/us/states/ky/districts/house/87.md) — 71% (state house)
- [KY House District 94](/us/states/ky/districts/house/94.md) — 28% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
