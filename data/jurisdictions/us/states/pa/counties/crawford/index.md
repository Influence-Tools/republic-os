---
type: Jurisdiction
title: "Crawford County, PA"
classification: county
fips: "42039"
state: "PA"
demographics:
  population: 82716
  population_under_18: 17004
  population_18_64: 46929
  population_65_plus: 18783
  median_household_income: 60476
  poverty_rate: 14.32
  homeownership_rate: 74.7
  unemployment_rate: 5.01
  median_home_value: 153200
  gini_index: 0.4454
  vacancy_rate: 19.73
  race_white: 77153
  race_black: 1148
  race_asian: 457
  race_native: 46
  hispanic: 1327
  bachelors_plus: 16974
districts:
  - to: "us/states/pa/districts/16"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/pa/districts/senate/50"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/pa/districts/house/6"
    rel: in-district
    area_weight: 0.5774
  - to: "us/states/pa/districts/house/65"
    rel: in-district
    area_weight: 0.2921
  - to: "us/states/pa/districts/house/64"
    rel: in-district
    area_weight: 0.1304
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Crawford County, PA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 82716 |
| Under 18 | 17004 |
| 18–64 | 46929 |
| 65+ | 18783 |
| Median household income | 60476 |
| Poverty rate | 14.32 |
| Homeownership rate | 74.7 |
| Unemployment rate | 5.01 |
| Median home value | 153200 |
| Gini index | 0.4454 |
| Vacancy rate | 19.73 |
| White | 77153 |
| Black | 1148 |
| Asian | 457 |
| Native | 46 |
| Hispanic/Latino | 1327 |
| Bachelor's or higher | 16974 |

## Districts

- [PA-16](/us/states/pa/districts/16.md) — 100% (congressional)
- [PA Senate District 50](/us/states/pa/districts/senate/50.md) — 100% (state senate)
- [PA House District 6](/us/states/pa/districts/house/6.md) — 58% (state house)
- [PA House District 65](/us/states/pa/districts/house/65.md) — 29% (state house)
- [PA House District 64](/us/states/pa/districts/house/64.md) — 13% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
