---
type: Jurisdiction
title: "Laclede County, MO"
classification: county
fips: "29105"
state: "MO"
demographics:
  population: 36390
  population_under_18: 8953
  population_18_64: 20785
  population_65_plus: 6652
  median_household_income: 53282
  poverty_rate: 18.2
  homeownership_rate: 68.21
  unemployment_rate: 5.34
  median_home_value: 168400
  gini_index: 0.4557
  vacancy_rate: 9.08
  race_white: 33231
  race_black: 209
  race_asian: 275
  race_native: 118
  hispanic: 1086
  bachelors_plus: 5465
districts:
  - to: "us/states/mo/districts/04"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/mo/districts/senate/16"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/141"
    rel: in-district
    area_weight: 0.8911
  - to: "us/states/mo/districts/house/142"
    rel: in-district
    area_weight: 0.1088
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Laclede County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 36390 |
| Under 18 | 8953 |
| 18–64 | 20785 |
| 65+ | 6652 |
| Median household income | 53282 |
| Poverty rate | 18.2 |
| Homeownership rate | 68.21 |
| Unemployment rate | 5.34 |
| Median home value | 168400 |
| Gini index | 0.4557 |
| Vacancy rate | 9.08 |
| White | 33231 |
| Black | 209 |
| Asian | 275 |
| Native | 118 |
| Hispanic/Latino | 1086 |
| Bachelor's or higher | 5465 |

## Districts

- [MO-04](/us/states/mo/districts/04.md) — 100% (congressional)
- [MO Senate District 16](/us/states/mo/districts/senate/16.md) — 100% (state senate)
- [MO House District 141](/us/states/mo/districts/house/141.md) — 89% (state house)
- [MO House District 142](/us/states/mo/districts/house/142.md) — 11% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
