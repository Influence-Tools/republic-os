---
type: Jurisdiction
title: "Pike County, AR"
classification: county
fips: "05109"
state: "AR"
demographics:
  population: 10115
  population_under_18: 2253
  population_18_64: 5739
  population_65_plus: 2123
  median_household_income: 49269
  poverty_rate: 20.66
  homeownership_rate: 74.99
  unemployment_rate: 3.88
  median_home_value: 121600
  gini_index: 0.5057
  vacancy_rate: 23.33
  race_white: 8748
  race_black: 331
  race_asian: 49
  race_native: 30
  hispanic: 807
  bachelors_plus: 1853
districts:
  - to: "us/states/ar/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ar/districts/senate/3"
    rel: in-district
    area_weight: 0.5194
  - to: "us/states/ar/districts/senate/5"
    rel: in-district
    area_weight: 0.4805
  - to: "us/states/ar/districts/house/89"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Pike County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10115 |
| Under 18 | 2253 |
| 18–64 | 5739 |
| 65+ | 2123 |
| Median household income | 49269 |
| Poverty rate | 20.66 |
| Homeownership rate | 74.99 |
| Unemployment rate | 3.88 |
| Median home value | 121600 |
| Gini index | 0.5057 |
| Vacancy rate | 23.33 |
| White | 8748 |
| Black | 331 |
| Asian | 49 |
| Native | 30 |
| Hispanic/Latino | 807 |
| Bachelor's or higher | 1853 |

## Districts

- [AR-04](/us/states/ar/districts/04.md) — 100% (congressional)
- [AR Senate District 3](/us/states/ar/districts/senate/3.md) — 52% (state senate)
- [AR Senate District 5](/us/states/ar/districts/senate/5.md) — 48% (state senate)
- [AR House District 89](/us/states/ar/districts/house/89.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
