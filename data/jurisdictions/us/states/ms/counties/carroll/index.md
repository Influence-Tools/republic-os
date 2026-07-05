---
type: Jurisdiction
title: "Carroll County, MS"
classification: county
fips: "28015"
state: "MS"
demographics:
  population: 9686
  population_under_18: 1675
  population_18_64: 5590
  population_65_plus: 2421
  median_household_income: 59327
  poverty_rate: 17.89
  homeownership_rate: 83.68
  unemployment_rate: 1.62
  median_home_value: 109600
  gini_index: 0.4342
  vacancy_rate: 14.22
  race_white: 6049
  race_black: 3335
  race_asian: 75
  race_native: 0
  hispanic: 0
  bachelors_plus: 1953
districts:
  - to: "us/states/ms/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ms/districts/senate/14"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ms/districts/house/46"
    rel: in-district
    area_weight: 0.8274
  - to: "us/states/ms/districts/house/48"
    rel: in-district
    area_weight: 0.1334
  - to: "us/states/ms/districts/house/34"
    rel: in-district
    area_weight: 0.0391
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Carroll County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9686 |
| Under 18 | 1675 |
| 18–64 | 5590 |
| 65+ | 2421 |
| Median household income | 59327 |
| Poverty rate | 17.89 |
| Homeownership rate | 83.68 |
| Unemployment rate | 1.62 |
| Median home value | 109600 |
| Gini index | 0.4342 |
| Vacancy rate | 14.22 |
| White | 6049 |
| Black | 3335 |
| Asian | 75 |
| Native | 0 |
| Hispanic/Latino | 0 |
| Bachelor's or higher | 1953 |

## Districts

- [MS-02](/us/states/ms/districts/02.md) — 100% (congressional)
- [MS Senate District 14](/us/states/ms/districts/senate/14.md) — 100% (state senate)
- [MS House District 46](/us/states/ms/districts/house/46.md) — 83% (state house)
- [MS House District 48](/us/states/ms/districts/house/48.md) — 13% (state house)
- [MS House District 34](/us/states/ms/districts/house/34.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
