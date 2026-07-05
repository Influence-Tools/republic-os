---
type: Jurisdiction
title: "Saline County, MO"
classification: county
fips: "29195"
state: "MO"
demographics:
  population: 23231
  population_under_18: 5102
  population_18_64: 14132
  population_65_plus: 3997
  median_household_income: 57931
  poverty_rate: 16.41
  homeownership_rate: 69.81
  unemployment_rate: 3.19
  median_home_value: 150500
  gini_index: 0.4439
  vacancy_rate: 17.94
  race_white: 18438
  race_black: 1138
  race_asian: 144
  race_native: 30
  hispanic: 2932
  bachelors_plus: 4564
districts:
  - to: "us/states/mo/districts/04"
    rel: in-district
    area_weight: 0.9972
  - to: "us/states/mo/districts/senate/21"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/51"
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

# Saline County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 23231 |
| Under 18 | 5102 |
| 18–64 | 14132 |
| 65+ | 3997 |
| Median household income | 57931 |
| Poverty rate | 16.41 |
| Homeownership rate | 69.81 |
| Unemployment rate | 3.19 |
| Median home value | 150500 |
| Gini index | 0.4439 |
| Vacancy rate | 17.94 |
| White | 18438 |
| Black | 1138 |
| Asian | 144 |
| Native | 30 |
| Hispanic/Latino | 2932 |
| Bachelor's or higher | 4564 |

## Districts

- [MO-04](/us/states/mo/districts/04.md) — 100% (congressional)
- [MO Senate District 21](/us/states/mo/districts/senate/21.md) — 100% (state senate)
- [MO House District 51](/us/states/mo/districts/house/51.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
