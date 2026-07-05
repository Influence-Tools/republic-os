---
type: Jurisdiction
title: "Grundy County, MO"
classification: county
fips: "29079"
state: "MO"
demographics:
  population: 9787
  population_under_18: 2533
  population_18_64: 5056
  population_65_plus: 2198
  median_household_income: 51975
  poverty_rate: 17.58
  homeownership_rate: 69.75
  unemployment_rate: 3.18
  median_home_value: 112500
  gini_index: 0.5022
  vacancy_rate: 19.18
  race_white: 9059
  race_black: 50
  race_asian: 73
  race_native: 20
  hispanic: 273
  bachelors_plus: 1481
districts:
  - to: "us/states/mo/districts/06"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/12"
    rel: in-district
    area_weight: 1.0
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

# Grundy County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9787 |
| Under 18 | 2533 |
| 18–64 | 5056 |
| 65+ | 2198 |
| Median household income | 51975 |
| Poverty rate | 17.58 |
| Homeownership rate | 69.75 |
| Unemployment rate | 3.18 |
| Median home value | 112500 |
| Gini index | 0.5022 |
| Vacancy rate | 19.18 |
| White | 9059 |
| Black | 50 |
| Asian | 73 |
| Native | 20 |
| Hispanic/Latino | 273 |
| Bachelor's or higher | 1481 |

## Districts

- [MO-06](/us/states/mo/districts/06.md) — 100% (congressional)
- [MO Senate District 12](/us/states/mo/districts/senate/12.md) — 100% (state senate)
- [MO House District 2](/us/states/mo/districts/house/2.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
