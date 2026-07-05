---
type: Jurisdiction
title: "Columbia County, AR"
classification: county
fips: "05027"
state: "AR"
demographics:
  population: 22349
  population_under_18: 4796
  population_18_64: 13648
  population_65_plus: 3905
  median_household_income: 55334
  poverty_rate: 21.13
  homeownership_rate: 70.73
  unemployment_rate: 3.21
  median_home_value: 152100
  gini_index: 0.4756
  vacancy_rate: 23.76
  race_white: 13553
  race_black: 7687
  race_asian: 96
  race_native: 36
  hispanic: 774
  bachelors_plus: 4104
districts:
  - to: "us/states/ar/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ar/districts/senate/3"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ar/districts/house/99"
    rel: in-district
    area_weight: 0.757
  - to: "us/states/ar/districts/house/98"
    rel: in-district
    area_weight: 0.2429
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Columbia County, AR

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 22349 |
| Under 18 | 4796 |
| 18–64 | 13648 |
| 65+ | 3905 |
| Median household income | 55334 |
| Poverty rate | 21.13 |
| Homeownership rate | 70.73 |
| Unemployment rate | 3.21 |
| Median home value | 152100 |
| Gini index | 0.4756 |
| Vacancy rate | 23.76 |
| White | 13553 |
| Black | 7687 |
| Asian | 96 |
| Native | 36 |
| Hispanic/Latino | 774 |
| Bachelor's or higher | 4104 |

## Districts

- [AR-04](/us/states/ar/districts/04.md) — 100% (congressional)
- [AR Senate District 3](/us/states/ar/districts/senate/3.md) — 100% (state senate)
- [AR House District 99](/us/states/ar/districts/house/99.md) — 76% (state house)
- [AR House District 98](/us/states/ar/districts/house/98.md) — 24% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
