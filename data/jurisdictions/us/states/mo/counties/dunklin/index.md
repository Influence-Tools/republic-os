---
type: Jurisdiction
title: "Dunklin County, MO"
classification: county
fips: "29069"
state: "MO"
demographics:
  population: 27493
  population_under_18: 7151
  population_18_64: 15191
  population_65_plus: 5151
  median_household_income: 47849
  poverty_rate: 22.03
  homeownership_rate: 62.28
  unemployment_rate: 4.76
  median_home_value: 97600
  gini_index: 0.4544
  vacancy_rate: 16.29
  race_white: 21005
  race_black: 1955
  race_asian: 96
  race_native: 28
  hispanic: 2107
  bachelors_plus: 3527
districts:
  - to: "us/states/mo/districts/08"
    rel: in-district
    area_weight: 0.9958
  - to: "us/states/mo/districts/senate/25"
    rel: in-district
    area_weight: 0.9985
  - to: "us/states/mo/districts/house/150"
    rel: in-district
    area_weight: 0.9984
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Dunklin County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 27493 |
| Under 18 | 7151 |
| 18–64 | 15191 |
| 65+ | 5151 |
| Median household income | 47849 |
| Poverty rate | 22.03 |
| Homeownership rate | 62.28 |
| Unemployment rate | 4.76 |
| Median home value | 97600 |
| Gini index | 0.4544 |
| Vacancy rate | 16.29 |
| White | 21005 |
| Black | 1955 |
| Asian | 96 |
| Native | 28 |
| Hispanic/Latino | 2107 |
| Bachelor's or higher | 3527 |

## Districts

- [MO-08](/us/states/mo/districts/08.md) — 100% (congressional)
- [MO Senate District 25](/us/states/mo/districts/senate/25.md) — 100% (state senate)
- [MO House District 150](/us/states/mo/districts/house/150.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
