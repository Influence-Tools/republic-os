---
type: Jurisdiction
title: "Jefferson Davis Parish, LA"
classification: county
fips: "22053"
state: "LA"
demographics:
  population: 31924
  population_under_18: 8016
  population_18_64: 18376
  population_65_plus: 5532
  median_household_income: 57341
  poverty_rate: 14.56
  homeownership_rate: 77.08
  unemployment_rate: 4.71
  median_home_value: 150800
  gini_index: 0.4416
  vacancy_rate: 15.19
  race_white: 24691
  race_black: 4629
  race_asian: 61
  race_native: 89
  hispanic: 806
  bachelors_plus: 4407
districts:
  - to: "us/states/la/districts/03"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/la/districts/senate/25"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/la/districts/house/37"
    rel: in-district
    area_weight: 0.9768
  - to: "us/states/la/districts/house/32"
    rel: in-district
    area_weight: 0.0228
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Jefferson Davis Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 31924 |
| Under 18 | 8016 |
| 18–64 | 18376 |
| 65+ | 5532 |
| Median household income | 57341 |
| Poverty rate | 14.56 |
| Homeownership rate | 77.08 |
| Unemployment rate | 4.71 |
| Median home value | 150800 |
| Gini index | 0.4416 |
| Vacancy rate | 15.19 |
| White | 24691 |
| Black | 4629 |
| Asian | 61 |
| Native | 89 |
| Hispanic/Latino | 806 |
| Bachelor's or higher | 4407 |

## Districts

- [LA-03](/us/states/la/districts/03.md) — 100% (congressional)
- [LA Senate District 25](/us/states/la/districts/senate/25.md) — 100% (state senate)
- [LA House District 37](/us/states/la/districts/house/37.md) — 98% (state house)
- [LA House District 32](/us/states/la/districts/house/32.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
