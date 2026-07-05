---
type: Jurisdiction
title: "Lenawee County, MI"
classification: county
fips: "26091"
state: "MI"
demographics:
  population: 98415
  population_under_18: 20217
  population_18_64: 58175
  population_65_plus: 20023
  median_household_income: 70518
  poverty_rate: 10.71
  homeownership_rate: 79.56
  unemployment_rate: 4.72
  median_home_value: 196800
  gini_index: 0.4108
  vacancy_rate: 11.17
  race_white: 85816
  race_black: 2335
  race_asian: 355
  race_native: 259
  hispanic: 8797
  bachelors_plus: 21196
districts:
  - to: "us/states/mi/districts/05"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/mi/districts/senate/16"
    rel: in-district
    area_weight: 0.9084
  - to: "us/states/mi/districts/senate/15"
    rel: in-district
    area_weight: 0.0914
  - to: "us/states/mi/districts/house/34"
    rel: in-district
    area_weight: 0.8714
  - to: "us/states/mi/districts/house/30"
    rel: in-district
    area_weight: 0.0825
  - to: "us/states/mi/districts/house/31"
    rel: in-district
    area_weight: 0.043
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Lenawee County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 98415 |
| Under 18 | 20217 |
| 18–64 | 58175 |
| 65+ | 20023 |
| Median household income | 70518 |
| Poverty rate | 10.71 |
| Homeownership rate | 79.56 |
| Unemployment rate | 4.72 |
| Median home value | 196800 |
| Gini index | 0.4108 |
| Vacancy rate | 11.17 |
| White | 85816 |
| Black | 2335 |
| Asian | 355 |
| Native | 259 |
| Hispanic/Latino | 8797 |
| Bachelor's or higher | 21196 |

## Districts

- [MI-05](/us/states/mi/districts/05.md) — 100% (congressional)
- [MI Senate District 16](/us/states/mi/districts/senate/16.md) — 91% (state senate)
- [MI Senate District 15](/us/states/mi/districts/senate/15.md) — 9% (state senate)
- [MI House District 34](/us/states/mi/districts/house/34.md) — 87% (state house)
- [MI House District 30](/us/states/mi/districts/house/30.md) — 8% (state house)
- [MI House District 31](/us/states/mi/districts/house/31.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
