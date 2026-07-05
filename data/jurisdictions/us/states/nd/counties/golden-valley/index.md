---
type: Jurisdiction
title: "Golden Valley County, ND"
classification: county
fips: "38033"
state: "ND"
demographics:
  population: 1653
  population_under_18: 371
  population_18_64: 803
  population_65_plus: 479
  median_household_income: 68021
  poverty_rate: 19.83
  homeownership_rate: 79.54
  unemployment_rate: 3.43
  median_home_value: 123900
  gini_index: 0.4121
  vacancy_rate: 22.51
  race_white: 1501
  race_black: 3
  race_asian: 4
  race_native: 0
  hispanic: 10
  bachelors_plus: 326
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nd/districts/senate/39"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nd/districts/house/39"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Golden Valley County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1653 |
| Under 18 | 371 |
| 18–64 | 803 |
| 65+ | 479 |
| Median household income | 68021 |
| Poverty rate | 19.83 |
| Homeownership rate | 79.54 |
| Unemployment rate | 3.43 |
| Median home value | 123900 |
| Gini index | 0.4121 |
| Vacancy rate | 22.51 |
| White | 1501 |
| Black | 3 |
| Asian | 4 |
| Native | 0 |
| Hispanic/Latino | 10 |
| Bachelor's or higher | 326 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 39](/us/states/nd/districts/senate/39.md) — 100% (state senate)
- [ND House District 39](/us/states/nd/districts/house/39.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
