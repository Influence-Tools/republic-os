---
type: Jurisdiction
title: "Greenbrier County, WV"
classification: county
fips: "54025"
state: "WV"
demographics:
  population: 32386
  population_under_18: 6245
  population_18_64: 18215
  population_65_plus: 7926
  median_household_income: 48218
  poverty_rate: 21.82
  homeownership_rate: 73.11
  unemployment_rate: 4.16
  median_home_value: 149000
  gini_index: 0.4886
  vacancy_rate: 17.45
  race_white: 29951
  race_black: 758
  race_asian: 214
  race_native: 44
  hispanic: 609
  bachelors_plus: 7473
districts:
  - to: "us/states/wv/districts/01"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/wv/districts/senate/10"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/wv/districts/house/47"
    rel: in-district
    area_weight: 0.4482
  - to: "us/states/wv/districts/house/46"
    rel: in-district
    area_weight: 0.3501
  - to: "us/states/wv/districts/house/48"
    rel: in-district
    area_weight: 0.2012
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Greenbrier County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 32386 |
| Under 18 | 6245 |
| 18–64 | 18215 |
| 65+ | 7926 |
| Median household income | 48218 |
| Poverty rate | 21.82 |
| Homeownership rate | 73.11 |
| Unemployment rate | 4.16 |
| Median home value | 149000 |
| Gini index | 0.4886 |
| Vacancy rate | 17.45 |
| White | 29951 |
| Black | 758 |
| Asian | 214 |
| Native | 44 |
| Hispanic/Latino | 609 |
| Bachelor's or higher | 7473 |

## Districts

- [WV-01](/us/states/wv/districts/01.md) — 100% (congressional)
- [WV Senate District 10](/us/states/wv/districts/senate/10.md) — 100% (state senate)
- [WV House District 47](/us/states/wv/districts/house/47.md) — 45% (state house)
- [WV House District 46](/us/states/wv/districts/house/46.md) — 35% (state house)
- [WV House District 48](/us/states/wv/districts/house/48.md) — 20% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
