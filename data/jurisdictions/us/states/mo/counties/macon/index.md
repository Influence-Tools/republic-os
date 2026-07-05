---
type: Jurisdiction
title: "Macon County, MO"
classification: county
fips: "29121"
state: "MO"
demographics:
  population: 15163
  population_under_18: 3500
  population_18_64: 8285
  population_65_plus: 3378
  median_household_income: 62357
  poverty_rate: 9.52
  homeownership_rate: 76.83
  unemployment_rate: 2.08
  median_home_value: 149100
  gini_index: 0.395
  vacancy_rate: 18.22
  race_white: 13958
  race_black: 323
  race_asian: 93
  race_native: 23
  hispanic: 287
  bachelors_plus: 2689
districts:
  - to: "us/states/mo/districts/06"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/18"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/house/6"
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

# Macon County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15163 |
| Under 18 | 3500 |
| 18–64 | 8285 |
| 65+ | 3378 |
| Median household income | 62357 |
| Poverty rate | 9.52 |
| Homeownership rate | 76.83 |
| Unemployment rate | 2.08 |
| Median home value | 149100 |
| Gini index | 0.395 |
| Vacancy rate | 18.22 |
| White | 13958 |
| Black | 323 |
| Asian | 93 |
| Native | 23 |
| Hispanic/Latino | 287 |
| Bachelor's or higher | 2689 |

## Districts

- [MO-06](/us/states/mo/districts/06.md) — 100% (congressional)
- [MO Senate District 18](/us/states/mo/districts/senate/18.md) — 100% (state senate)
- [MO House District 6](/us/states/mo/districts/house/6.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
