---
type: Jurisdiction
title: "Scott County, AR"
classification: county
fips: "05127"
state: "AR"
demographics:
  population: 9816
  population_under_18: 2218
  population_18_64: 5620
  population_65_plus: 1978
  median_household_income: 43270
  poverty_rate: 18.73
  homeownership_rate: 78.09
  unemployment_rate: 6.17
  median_home_value: 115000
  gini_index: 0.4194
  vacancy_rate: 18.04
  race_white: 8212
  race_black: 110
  race_asian: 297
  race_native: 49
  hispanic: 777
  bachelors_plus: 1071
districts:
  - to: "us/states/ar/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ar/districts/senate/5"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ar/districts/house/52"
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

# Scott County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9816 |
| Under 18 | 2218 |
| 18–64 | 5620 |
| 65+ | 1978 |
| Median household income | 43270 |
| Poverty rate | 18.73 |
| Homeownership rate | 78.09 |
| Unemployment rate | 6.17 |
| Median home value | 115000 |
| Gini index | 0.4194 |
| Vacancy rate | 18.04 |
| White | 8212 |
| Black | 110 |
| Asian | 297 |
| Native | 49 |
| Hispanic/Latino | 777 |
| Bachelor's or higher | 1071 |

## Districts

- [AR-04](/us/states/ar/districts/04.md) — 100% (congressional)
- [AR Senate District 5](/us/states/ar/districts/senate/5.md) — 100% (state senate)
- [AR House District 52](/us/states/ar/districts/house/52.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
