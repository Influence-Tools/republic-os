---
type: Jurisdiction
title: "Montezuma County, CO"
classification: county
fips: "08083"
state: "CO"
demographics:
  population: 26412
  population_under_18: 5468
  population_18_64: 14345
  population_65_plus: 6599
  median_household_income: 65244
  poverty_rate: 13.25
  homeownership_rate: 76.24
  unemployment_rate: 3.86
  median_home_value: 331400
  gini_index: 0.4438
  vacancy_rate: 8.94
  race_white: 19818
  race_black: 178
  race_asian: 295
  race_native: 2797
  hispanic: 3302
  bachelors_plus: 8594
districts:
  - to: "us/states/co/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/co/districts/senate/6"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/co/districts/house/59"
    rel: in-district
    area_weight: 0.7471
  - to: "us/states/co/districts/house/58"
    rel: in-district
    area_weight: 0.2527
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Montezuma County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 26412 |
| Under 18 | 5468 |
| 18–64 | 14345 |
| 65+ | 6599 |
| Median household income | 65244 |
| Poverty rate | 13.25 |
| Homeownership rate | 76.24 |
| Unemployment rate | 3.86 |
| Median home value | 331400 |
| Gini index | 0.4438 |
| Vacancy rate | 8.94 |
| White | 19818 |
| Black | 178 |
| Asian | 295 |
| Native | 2797 |
| Hispanic/Latino | 3302 |
| Bachelor's or higher | 8594 |

## Districts

- [CO-03](/us/states/co/districts/03.md) — 100% (congressional)
- [CO Senate District 6](/us/states/co/districts/senate/6.md) — 100% (state senate)
- [CO House District 59](/us/states/co/districts/house/59.md) — 75% (state house)
- [CO House District 58](/us/states/co/districts/house/58.md) — 25% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
