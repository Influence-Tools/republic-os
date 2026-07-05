---
type: Jurisdiction
title: "Putnam County, MO"
classification: county
fips: "29171"
state: "MO"
demographics:
  population: 4642
  population_under_18: 1049
  population_18_64: 2431
  population_65_plus: 1162
  median_household_income: 63510
  poverty_rate: 15.52
  homeownership_rate: 83.03
  unemployment_rate: 3.99
  median_home_value: 119500
  gini_index: 0.4448
  vacancy_rate: 36.8
  race_white: 4458
  race_black: 9
  race_asian: 0
  race_native: 23
  hispanic: 139
  bachelors_plus: 988
districts:
  - to: "us/states/mo/districts/06"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/senate/18"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/house/3"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Putnam County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4642 |
| Under 18 | 1049 |
| 18–64 | 2431 |
| 65+ | 1162 |
| Median household income | 63510 |
| Poverty rate | 15.52 |
| Homeownership rate | 83.03 |
| Unemployment rate | 3.99 |
| Median home value | 119500 |
| Gini index | 0.4448 |
| Vacancy rate | 36.8 |
| White | 4458 |
| Black | 9 |
| Asian | 0 |
| Native | 23 |
| Hispanic/Latino | 139 |
| Bachelor's or higher | 988 |

## Districts

- [MO-06](/us/states/mo/districts/06.md) — 100% (congressional)
- [MO Senate District 18](/us/states/mo/districts/senate/18.md) — 100% (state senate)
- [MO House District 3](/us/states/mo/districts/house/3.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
