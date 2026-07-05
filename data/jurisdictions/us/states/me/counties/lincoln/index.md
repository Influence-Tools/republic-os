---
type: Jurisdiction
title: "Lincoln County, ME"
classification: county
fips: "23015"
state: "ME"
demographics:
  population: 36099
  population_under_18: 5945
  population_18_64: 19529
  population_65_plus: 10625
  median_household_income: 76875
  poverty_rate: 7.9
  homeownership_rate: 82.5
  unemployment_rate: 2.92
  median_home_value: 332700
  gini_index: 0.4432
  vacancy_rate: 30.64
  race_white: 33832
  race_black: 293
  race_asian: 239
  race_native: 134
  hispanic: 512
  bachelors_plus: 15826
districts:
  - to: "us/states/me/districts/01"
    rel: in-district
    area_weight: 0.7543
  - to: "us/states/me/districts/senate/13"
    rel: in-district
    area_weight: 0.6907
  - to: "us/states/me/districts/senate/24"
    rel: in-district
    area_weight: 0.0476
  - to: "us/states/me/districts/house/47"
    rel: in-district
    area_weight: 0.2222
  - to: "us/states/me/districts/house/46"
    rel: in-district
    area_weight: 0.1543
  - to: "us/states/me/districts/house/45"
    rel: in-district
    area_weight: 0.1464
  - to: "us/states/me/districts/house/48"
    rel: in-district
    area_weight: 0.134
  - to: "us/states/me/districts/house/53"
    rel: in-district
    area_weight: 0.0475
  - to: "us/states/me/districts/house/62"
    rel: in-district
    area_weight: 0.0338
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, me]
timestamp: "2026-07-03"
---

# Lincoln County, ME

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 36099 |
| Under 18 | 5945 |
| 18–64 | 19529 |
| 65+ | 10625 |
| Median household income | 76875 |
| Poverty rate | 7.9 |
| Homeownership rate | 82.5 |
| Unemployment rate | 2.92 |
| Median home value | 332700 |
| Gini index | 0.4432 |
| Vacancy rate | 30.64 |
| White | 33832 |
| Black | 293 |
| Asian | 239 |
| Native | 134 |
| Hispanic/Latino | 512 |
| Bachelor's or higher | 15826 |

## Districts

- [ME-01](/us/states/me/districts/01.md) — 75% (congressional)
- [ME Senate District 13](/us/states/me/districts/senate/13.md) — 69% (state senate)
- [ME Senate District 24](/us/states/me/districts/senate/24.md) — 5% (state senate)
- [ME House District 47](/us/states/me/districts/house/47.md) — 22% (state house)
- [ME House District 46](/us/states/me/districts/house/46.md) — 15% (state house)
- [ME House District 45](/us/states/me/districts/house/45.md) — 15% (state house)
- [ME House District 48](/us/states/me/districts/house/48.md) — 13% (state house)
- [ME House District 53](/us/states/me/districts/house/53.md) — 5% (state house)
- [ME House District 62](/us/states/me/districts/house/62.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
