---
type: Jurisdiction
title: "Gratiot County, MI"
classification: county
fips: "26057"
state: "MI"
demographics:
  population: 41385
  population_under_18: 8079
  population_18_64: 25929
  population_65_plus: 7377
  median_household_income: 63556
  poverty_rate: 13.97
  homeownership_rate: 78.86
  unemployment_rate: 4.18
  median_home_value: 147500
  gini_index: 0.4404
  vacancy_rate: 8.12
  race_white: 35595
  race_black: 2413
  race_asian: 169
  race_native: 108
  hispanic: 3171
  bachelors_plus: 7032
districts:
  - to: "us/states/mi/districts/02"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mi/districts/senate/34"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mi/districts/house/93"
    rel: in-district
    area_weight: 0.6789
  - to: "us/states/mi/districts/house/92"
    rel: in-district
    area_weight: 0.321
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Gratiot County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 41385 |
| Under 18 | 8079 |
| 18–64 | 25929 |
| 65+ | 7377 |
| Median household income | 63556 |
| Poverty rate | 13.97 |
| Homeownership rate | 78.86 |
| Unemployment rate | 4.18 |
| Median home value | 147500 |
| Gini index | 0.4404 |
| Vacancy rate | 8.12 |
| White | 35595 |
| Black | 2413 |
| Asian | 169 |
| Native | 108 |
| Hispanic/Latino | 3171 |
| Bachelor's or higher | 7032 |

## Districts

- [MI-02](/us/states/mi/districts/02.md) — 100% (congressional)
- [MI Senate District 34](/us/states/mi/districts/senate/34.md) — 100% (state senate)
- [MI House District 93](/us/states/mi/districts/house/93.md) — 68% (state house)
- [MI House District 92](/us/states/mi/districts/house/92.md) — 32% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
