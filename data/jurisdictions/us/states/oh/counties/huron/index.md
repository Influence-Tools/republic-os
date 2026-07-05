---
type: Jurisdiction
title: "Huron County, OH"
classification: county
fips: "39077"
state: "OH"
demographics:
  population: 58319
  population_under_18: 13783
  population_18_64: 33728
  population_65_plus: 10808
  median_household_income: 67878
  poverty_rate: 13.21
  homeownership_rate: 74.0
  unemployment_rate: 4.54
  median_home_value: 166000
  gini_index: 0.4051
  vacancy_rate: 8.23
  race_white: 53468
  race_black: 477
  race_asian: 239
  race_native: 21
  hispanic: 4297
  bachelors_plus: 9214
districts:
  - to: "us/states/oh/districts/05"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/oh/districts/senate/13"
    rel: in-district
    area_weight: 0.8948
  - to: "us/states/oh/districts/senate/2"
    rel: in-district
    area_weight: 0.1051
  - to: "us/states/oh/districts/house/54"
    rel: in-district
    area_weight: 0.8948
  - to: "us/states/oh/districts/house/89"
    rel: in-district
    area_weight: 0.1051
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Huron County, OH

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 58319 |
| Under 18 | 13783 |
| 18–64 | 33728 |
| 65+ | 10808 |
| Median household income | 67878 |
| Poverty rate | 13.21 |
| Homeownership rate | 74.0 |
| Unemployment rate | 4.54 |
| Median home value | 166000 |
| Gini index | 0.4051 |
| Vacancy rate | 8.23 |
| White | 53468 |
| Black | 477 |
| Asian | 239 |
| Native | 21 |
| Hispanic/Latino | 4297 |
| Bachelor's or higher | 9214 |

## Districts

- [OH-05](/us/states/oh/districts/05.md) — 100% (congressional)
- [OH Senate District 13](/us/states/oh/districts/senate/13.md) — 89% (state senate)
- [OH Senate District 2](/us/states/oh/districts/senate/2.md) — 11% (state senate)
- [OH House District 54](/us/states/oh/districts/house/54.md) — 89% (state house)
- [OH House District 89](/us/states/oh/districts/house/89.md) — 11% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
