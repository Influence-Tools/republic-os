---
type: Jurisdiction
title: "Ralls County, MO"
classification: county
fips: "29173"
state: "MO"
demographics:
  population: 10428
  population_under_18: 2206
  population_18_64: 5807
  population_65_plus: 2415
  median_household_income: 65388
  poverty_rate: 11.38
  homeownership_rate: 85.52
  unemployment_rate: 4.83
  median_home_value: 168200
  gini_index: 0.4102
  vacancy_rate: 21.48
  race_white: 9688
  race_black: 187
  race_asian: 17
  race_native: 6
  hispanic: 128
  bachelors_plus: 1758
districts:
  - to: "us/states/mo/districts/06"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/18"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/5"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Ralls County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10428 |
| Under 18 | 2206 |
| 18–64 | 5807 |
| 65+ | 2415 |
| Median household income | 65388 |
| Poverty rate | 11.38 |
| Homeownership rate | 85.52 |
| Unemployment rate | 4.83 |
| Median home value | 168200 |
| Gini index | 0.4102 |
| Vacancy rate | 21.48 |
| White | 9688 |
| Black | 187 |
| Asian | 17 |
| Native | 6 |
| Hispanic/Latino | 128 |
| Bachelor's or higher | 1758 |

## Districts

- [MO-06](/us/states/mo/districts/06.md) — 100% (congressional)
- [MO Senate District 18](/us/states/mo/districts/senate/18.md) — 100% (state senate)
- [MO House District 5](/us/states/mo/districts/house/5.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
