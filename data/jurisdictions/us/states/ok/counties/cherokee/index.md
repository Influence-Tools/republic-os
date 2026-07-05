---
type: Jurisdiction
title: "Cherokee County, OK"
classification: county
fips: "40021"
state: "OK"
demographics:
  population: 47942
  population_under_18: 10159
  population_18_64: 29256
  population_65_plus: 8527
  median_household_income: 53218
  poverty_rate: 18.21
  homeownership_rate: 65.73
  unemployment_rate: 5.14
  median_home_value: 168500
  gini_index: 0.4553
  vacancy_rate: 16.39
  race_white: 22152
  race_black: 607
  race_asian: 489
  race_native: 15640
  hispanic: 3829
  bachelors_plus: 12170
districts:
  - to: "us/states/ok/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ok/districts/senate/3"
    rel: in-district
    area_weight: 0.574
  - to: "us/states/ok/districts/senate/9"
    rel: in-district
    area_weight: 0.2132
  - to: "us/states/ok/districts/senate/4"
    rel: in-district
    area_weight: 0.2128
  - to: "us/states/ok/districts/house/4"
    rel: in-district
    area_weight: 0.5965
  - to: "us/states/ok/districts/house/86"
    rel: in-district
    area_weight: 0.3073
  - to: "us/states/ok/districts/house/14"
    rel: in-district
    area_weight: 0.0963
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Cherokee County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 47942 |
| Under 18 | 10159 |
| 18–64 | 29256 |
| 65+ | 8527 |
| Median household income | 53218 |
| Poverty rate | 18.21 |
| Homeownership rate | 65.73 |
| Unemployment rate | 5.14 |
| Median home value | 168500 |
| Gini index | 0.4553 |
| Vacancy rate | 16.39 |
| White | 22152 |
| Black | 607 |
| Asian | 489 |
| Native | 15640 |
| Hispanic/Latino | 3829 |
| Bachelor's or higher | 12170 |

## Districts

- [OK-02](/us/states/ok/districts/02.md) — 100% (congressional)
- [OK Senate District 3](/us/states/ok/districts/senate/3.md) — 57% (state senate)
- [OK Senate District 9](/us/states/ok/districts/senate/9.md) — 21% (state senate)
- [OK Senate District 4](/us/states/ok/districts/senate/4.md) — 21% (state senate)
- [OK House District 4](/us/states/ok/districts/house/4.md) — 60% (state house)
- [OK House District 86](/us/states/ok/districts/house/86.md) — 31% (state house)
- [OK House District 14](/us/states/ok/districts/house/14.md) — 10% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
