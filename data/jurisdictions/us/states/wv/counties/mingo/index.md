---
type: Jurisdiction
title: "Mingo County, WV"
classification: county
fips: "54059"
state: "WV"
demographics:
  population: 22542
  population_under_18: 5122
  population_18_64: 12491
  population_65_plus: 4929
  median_household_income: 38119
  poverty_rate: 32.36
  homeownership_rate: 73.42
  unemployment_rate: 11.51
  median_home_value: 90500
  gini_index: 0.5368
  vacancy_rate: 19.36
  race_white: 21483
  race_black: 447
  race_asian: 1
  race_native: 3
  hispanic: 178
  bachelors_plus: 2113
districts:
  - to: "us/states/wv/districts/01"
    rel: in-district
    area_weight: 0.9922
  - to: "us/states/ky/districts/05"
    rel: in-district
    area_weight: 0.0072
  - to: "us/states/wv/districts/senate/6"
    rel: in-district
    area_weight: 0.9985
  - to: "us/states/wv/districts/house/34"
    rel: in-district
    area_weight: 0.6274
  - to: "us/states/wv/districts/house/29"
    rel: in-district
    area_weight: 0.371
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Mingo County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 22542 |
| Under 18 | 5122 |
| 18–64 | 12491 |
| 65+ | 4929 |
| Median household income | 38119 |
| Poverty rate | 32.36 |
| Homeownership rate | 73.42 |
| Unemployment rate | 11.51 |
| Median home value | 90500 |
| Gini index | 0.5368 |
| Vacancy rate | 19.36 |
| White | 21483 |
| Black | 447 |
| Asian | 1 |
| Native | 3 |
| Hispanic/Latino | 178 |
| Bachelor's or higher | 2113 |

## Districts

- [WV-01](/us/states/wv/districts/01.md) — 99% (congressional)
- [KY-05](/us/states/ky/districts/05.md) — 1% (congressional)
- [WV Senate District 6](/us/states/wv/districts/senate/6.md) — 100% (state senate)
- [WV House District 34](/us/states/wv/districts/house/34.md) — 63% (state house)
- [WV House District 29](/us/states/wv/districts/house/29.md) — 37% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
