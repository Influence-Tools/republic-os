---
type: Jurisdiction
title: "Coal County, OK"
classification: county
fips: "40029"
state: "OK"
demographics:
  population: 5320
  population_under_18: 1284
  population_18_64: 2934
  population_65_plus: 1102
  median_household_income: 50423
  poverty_rate: 20.82
  homeownership_rate: 69.38
  unemployment_rate: 7.52
  median_home_value: 115700
  gini_index: 0.4663
  vacancy_rate: 20.66
  race_white: 3474
  race_black: 19
  race_asian: 27
  race_native: 566
  hispanic: 246
  bachelors_plus: 883
districts:
  - to: "us/states/ok/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/senate/14"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/house/18"
    rel: in-district
    area_weight: 0.7084
  - to: "us/states/ok/districts/house/22"
    rel: in-district
    area_weight: 0.2916
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Coal County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5320 |
| Under 18 | 1284 |
| 18–64 | 2934 |
| 65+ | 1102 |
| Median household income | 50423 |
| Poverty rate | 20.82 |
| Homeownership rate | 69.38 |
| Unemployment rate | 7.52 |
| Median home value | 115700 |
| Gini index | 0.4663 |
| Vacancy rate | 20.66 |
| White | 3474 |
| Black | 19 |
| Asian | 27 |
| Native | 566 |
| Hispanic/Latino | 246 |
| Bachelor's or higher | 883 |

## Districts

- [OK-02](/us/states/ok/districts/02.md) — 100% (congressional)
- [OK Senate District 14](/us/states/ok/districts/senate/14.md) — 100% (state senate)
- [OK House District 18](/us/states/ok/districts/house/18.md) — 71% (state house)
- [OK House District 22](/us/states/ok/districts/house/22.md) — 29% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
