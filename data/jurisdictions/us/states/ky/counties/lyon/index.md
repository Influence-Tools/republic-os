---
type: Jurisdiction
title: "Lyon County, KY"
classification: county
fips: "21143"
state: "KY"
demographics:
  population: 8900
  population_under_18: 1207
  population_18_64: 5500
  population_65_plus: 2193
  median_household_income: 65066
  poverty_rate: 9.53
  homeownership_rate: 80.4
  unemployment_rate: 2.86
  median_home_value: 189500
  gini_index: 0.4516
  vacancy_rate: 29.46
  race_white: 7860
  race_black: 602
  race_asian: 48
  race_native: 36
  hispanic: 194
  bachelors_plus: 1707
districts:
  - to: "us/states/ky/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ky/districts/senate/1"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ky/districts/house/6"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Lyon County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8900 |
| Under 18 | 1207 |
| 18–64 | 5500 |
| 65+ | 2193 |
| Median household income | 65066 |
| Poverty rate | 9.53 |
| Homeownership rate | 80.4 |
| Unemployment rate | 2.86 |
| Median home value | 189500 |
| Gini index | 0.4516 |
| Vacancy rate | 29.46 |
| White | 7860 |
| Black | 602 |
| Asian | 48 |
| Native | 36 |
| Hispanic/Latino | 194 |
| Bachelor's or higher | 1707 |

## Districts

- [KY-01](/us/states/ky/districts/01.md) — 100% (congressional)
- [KY Senate District 1](/us/states/ky/districts/senate/1.md) — 100% (state senate)
- [KY House District 6](/us/states/ky/districts/house/6.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
