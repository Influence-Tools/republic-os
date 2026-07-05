---
type: Jurisdiction
title: "Costilla County, CO"
classification: county
fips: "08023"
state: "CO"
demographics:
  population: 3607
  population_under_18: 671
  population_18_64: 1907
  population_65_plus: 1029
  median_household_income: 36861
  poverty_rate: 21.0
  homeownership_rate: 79.04
  unemployment_rate: 3.52
  median_home_value: 184700
  gini_index: 0.5023
  vacancy_rate: 32.14
  race_white: 1595
  race_black: 91
  race_asian: 55
  race_native: 162
  hispanic: 1973
  bachelors_plus: 897
districts:
  - to: "us/states/co/districts/03"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/co/districts/senate/6"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/co/districts/house/62"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Costilla County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3607 |
| Under 18 | 671 |
| 18–64 | 1907 |
| 65+ | 1029 |
| Median household income | 36861 |
| Poverty rate | 21.0 |
| Homeownership rate | 79.04 |
| Unemployment rate | 3.52 |
| Median home value | 184700 |
| Gini index | 0.5023 |
| Vacancy rate | 32.14 |
| White | 1595 |
| Black | 91 |
| Asian | 55 |
| Native | 162 |
| Hispanic/Latino | 1973 |
| Bachelor's or higher | 897 |

## Districts

- [CO-03](/us/states/co/districts/03.md) — 100% (congressional)
- [CO Senate District 6](/us/states/co/districts/senate/6.md) — 100% (state senate)
- [CO House District 62](/us/states/co/districts/house/62.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
