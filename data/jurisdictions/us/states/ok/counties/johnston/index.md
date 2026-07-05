---
type: Jurisdiction
title: "Johnston County, OK"
classification: county
fips: "40069"
state: "OK"
demographics:
  population: 10278
  population_under_18: 2404
  population_18_64: 5953
  population_65_plus: 1921
  median_household_income: 52688
  poverty_rate: 22.9
  homeownership_rate: 72.22
  unemployment_rate: 4.47
  median_home_value: 116500
  gini_index: 0.4415
  vacancy_rate: 17.35
  race_white: 7012
  race_black: 236
  race_asian: 6
  race_native: 1377
  hispanic: 630
  bachelors_plus: 1760
districts:
  - to: "us/states/ok/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ok/districts/senate/14"
    rel: in-district
    area_weight: 0.7738
  - to: "us/states/ok/districts/senate/6"
    rel: in-district
    area_weight: 0.2262
  - to: "us/states/ok/districts/house/22"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Johnston County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10278 |
| Under 18 | 2404 |
| 18–64 | 5953 |
| 65+ | 1921 |
| Median household income | 52688 |
| Poverty rate | 22.9 |
| Homeownership rate | 72.22 |
| Unemployment rate | 4.47 |
| Median home value | 116500 |
| Gini index | 0.4415 |
| Vacancy rate | 17.35 |
| White | 7012 |
| Black | 236 |
| Asian | 6 |
| Native | 1377 |
| Hispanic/Latino | 630 |
| Bachelor's or higher | 1760 |

## Districts

- [OK-02](/us/states/ok/districts/02.md) — 100% (congressional)
- [OK Senate District 14](/us/states/ok/districts/senate/14.md) — 77% (state senate)
- [OK Senate District 6](/us/states/ok/districts/senate/6.md) — 23% (state senate)
- [OK House District 22](/us/states/ok/districts/house/22.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
