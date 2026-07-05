---
type: Jurisdiction
title: "Aitkin County, MN"
classification: county
fips: "27001"
state: "MN"
demographics:
  population: 16056
  population_under_18: 2510
  population_18_64: 8024
  population_65_plus: 5522
  median_household_income: 60833
  poverty_rate: 13.11
  homeownership_rate: 85.29
  unemployment_rate: 5.78
  median_home_value: 255800
  gini_index: 0.4375
  vacancy_rate: 49.33
  race_white: 14989
  race_black: 103
  race_asian: 38
  race_native: 236
  hispanic: 244
  bachelors_plus: 3355
districts:
  - to: "us/states/mn/districts/08"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mn/districts/senate/7"
    rel: in-district
    area_weight: 0.5113
  - to: "us/states/mn/districts/senate/10"
    rel: in-district
    area_weight: 0.4886
  - to: "us/states/mn/districts/house/7a"
    rel: in-district
    area_weight: 0.5113
  - to: "us/states/mn/districts/house/10a"
    rel: in-district
    area_weight: 0.4886
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Aitkin County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16056 |
| Under 18 | 2510 |
| 18–64 | 8024 |
| 65+ | 5522 |
| Median household income | 60833 |
| Poverty rate | 13.11 |
| Homeownership rate | 85.29 |
| Unemployment rate | 5.78 |
| Median home value | 255800 |
| Gini index | 0.4375 |
| Vacancy rate | 49.33 |
| White | 14989 |
| Black | 103 |
| Asian | 38 |
| Native | 236 |
| Hispanic/Latino | 244 |
| Bachelor's or higher | 3355 |

## Districts

- [MN-08](/us/states/mn/districts/08.md) — 100% (congressional)
- [MN Senate District 7](/us/states/mn/districts/senate/7.md) — 51% (state senate)
- [MN Senate District 10](/us/states/mn/districts/senate/10.md) — 49% (state senate)
- [MN House District 7A](/us/states/mn/districts/house/7a.md) — 51% (state house)
- [MN House District 10A](/us/states/mn/districts/house/10a.md) — 49% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
