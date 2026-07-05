---
type: Jurisdiction
title: "Summit County, CO"
classification: county
fips: "08117"
state: "CO"
demographics:
  population: 31017
  population_under_18: 5423
  population_18_64: 12499
  population_65_plus: 13095
  median_household_income: 109773
  poverty_rate: 7.69
  homeownership_rate: 72.06
  unemployment_rate: 4.97
  median_home_value: 939900
  gini_index: 0.4364
  vacancy_rate: 61.1
  race_white: 23723
  race_black: 129
  race_asian: 486
  race_native: 112
  hispanic: 5334
  bachelors_plus: 18314
districts:
  - to: "us/states/co/districts/02"
    rel: in-district
    area_weight: 0.9977
  - to: "us/states/co/districts/senate/8"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/co/districts/house/13"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Summit County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 31017 |
| Under 18 | 5423 |
| 18–64 | 12499 |
| 65+ | 13095 |
| Median household income | 109773 |
| Poverty rate | 7.69 |
| Homeownership rate | 72.06 |
| Unemployment rate | 4.97 |
| Median home value | 939900 |
| Gini index | 0.4364 |
| Vacancy rate | 61.1 |
| White | 23723 |
| Black | 129 |
| Asian | 486 |
| Native | 112 |
| Hispanic/Latino | 5334 |
| Bachelor's or higher | 18314 |

## Districts

- [CO-02](/us/states/co/districts/02.md) — 100% (congressional)
- [CO Senate District 8](/us/states/co/districts/senate/8.md) — 100% (state senate)
- [CO House District 13](/us/states/co/districts/house/13.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
