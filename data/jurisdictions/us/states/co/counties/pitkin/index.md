---
type: Jurisdiction
title: "Pitkin County, CO"
classification: county
fips: "08097"
state: "CO"
demographics:
  population: 16985
  population_under_18: 2484
  population_18_64: 10626
  population_65_plus: 3875
  median_household_income: 102645
  poverty_rate: 7.8
  homeownership_rate: 62.83
  unemployment_rate: 2.51
  median_home_value: 1139100
  gini_index: 0.5919
  vacancy_rate: 31.29
  race_white: 14200
  race_black: 95
  race_asian: 341
  race_native: 52
  hispanic: 1935
  bachelors_plus: 12168
districts:
  - to: "us/states/co/districts/03"
    rel: in-district
    area_weight: 0.9984
  - to: "us/states/co/districts/senate/5"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/co/districts/house/57"
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

# Pitkin County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16985 |
| Under 18 | 2484 |
| 18–64 | 10626 |
| 65+ | 3875 |
| Median household income | 102645 |
| Poverty rate | 7.8 |
| Homeownership rate | 62.83 |
| Unemployment rate | 2.51 |
| Median home value | 1139100 |
| Gini index | 0.5919 |
| Vacancy rate | 31.29 |
| White | 14200 |
| Black | 95 |
| Asian | 341 |
| Native | 52 |
| Hispanic/Latino | 1935 |
| Bachelor's or higher | 12168 |

## Districts

- [CO-03](/us/states/co/districts/03.md) — 100% (congressional)
- [CO Senate District 5](/us/states/co/districts/senate/5.md) — 100% (state senate)
- [CO House District 57](/us/states/co/districts/house/57.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
