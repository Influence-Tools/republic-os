---
type: Jurisdiction
title: "Carbon County, WY"
classification: county
fips: "56007"
state: "WY"
demographics:
  population: 14463
  population_under_18: 3244
  population_18_64: 8451
  population_65_plus: 2768
  median_household_income: 70511
  poverty_rate: 12.17
  homeownership_rate: 76.26
  unemployment_rate: 4.96
  median_home_value: 222700
  gini_index: 0.4209
  vacancy_rate: 25.74
  race_white: 11781
  race_black: 203
  race_asian: 34
  race_native: 126
  hispanic: 2640
  bachelors_plus: 3302
districts:
  - to: "us/states/wy/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wy/districts/senate/11"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/wy/districts/house/47"
    rel: in-district
    area_weight: 0.6943
  - to: "us/states/wy/districts/house/15"
    rel: in-district
    area_weight: 0.3055
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wy]
timestamp: "2026-07-03"
---

# Carbon County, WY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14463 |
| Under 18 | 3244 |
| 18–64 | 8451 |
| 65+ | 2768 |
| Median household income | 70511 |
| Poverty rate | 12.17 |
| Homeownership rate | 76.26 |
| Unemployment rate | 4.96 |
| Median home value | 222700 |
| Gini index | 0.4209 |
| Vacancy rate | 25.74 |
| White | 11781 |
| Black | 203 |
| Asian | 34 |
| Native | 126 |
| Hispanic/Latino | 2640 |
| Bachelor's or higher | 3302 |

## Districts

- [WY-00](/us/states/wy/districts/00.md) — 100% (congressional)
- [WY Senate District 11](/us/states/wy/districts/senate/11.md) — 100% (state senate)
- [WY House District 47](/us/states/wy/districts/house/47.md) — 69% (state house)
- [WY House District 15](/us/states/wy/districts/house/15.md) — 31% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
