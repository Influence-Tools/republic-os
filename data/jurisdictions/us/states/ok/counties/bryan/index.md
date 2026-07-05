---
type: Jurisdiction
title: "Bryan County, OK"
classification: county
fips: "40013"
state: "OK"
demographics:
  population: 48253
  population_under_18: 11413
  population_18_64: 28492
  population_65_plus: 8348
  median_household_income: 57225
  poverty_rate: 16.57
  homeownership_rate: 63.82
  unemployment_rate: 4.6
  median_home_value: 174900
  gini_index: 0.4319
  vacancy_rate: 11.47
  race_white: 33524
  race_black: 1162
  race_asian: 347
  race_native: 6089
  hispanic: 3882
  bachelors_plus: 11305
districts:
  - to: "us/states/ok/districts/02"
    rel: in-district
    area_weight: 0.9977
  - to: "us/states/ok/districts/senate/6"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/ok/districts/house/19"
    rel: in-district
    area_weight: 0.7275
  - to: "us/states/ok/districts/house/21"
    rel: in-district
    area_weight: 0.2718
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Bryan County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 48253 |
| Under 18 | 11413 |
| 18–64 | 28492 |
| 65+ | 8348 |
| Median household income | 57225 |
| Poverty rate | 16.57 |
| Homeownership rate | 63.82 |
| Unemployment rate | 4.6 |
| Median home value | 174900 |
| Gini index | 0.4319 |
| Vacancy rate | 11.47 |
| White | 33524 |
| Black | 1162 |
| Asian | 347 |
| Native | 6089 |
| Hispanic/Latino | 3882 |
| Bachelor's or higher | 11305 |

## Districts

- [OK-02](/us/states/ok/districts/02.md) — 100% (congressional)
- [OK Senate District 6](/us/states/ok/districts/senate/6.md) — 100% (state senate)
- [OK House District 19](/us/states/ok/districts/house/19.md) — 73% (state house)
- [OK House District 21](/us/states/ok/districts/house/21.md) — 27% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
