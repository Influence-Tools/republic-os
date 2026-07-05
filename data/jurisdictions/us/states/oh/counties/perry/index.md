---
type: Jurisdiction
title: "Perry County, OH"
classification: county
fips: "39127"
state: "OH"
demographics:
  population: 35535
  population_under_18: 8327
  population_18_64: 20691
  population_65_plus: 6517
  median_household_income: 67460
  poverty_rate: 14.73
  homeownership_rate: 76.37
  unemployment_rate: 3.7
  median_home_value: 191100
  gini_index: 0.4385
  vacancy_rate: 10.58
  race_white: 34057
  race_black: 73
  race_asian: 47
  race_native: 0
  hispanic: 314
  bachelors_plus: 5232
districts:
  - to: "us/states/oh/districts/12"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/oh/districts/senate/20"
    rel: in-district
    area_weight: 0.5885
  - to: "us/states/oh/districts/senate/17"
    rel: in-district
    area_weight: 0.4114
  - to: "us/states/oh/districts/house/69"
    rel: in-district
    area_weight: 0.5885
  - to: "us/states/oh/districts/house/92"
    rel: in-district
    area_weight: 0.4114
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Perry County, OH

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 35535 |
| Under 18 | 8327 |
| 18–64 | 20691 |
| 65+ | 6517 |
| Median household income | 67460 |
| Poverty rate | 14.73 |
| Homeownership rate | 76.37 |
| Unemployment rate | 3.7 |
| Median home value | 191100 |
| Gini index | 0.4385 |
| Vacancy rate | 10.58 |
| White | 34057 |
| Black | 73 |
| Asian | 47 |
| Native | 0 |
| Hispanic/Latino | 314 |
| Bachelor's or higher | 5232 |

## Districts

- [OH-12](/us/states/oh/districts/12.md) — 100% (congressional)
- [OH Senate District 20](/us/states/oh/districts/senate/20.md) — 59% (state senate)
- [OH Senate District 17](/us/states/oh/districts/senate/17.md) — 41% (state senate)
- [OH House District 69](/us/states/oh/districts/house/69.md) — 59% (state house)
- [OH House District 92](/us/states/oh/districts/house/92.md) — 41% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
