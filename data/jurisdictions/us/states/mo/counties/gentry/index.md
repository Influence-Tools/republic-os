---
type: Jurisdiction
title: "Gentry County, MO"
classification: county
fips: "29075"
state: "MO"
demographics:
  population: 6245
  population_under_18: 1613
  population_18_64: 3465
  population_65_plus: 1167
  median_household_income: 55848
  poverty_rate: 17.86
  homeownership_rate: 74.4
  unemployment_rate: 2.19
  median_home_value: 134000
  gini_index: 0.4289
  vacancy_rate: 17.0
  race_white: 5916
  race_black: 22
  race_asian: 42
  race_native: 2
  hispanic: 124
  bachelors_plus: 1251
districts:
  - to: "us/states/mo/districts/06"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/12"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/house/1"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Gentry County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6245 |
| Under 18 | 1613 |
| 18–64 | 3465 |
| 65+ | 1167 |
| Median household income | 55848 |
| Poverty rate | 17.86 |
| Homeownership rate | 74.4 |
| Unemployment rate | 2.19 |
| Median home value | 134000 |
| Gini index | 0.4289 |
| Vacancy rate | 17.0 |
| White | 5916 |
| Black | 22 |
| Asian | 42 |
| Native | 2 |
| Hispanic/Latino | 124 |
| Bachelor's or higher | 1251 |

## Districts

- [MO-06](/us/states/mo/districts/06.md) — 100% (congressional)
- [MO Senate District 12](/us/states/mo/districts/senate/12.md) — 100% (state senate)
- [MO House District 1](/us/states/mo/districts/house/1.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
