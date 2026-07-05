---
type: Jurisdiction
title: "Ontonagon County, MI"
classification: county
fips: "26131"
state: "MI"
demographics:
  population: 5850
  population_under_18: 669
  population_18_64: 2945
  population_65_plus: 2236
  median_household_income: 54398
  poverty_rate: 12.52
  homeownership_rate: 87.08
  unemployment_rate: 5.33
  median_home_value: 111700
  gini_index: 0.4209
  vacancy_rate: 39.88
  race_white: 5415
  race_black: 31
  race_asian: 24
  race_native: 28
  hispanic: 105
  bachelors_plus: 1221
districts:
  - to: "us/states/mi/districts/01"
    rel: in-district
    area_weight: 0.3528
  - to: "us/states/mi/districts/senate/38"
    rel: in-district
    area_weight: 0.3526
  - to: "us/states/mi/districts/house/110"
    rel: in-district
    area_weight: 0.3526
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Ontonagon County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5850 |
| Under 18 | 669 |
| 18–64 | 2945 |
| 65+ | 2236 |
| Median household income | 54398 |
| Poverty rate | 12.52 |
| Homeownership rate | 87.08 |
| Unemployment rate | 5.33 |
| Median home value | 111700 |
| Gini index | 0.4209 |
| Vacancy rate | 39.88 |
| White | 5415 |
| Black | 31 |
| Asian | 24 |
| Native | 28 |
| Hispanic/Latino | 105 |
| Bachelor's or higher | 1221 |

## Districts

- [MI-01](/us/states/mi/districts/01.md) — 35% (congressional)
- [MI Senate District 38](/us/states/mi/districts/senate/38.md) — 35% (state senate)
- [MI House District 110](/us/states/mi/districts/house/110.md) — 35% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
