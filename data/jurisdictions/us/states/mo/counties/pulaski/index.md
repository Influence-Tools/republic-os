---
type: Jurisdiction
title: "Pulaski County, MO"
classification: county
fips: "29169"
state: "MO"
demographics:
  population: 53894
  population_under_18: 11784
  population_18_64: 36909
  population_65_plus: 5201
  median_household_income: 64466
  poverty_rate: 12.67
  homeownership_rate: 61.16
  unemployment_rate: 4.72
  median_home_value: 189800
  gini_index: 0.4089
  vacancy_rate: 13.28
  race_white: 38565
  race_black: 5611
  race_asian: 1205
  race_native: 194
  hispanic: 6199
  bachelors_plus: 10128
districts:
  - to: "us/states/mo/districts/04"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/mo/districts/senate/16"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/124"
    rel: in-district
    area_weight: 0.5785
  - to: "us/states/mo/districts/house/121"
    rel: in-district
    area_weight: 0.4213
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Pulaski County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 53894 |
| Under 18 | 11784 |
| 18–64 | 36909 |
| 65+ | 5201 |
| Median household income | 64466 |
| Poverty rate | 12.67 |
| Homeownership rate | 61.16 |
| Unemployment rate | 4.72 |
| Median home value | 189800 |
| Gini index | 0.4089 |
| Vacancy rate | 13.28 |
| White | 38565 |
| Black | 5611 |
| Asian | 1205 |
| Native | 194 |
| Hispanic/Latino | 6199 |
| Bachelor's or higher | 10128 |

## Districts

- [MO-04](/us/states/mo/districts/04.md) — 100% (congressional)
- [MO Senate District 16](/us/states/mo/districts/senate/16.md) — 100% (state senate)
- [MO House District 124](/us/states/mo/districts/house/124.md) — 58% (state house)
- [MO House District 121](/us/states/mo/districts/house/121.md) — 42% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
