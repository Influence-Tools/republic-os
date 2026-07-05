---
type: Jurisdiction
title: "Atchison County, MO"
classification: county
fips: "29005"
state: "MO"
demographics:
  population: 5187
  population_under_18: 1083
  population_18_64: 2797
  population_65_plus: 1307
  median_household_income: 58750
  poverty_rate: 11.62
  homeownership_rate: 76.83
  unemployment_rate: 2.26
  median_home_value: 106800
  gini_index: 0.4488
  vacancy_rate: 16.1
  race_white: 4853
  race_black: 13
  race_asian: 22
  race_native: 7
  hispanic: 107
  bachelors_plus: 1097
districts:
  - to: "us/states/mo/districts/06"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/mo/districts/senate/12"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/mo/districts/house/1"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Atchison County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5187 |
| Under 18 | 1083 |
| 18–64 | 2797 |
| 65+ | 1307 |
| Median household income | 58750 |
| Poverty rate | 11.62 |
| Homeownership rate | 76.83 |
| Unemployment rate | 2.26 |
| Median home value | 106800 |
| Gini index | 0.4488 |
| Vacancy rate | 16.1 |
| White | 4853 |
| Black | 13 |
| Asian | 22 |
| Native | 7 |
| Hispanic/Latino | 107 |
| Bachelor's or higher | 1097 |

## Districts

- [MO-06](/us/states/mo/districts/06.md) — 100% (congressional)
- [MO Senate District 12](/us/states/mo/districts/senate/12.md) — 100% (state senate)
- [MO House District 1](/us/states/mo/districts/house/1.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
