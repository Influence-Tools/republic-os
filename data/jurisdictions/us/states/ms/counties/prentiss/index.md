---
type: Jurisdiction
title: "Prentiss County, MS"
classification: county
fips: "28117"
state: "MS"
demographics:
  population: 25184
  population_under_18: 5591
  population_18_64: 15197
  population_65_plus: 4396
  median_household_income: 49724
  poverty_rate: 16.78
  homeownership_rate: 77.51
  unemployment_rate: 3.45
  median_home_value: 122500
  gini_index: 0.479
  vacancy_rate: 13.17
  race_white: 20023
  race_black: 3228
  race_asian: 134
  race_native: 61
  hispanic: 382
  bachelors_plus: 4888
districts:
  - to: "us/states/ms/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ms/districts/senate/5"
    rel: in-district
    area_weight: 0.8048
  - to: "us/states/ms/districts/senate/3"
    rel: in-district
    area_weight: 0.1951
  - to: "us/states/ms/districts/house/3"
    rel: in-district
    area_weight: 0.8048
  - to: "us/states/ms/districts/house/18"
    rel: in-district
    area_weight: 0.1951
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Prentiss County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25184 |
| Under 18 | 5591 |
| 18–64 | 15197 |
| 65+ | 4396 |
| Median household income | 49724 |
| Poverty rate | 16.78 |
| Homeownership rate | 77.51 |
| Unemployment rate | 3.45 |
| Median home value | 122500 |
| Gini index | 0.479 |
| Vacancy rate | 13.17 |
| White | 20023 |
| Black | 3228 |
| Asian | 134 |
| Native | 61 |
| Hispanic/Latino | 382 |
| Bachelor's or higher | 4888 |

## Districts

- [MS-01](/us/states/ms/districts/01.md) — 100% (congressional)
- [MS Senate District 5](/us/states/ms/districts/senate/5.md) — 80% (state senate)
- [MS Senate District 3](/us/states/ms/districts/senate/3.md) — 20% (state senate)
- [MS House District 3](/us/states/ms/districts/house/3.md) — 80% (state house)
- [MS House District 18](/us/states/ms/districts/house/18.md) — 20% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
