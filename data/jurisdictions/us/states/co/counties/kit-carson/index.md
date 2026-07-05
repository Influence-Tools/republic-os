---
type: Jurisdiction
title: "Kit Carson County, CO"
classification: county
fips: "08063"
state: "CO"
demographics:
  population: 7023
  population_under_18: 1835
  population_18_64: 3794
  population_65_plus: 1394
  median_household_income: 70259
  poverty_rate: 9.83
  homeownership_rate: 72.62
  unemployment_rate: 2.42
  median_home_value: 239500
  gini_index: 0.4903
  vacancy_rate: 15.52
  race_white: 5523
  race_black: 4
  race_asian: 17
  race_native: 52
  hispanic: 1418
  bachelors_plus: 1227
districts:
  - to: "us/states/co/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/co/districts/senate/35"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/co/districts/house/56"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Kit Carson County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7023 |
| Under 18 | 1835 |
| 18–64 | 3794 |
| 65+ | 1394 |
| Median household income | 70259 |
| Poverty rate | 9.83 |
| Homeownership rate | 72.62 |
| Unemployment rate | 2.42 |
| Median home value | 239500 |
| Gini index | 0.4903 |
| Vacancy rate | 15.52 |
| White | 5523 |
| Black | 4 |
| Asian | 17 |
| Native | 52 |
| Hispanic/Latino | 1418 |
| Bachelor's or higher | 1227 |

## Districts

- [CO-04](/us/states/co/districts/04.md) — 100% (congressional)
- [CO Senate District 35](/us/states/co/districts/senate/35.md) — 100% (state senate)
- [CO House District 56](/us/states/co/districts/house/56.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
