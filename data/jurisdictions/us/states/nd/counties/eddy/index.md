---
type: Jurisdiction
title: "Eddy County, ND"
classification: county
fips: "38027"
state: "ND"
demographics:
  population: 2307
  population_under_18: 482
  population_18_64: 1236
  population_65_plus: 589
  median_household_income: 50850
  poverty_rate: 14.24
  homeownership_rate: 72.04
  unemployment_rate: 2.54
  median_home_value: 124000
  gini_index: 0.4869
  vacancy_rate: 13.62
  race_white: 2085
  race_black: 0
  race_asian: 0
  race_native: 98
  hispanic: 124
  bachelors_plus: 694
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/senate/14"
    rel: in-district
    area_weight: 0.8742
  - to: "us/states/nd/districts/senate/9"
    rel: in-district
    area_weight: 0.1257
  - to: "us/states/nd/districts/house/14"
    rel: in-district
    area_weight: 0.8742
  - to: "us/states/nd/districts/house/9"
    rel: in-district
    area_weight: 0.1257
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Eddy County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2307 |
| Under 18 | 482 |
| 18–64 | 1236 |
| 65+ | 589 |
| Median household income | 50850 |
| Poverty rate | 14.24 |
| Homeownership rate | 72.04 |
| Unemployment rate | 2.54 |
| Median home value | 124000 |
| Gini index | 0.4869 |
| Vacancy rate | 13.62 |
| White | 2085 |
| Black | 0 |
| Asian | 0 |
| Native | 98 |
| Hispanic/Latino | 124 |
| Bachelor's or higher | 694 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 14](/us/states/nd/districts/senate/14.md) — 87% (state senate)
- [ND Senate District 9](/us/states/nd/districts/senate/9.md) — 13% (state senate)
- [ND House District 14](/us/states/nd/districts/house/14.md) — 87% (state house)
- [ND House District 9](/us/states/nd/districts/house/9.md) — 13% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
