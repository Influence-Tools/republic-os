---
type: Jurisdiction
title: "Haskell County, OK"
classification: county
fips: "40061"
state: "OK"
demographics:
  population: 11683
  population_under_18: 2750
  population_18_64: 6582
  population_65_plus: 2351
  median_household_income: 49806
  poverty_rate: 20.78
  homeownership_rate: 78.34
  unemployment_rate: 6.57
  median_home_value: 138800
  gini_index: 0.4598
  vacancy_rate: 19.64
  race_white: 7996
  race_black: 32
  race_asian: 135
  race_native: 1869
  hispanic: 621
  bachelors_plus: 1623
districts:
  - to: "us/states/ok/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ok/districts/senate/7"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/house/15"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Haskell County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11683 |
| Under 18 | 2750 |
| 18–64 | 6582 |
| 65+ | 2351 |
| Median household income | 49806 |
| Poverty rate | 20.78 |
| Homeownership rate | 78.34 |
| Unemployment rate | 6.57 |
| Median home value | 138800 |
| Gini index | 0.4598 |
| Vacancy rate | 19.64 |
| White | 7996 |
| Black | 32 |
| Asian | 135 |
| Native | 1869 |
| Hispanic/Latino | 621 |
| Bachelor's or higher | 1623 |

## Districts

- [OK-02](/us/states/ok/districts/02.md) — 100% (congressional)
- [OK Senate District 7](/us/states/ok/districts/senate/7.md) — 100% (state senate)
- [OK House District 15](/us/states/ok/districts/house/15.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
