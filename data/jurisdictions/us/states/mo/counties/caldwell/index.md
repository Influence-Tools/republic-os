---
type: Jurisdiction
title: "Caldwell County, MO"
classification: county
fips: "29025"
state: "MO"
demographics:
  population: 8927
  population_under_18: 2100
  population_18_64: 5019
  population_65_plus: 1808
  median_household_income: 64806
  poverty_rate: 10.34
  homeownership_rate: 78.16
  unemployment_rate: 2.88
  median_home_value: 166500
  gini_index: 0.4289
  vacancy_rate: 11.84
  race_white: 8270
  race_black: 107
  race_asian: 37
  race_native: 34
  hispanic: 203
  bachelors_plus: 1660
districts:
  - to: "us/states/mo/districts/06"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/12"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/2"
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

# Caldwell County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8927 |
| Under 18 | 2100 |
| 18–64 | 5019 |
| 65+ | 1808 |
| Median household income | 64806 |
| Poverty rate | 10.34 |
| Homeownership rate | 78.16 |
| Unemployment rate | 2.88 |
| Median home value | 166500 |
| Gini index | 0.4289 |
| Vacancy rate | 11.84 |
| White | 8270 |
| Black | 107 |
| Asian | 37 |
| Native | 34 |
| Hispanic/Latino | 203 |
| Bachelor's or higher | 1660 |

## Districts

- [MO-06](/us/states/mo/districts/06.md) — 100% (congressional)
- [MO Senate District 12](/us/states/mo/districts/senate/12.md) — 100% (state senate)
- [MO House District 2](/us/states/mo/districts/house/2.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
