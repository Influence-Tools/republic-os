---
type: Jurisdiction
title: "Madison County, MO"
classification: county
fips: "29123"
state: "MO"
demographics:
  population: 12729
  population_under_18: 2966
  population_18_64: 7274
  population_65_plus: 2489
  median_household_income: 54434
  poverty_rate: 13.2
  homeownership_rate: 73.67
  unemployment_rate: 4.77
  median_home_value: 159000
  gini_index: 0.4595
  vacancy_rate: 20.17
  race_white: 11739
  race_black: 35
  race_asian: 36
  race_native: 65
  hispanic: 356
  bachelors_plus: 1865
districts:
  - to: "us/states/mo/districts/08"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/27"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/house/144"
    rel: in-district
    area_weight: 0.5587
  - to: "us/states/mo/districts/house/116"
    rel: in-district
    area_weight: 0.4413
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Madison County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12729 |
| Under 18 | 2966 |
| 18–64 | 7274 |
| 65+ | 2489 |
| Median household income | 54434 |
| Poverty rate | 13.2 |
| Homeownership rate | 73.67 |
| Unemployment rate | 4.77 |
| Median home value | 159000 |
| Gini index | 0.4595 |
| Vacancy rate | 20.17 |
| White | 11739 |
| Black | 35 |
| Asian | 36 |
| Native | 65 |
| Hispanic/Latino | 356 |
| Bachelor's or higher | 1865 |

## Districts

- [MO-08](/us/states/mo/districts/08.md) — 100% (congressional)
- [MO Senate District 27](/us/states/mo/districts/senate/27.md) — 100% (state senate)
- [MO House District 144](/us/states/mo/districts/house/144.md) — 56% (state house)
- [MO House District 116](/us/states/mo/districts/house/116.md) — 44% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
