---
type: Jurisdiction
title: "Pendleton County, KY"
classification: county
fips: "21191"
state: "KY"
demographics:
  population: 14723
  population_under_18: 3427
  population_18_64: 8723
  population_65_plus: 2573
  median_household_income: 64669
  poverty_rate: 15.91
  homeownership_rate: 74.66
  unemployment_rate: 4.52
  median_home_value: 159800
  gini_index: 0.4322
  vacancy_rate: 13.61
  race_white: 13685
  race_black: 76
  race_asian: 35
  race_native: 8
  hispanic: 237
  bachelors_plus: 2019
districts:
  - to: "us/states/ky/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ky/districts/senate/24"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ky/districts/house/78"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Pendleton County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14723 |
| Under 18 | 3427 |
| 18–64 | 8723 |
| 65+ | 2573 |
| Median household income | 64669 |
| Poverty rate | 15.91 |
| Homeownership rate | 74.66 |
| Unemployment rate | 4.52 |
| Median home value | 159800 |
| Gini index | 0.4322 |
| Vacancy rate | 13.61 |
| White | 13685 |
| Black | 76 |
| Asian | 35 |
| Native | 8 |
| Hispanic/Latino | 237 |
| Bachelor's or higher | 2019 |

## Districts

- [KY-04](/us/states/ky/districts/04.md) — 100% (congressional)
- [KY Senate District 24](/us/states/ky/districts/senate/24.md) — 100% (state senate)
- [KY House District 78](/us/states/ky/districts/house/78.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
