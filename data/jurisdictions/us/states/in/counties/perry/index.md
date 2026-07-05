---
type: Jurisdiction
title: "Perry County, IN"
classification: county
fips: "18123"
state: "IN"
demographics:
  population: 19270
  population_under_18: 3974
  population_18_64: 11537
  population_65_plus: 3759
  median_household_income: 61151
  poverty_rate: 14.96
  homeownership_rate: 75.5
  unemployment_rate: 4.49
  median_home_value: 163400
  gini_index: 0.4335
  vacancy_rate: 9.76
  race_white: 17862
  race_black: 429
  race_asian: 112
  race_native: 60
  hispanic: 302
  bachelors_plus: 2958
districts:
  - to: "us/states/in/districts/08"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/in/districts/senate/48"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/in/districts/house/74"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Perry County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19270 |
| Under 18 | 3974 |
| 18–64 | 11537 |
| 65+ | 3759 |
| Median household income | 61151 |
| Poverty rate | 14.96 |
| Homeownership rate | 75.5 |
| Unemployment rate | 4.49 |
| Median home value | 163400 |
| Gini index | 0.4335 |
| Vacancy rate | 9.76 |
| White | 17862 |
| Black | 429 |
| Asian | 112 |
| Native | 60 |
| Hispanic/Latino | 302 |
| Bachelor's or higher | 2958 |

## Districts

- [IN-08](/us/states/in/districts/08.md) — 100% (congressional)
- [IN Senate District 48](/us/states/in/districts/senate/48.md) — 100% (state senate)
- [IN House District 74](/us/states/in/districts/house/74.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
