---
type: Jurisdiction
title: "Kalkaska County, MI"
classification: county
fips: "26079"
state: "MI"
demographics:
  population: 18239
  population_under_18: 3671
  population_18_64: 10607
  population_65_plus: 3961
  median_household_income: 68578
  poverty_rate: 12.24
  homeownership_rate: 88.18
  unemployment_rate: 3.85
  median_home_value: 188900
  gini_index: 0.4065
  vacancy_rate: 33.37
  race_white: 16970
  race_black: 148
  race_asian: 91
  race_native: 38
  hispanic: 417
  bachelors_plus: 3473
districts:
  - to: "us/states/mi/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mi/districts/senate/36"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mi/districts/house/104"
    rel: in-district
    area_weight: 0.5612
  - to: "us/states/mi/districts/house/105"
    rel: in-district
    area_weight: 0.4388
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Kalkaska County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18239 |
| Under 18 | 3671 |
| 18–64 | 10607 |
| 65+ | 3961 |
| Median household income | 68578 |
| Poverty rate | 12.24 |
| Homeownership rate | 88.18 |
| Unemployment rate | 3.85 |
| Median home value | 188900 |
| Gini index | 0.4065 |
| Vacancy rate | 33.37 |
| White | 16970 |
| Black | 148 |
| Asian | 91 |
| Native | 38 |
| Hispanic/Latino | 417 |
| Bachelor's or higher | 3473 |

## Districts

- [MI-01](/us/states/mi/districts/01.md) — 100% (congressional)
- [MI Senate District 36](/us/states/mi/districts/senate/36.md) — 100% (state senate)
- [MI House District 104](/us/states/mi/districts/house/104.md) — 56% (state house)
- [MI House District 105](/us/states/mi/districts/house/105.md) — 44% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
