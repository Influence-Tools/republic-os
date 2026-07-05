---
type: Jurisdiction
title: "Desha County, AR"
classification: county
fips: "05041"
state: "AR"
demographics:
  population: 10786
  population_under_18: 2690
  population_18_64: 5928
  population_65_plus: 2168
  median_household_income: 37662
  poverty_rate: 28.33
  homeownership_rate: 56.81
  unemployment_rate: 7.99
  median_home_value: 90900
  gini_index: 0.4858
  vacancy_rate: 20.5
  race_white: 4747
  race_black: 5288
  race_asian: 0
  race_native: 19
  hispanic: 781
  bachelors_plus: 1329
districts:
  - to: "us/states/ar/districts/01"
    rel: in-district
    area_weight: 0.9979
  - to: "us/states/ar/districts/senate/8"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/ar/districts/house/62"
    rel: in-district
    area_weight: 0.7051
  - to: "us/states/ar/districts/house/94"
    rel: in-district
    area_weight: 0.2003
  - to: "us/states/ar/districts/house/64"
    rel: in-district
    area_weight: 0.094
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Desha County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10786 |
| Under 18 | 2690 |
| 18–64 | 5928 |
| 65+ | 2168 |
| Median household income | 37662 |
| Poverty rate | 28.33 |
| Homeownership rate | 56.81 |
| Unemployment rate | 7.99 |
| Median home value | 90900 |
| Gini index | 0.4858 |
| Vacancy rate | 20.5 |
| White | 4747 |
| Black | 5288 |
| Asian | 0 |
| Native | 19 |
| Hispanic/Latino | 781 |
| Bachelor's or higher | 1329 |

## Districts

- [AR-01](/us/states/ar/districts/01.md) — 100% (congressional)
- [AR Senate District 8](/us/states/ar/districts/senate/8.md) — 100% (state senate)
- [AR House District 62](/us/states/ar/districts/house/62.md) — 71% (state house)
- [AR House District 94](/us/states/ar/districts/house/94.md) — 20% (state house)
- [AR House District 64](/us/states/ar/districts/house/64.md) — 9% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
