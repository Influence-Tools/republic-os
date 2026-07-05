---
type: Jurisdiction
title: "Huntington County, IN"
classification: county
fips: "18069"
state: "IN"
demographics:
  population: 36798
  population_under_18: 7963
  population_18_64: 21954
  population_65_plus: 6881
  median_household_income: 66301
  poverty_rate: 9.86
  homeownership_rate: 77.39
  unemployment_rate: 3.5
  median_home_value: 161600
  gini_index: 0.4034
  vacancy_rate: 5.73
  race_white: 34724
  race_black: 257
  race_asian: 232
  race_native: 64
  hispanic: 1164
  bachelors_plus: 7261
districts:
  - to: "us/states/in/districts/03"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/in/districts/senate/17"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/in/districts/house/50"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Huntington County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 36798 |
| Under 18 | 7963 |
| 18–64 | 21954 |
| 65+ | 6881 |
| Median household income | 66301 |
| Poverty rate | 9.86 |
| Homeownership rate | 77.39 |
| Unemployment rate | 3.5 |
| Median home value | 161600 |
| Gini index | 0.4034 |
| Vacancy rate | 5.73 |
| White | 34724 |
| Black | 257 |
| Asian | 232 |
| Native | 64 |
| Hispanic/Latino | 1164 |
| Bachelor's or higher | 7261 |

## Districts

- [IN-03](/us/states/in/districts/03.md) — 100% (congressional)
- [IN Senate District 17](/us/states/in/districts/senate/17.md) — 100% (state senate)
- [IN House District 50](/us/states/in/districts/house/50.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
