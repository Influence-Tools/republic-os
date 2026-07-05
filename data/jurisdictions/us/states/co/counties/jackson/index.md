---
type: Jurisdiction
title: "Jackson County, CO"
classification: county
fips: "08057"
state: "CO"
demographics:
  population: 1372
  population_under_18: 232
  population_18_64: 693
  population_65_plus: 447
  median_household_income: 47667
  poverty_rate: 14.64
  homeownership_rate: 71.12
  unemployment_rate: 9.23
  median_home_value: 239600
  gini_index: 0.4447
  vacancy_rate: 40.56
  race_white: 1190
  race_black: 18
  race_asian: 0
  race_native: 5
  hispanic: 144
  bachelors_plus: 528
districts:
  - to: "us/states/co/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/co/districts/senate/8"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/co/districts/house/13"
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

# Jackson County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1372 |
| Under 18 | 232 |
| 18–64 | 693 |
| 65+ | 447 |
| Median household income | 47667 |
| Poverty rate | 14.64 |
| Homeownership rate | 71.12 |
| Unemployment rate | 9.23 |
| Median home value | 239600 |
| Gini index | 0.4447 |
| Vacancy rate | 40.56 |
| White | 1190 |
| Black | 18 |
| Asian | 0 |
| Native | 5 |
| Hispanic/Latino | 144 |
| Bachelor's or higher | 528 |

## Districts

- [CO-02](/us/states/co/districts/02.md) — 100% (congressional)
- [CO Senate District 8](/us/states/co/districts/senate/8.md) — 100% (state senate)
- [CO House District 13](/us/states/co/districts/house/13.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
