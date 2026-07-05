---
type: Jurisdiction
title: "Mono County, CA"
classification: county
fips: "06051"
state: "CA"
demographics:
  population: 13148
  population_under_18: 2329
  population_18_64: 8522
  population_65_plus: 2297
  median_household_income: 99415
  poverty_rate: 8.55
  homeownership_rate: 65.42
  unemployment_rate: 3.07
  median_home_value: 639400
  gini_index: 0.4253
  vacancy_rate: 58.0
  race_white: 9354
  race_black: 9
  race_asian: 249
  race_native: 268
  hispanic: 3568
  bachelors_plus: 4593
districts:
  - to: "us/states/ca/districts/03"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/ca/districts/senate/4"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ca/districts/house/8"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Mono County, CA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13148 |
| Under 18 | 2329 |
| 18–64 | 8522 |
| 65+ | 2297 |
| Median household income | 99415 |
| Poverty rate | 8.55 |
| Homeownership rate | 65.42 |
| Unemployment rate | 3.07 |
| Median home value | 639400 |
| Gini index | 0.4253 |
| Vacancy rate | 58.0 |
| White | 9354 |
| Black | 9 |
| Asian | 249 |
| Native | 268 |
| Hispanic/Latino | 3568 |
| Bachelor's or higher | 4593 |

## Districts

- [CA-03](/us/states/ca/districts/03.md) — 100% (congressional)
- [CA Senate District 4](/us/states/ca/districts/senate/4.md) — 100% (state senate)
- [CA House District 8](/us/states/ca/districts/house/8.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
