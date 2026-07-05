---
type: Jurisdiction
title: "Barry County, MO"
classification: county
fips: "29009"
state: "MO"
demographics:
  population: 35033
  population_under_18: 7996
  population_18_64: 19335
  population_65_plus: 7702
  median_household_income: 58346
  poverty_rate: 15.19
  homeownership_rate: 77.29
  unemployment_rate: 4.55
  median_home_value: 187800
  gini_index: 0.4547
  vacancy_rate: 21.84
  race_white: 28651
  race_black: 70
  race_asian: 695
  race_native: 257
  hispanic: 3564
  bachelors_plus: 4808
districts:
  - to: "us/states/mo/districts/07"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/29"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/house/158"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Barry County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 35033 |
| Under 18 | 7996 |
| 18–64 | 19335 |
| 65+ | 7702 |
| Median household income | 58346 |
| Poverty rate | 15.19 |
| Homeownership rate | 77.29 |
| Unemployment rate | 4.55 |
| Median home value | 187800 |
| Gini index | 0.4547 |
| Vacancy rate | 21.84 |
| White | 28651 |
| Black | 70 |
| Asian | 695 |
| Native | 257 |
| Hispanic/Latino | 3564 |
| Bachelor's or higher | 4808 |

## Districts

- [MO-07](/us/states/mo/districts/07.md) — 100% (congressional)
- [MO Senate District 29](/us/states/mo/districts/senate/29.md) — 100% (state senate)
- [MO House District 158](/us/states/mo/districts/house/158.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
