---
type: Jurisdiction
title: "Golden Valley County, MT"
classification: county
fips: "30037"
state: "MT"
demographics:
  population: 899
  population_under_18: 164
  population_18_64: 476
  population_65_plus: 259
  median_household_income: 58333
  poverty_rate: 17.02
  homeownership_rate: 81.12
  unemployment_rate: 1.54
  median_home_value: 212200
  gini_index: 0.4336
  vacancy_rate: 21.99
  race_white: 813
  race_black: 7
  race_asian: 0
  race_native: 7
  hispanic: 39
  bachelors_plus: 175
districts:
  - to: "us/states/mt/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mt/districts/senate/19"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mt/districts/house/38"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Golden Valley County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 899 |
| Under 18 | 164 |
| 18–64 | 476 |
| 65+ | 259 |
| Median household income | 58333 |
| Poverty rate | 17.02 |
| Homeownership rate | 81.12 |
| Unemployment rate | 1.54 |
| Median home value | 212200 |
| Gini index | 0.4336 |
| Vacancy rate | 21.99 |
| White | 813 |
| Black | 7 |
| Asian | 0 |
| Native | 7 |
| Hispanic/Latino | 39 |
| Bachelor's or higher | 175 |

## Districts

- [MT-02](/us/states/mt/districts/02.md) — 100% (congressional)
- [MT Senate District 19](/us/states/mt/districts/senate/19.md) — 100% (state senate)
- [MT House District 38](/us/states/mt/districts/house/38.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
