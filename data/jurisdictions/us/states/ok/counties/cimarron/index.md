---
type: Jurisdiction
title: "Cimarron County, OK"
classification: county
fips: "40025"
state: "OK"
demographics:
  population: 2218
  population_under_18: 456
  population_18_64: 1158
  population_65_plus: 604
  median_household_income: 62188
  poverty_rate: 7.44
  homeownership_rate: 78.36
  unemployment_rate: 0.36
  median_home_value: 98600
  gini_index: 0.4617
  vacancy_rate: 48.24
  race_white: 1513
  race_black: 1
  race_asian: 0
  race_native: 2
  hispanic: 561
  bachelors_plus: 560
districts:
  - to: "us/states/ok/districts/03"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ok/districts/senate/27"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ok/districts/house/61"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Cimarron County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2218 |
| Under 18 | 456 |
| 18–64 | 1158 |
| 65+ | 604 |
| Median household income | 62188 |
| Poverty rate | 7.44 |
| Homeownership rate | 78.36 |
| Unemployment rate | 0.36 |
| Median home value | 98600 |
| Gini index | 0.4617 |
| Vacancy rate | 48.24 |
| White | 1513 |
| Black | 1 |
| Asian | 0 |
| Native | 2 |
| Hispanic/Latino | 561 |
| Bachelor's or higher | 560 |

## Districts

- [OK-03](/us/states/ok/districts/03.md) — 100% (congressional)
- [OK Senate District 27](/us/states/ok/districts/senate/27.md) — 100% (state senate)
- [OK House District 61](/us/states/ok/districts/house/61.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
