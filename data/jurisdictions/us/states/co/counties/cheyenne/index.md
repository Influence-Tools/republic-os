---
type: Jurisdiction
title: "Cheyenne County, CO"
classification: county
fips: "08017"
state: "CO"
demographics:
  population: 1741
  population_under_18: 386
  population_18_64: 1013
  population_65_plus: 342
  median_household_income: 70865
  poverty_rate: 8.23
  homeownership_rate: 72.61
  unemployment_rate: 0.41
  median_home_value: 187500
  gini_index: 0.4261
  vacancy_rate: 20.39
  race_white: 1428
  race_black: 31
  race_asian: 0
  race_native: 2
  hispanic: 188
  bachelors_plus: 472
districts:
  - to: "us/states/co/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/co/districts/senate/35"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/co/districts/house/56"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Cheyenne County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1741 |
| Under 18 | 386 |
| 18–64 | 1013 |
| 65+ | 342 |
| Median household income | 70865 |
| Poverty rate | 8.23 |
| Homeownership rate | 72.61 |
| Unemployment rate | 0.41 |
| Median home value | 187500 |
| Gini index | 0.4261 |
| Vacancy rate | 20.39 |
| White | 1428 |
| Black | 31 |
| Asian | 0 |
| Native | 2 |
| Hispanic/Latino | 188 |
| Bachelor's or higher | 472 |

## Districts

- [CO-04](/us/states/co/districts/04.md) — 100% (congressional)
- [CO Senate District 35](/us/states/co/districts/senate/35.md) — 100% (state senate)
- [CO House District 56](/us/states/co/districts/house/56.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
