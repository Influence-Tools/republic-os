---
type: Jurisdiction
title: "Baxter County, AR"
classification: county
fips: "05005"
state: "AR"
demographics:
  population: 42407
  population_under_18: 7509
  population_18_64: 21758
  population_65_plus: 13140
  median_household_income: 48452
  poverty_rate: 15.49
  homeownership_rate: 75.2
  unemployment_rate: 6.34
  median_home_value: 174600
  gini_index: 0.4758
  vacancy_rate: 15.45
  race_white: 39118
  race_black: 136
  race_asian: 294
  race_native: 171
  hispanic: 1222
  bachelors_plus: 8035
districts:
  - to: "us/states/ar/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ar/districts/senate/23"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ar/districts/house/3"
    rel: in-district
    area_weight: 0.4721
  - to: "us/states/ar/districts/house/4"
    rel: in-district
    area_weight: 0.4465
  - to: "us/states/ar/districts/house/27"
    rel: in-district
    area_weight: 0.0814
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Baxter County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 42407 |
| Under 18 | 7509 |
| 18–64 | 21758 |
| 65+ | 13140 |
| Median household income | 48452 |
| Poverty rate | 15.49 |
| Homeownership rate | 75.2 |
| Unemployment rate | 6.34 |
| Median home value | 174600 |
| Gini index | 0.4758 |
| Vacancy rate | 15.45 |
| White | 39118 |
| Black | 136 |
| Asian | 294 |
| Native | 171 |
| Hispanic/Latino | 1222 |
| Bachelor's or higher | 8035 |

## Districts

- [AR-01](/us/states/ar/districts/01.md) — 100% (congressional)
- [AR Senate District 23](/us/states/ar/districts/senate/23.md) — 100% (state senate)
- [AR House District 3](/us/states/ar/districts/house/3.md) — 47% (state house)
- [AR House District 4](/us/states/ar/districts/house/4.md) — 45% (state house)
- [AR House District 27](/us/states/ar/districts/house/27.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
