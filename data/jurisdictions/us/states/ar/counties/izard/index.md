---
type: Jurisdiction
title: "Izard County, AR"
classification: county
fips: "05065"
state: "AR"
demographics:
  population: 14009
  population_under_18: 2490
  population_18_64: 7996
  population_65_plus: 3523
  median_household_income: 49405
  poverty_rate: 22.28
  homeownership_rate: 75.42
  unemployment_rate: 7.17
  median_home_value: 129100
  gini_index: 0.4417
  vacancy_rate: 22.36
  race_white: 12447
  race_black: 220
  race_asian: 69
  race_native: 86
  hispanic: 414
  bachelors_plus: 2733
districts:
  - to: "us/states/ar/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ar/districts/senate/23"
    rel: in-district
    area_weight: 0.7521
  - to: "us/states/ar/districts/senate/22"
    rel: in-district
    area_weight: 0.2478
  - to: "us/states/ar/districts/house/27"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Izard County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14009 |
| Under 18 | 2490 |
| 18–64 | 7996 |
| 65+ | 3523 |
| Median household income | 49405 |
| Poverty rate | 22.28 |
| Homeownership rate | 75.42 |
| Unemployment rate | 7.17 |
| Median home value | 129100 |
| Gini index | 0.4417 |
| Vacancy rate | 22.36 |
| White | 12447 |
| Black | 220 |
| Asian | 69 |
| Native | 86 |
| Hispanic/Latino | 414 |
| Bachelor's or higher | 2733 |

## Districts

- [AR-01](/us/states/ar/districts/01.md) — 100% (congressional)
- [AR Senate District 23](/us/states/ar/districts/senate/23.md) — 75% (state senate)
- [AR Senate District 22](/us/states/ar/districts/senate/22.md) — 25% (state senate)
- [AR House District 27](/us/states/ar/districts/house/27.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
