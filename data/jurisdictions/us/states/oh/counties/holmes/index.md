---
type: Jurisdiction
title: "Holmes County, OH"
classification: county
fips: "39075"
state: "OH"
demographics:
  population: 44418
  population_under_18: 13443
  population_18_64: 24546
  population_65_plus: 6429
  median_household_income: 76140
  poverty_rate: 9.26
  homeownership_rate: 78.98
  unemployment_rate: 2.24
  median_home_value: 267700
  gini_index: 0.4297
  vacancy_rate: 8.01
  race_white: 43480
  race_black: 40
  race_asian: 28
  race_native: 44
  hispanic: 467
  bachelors_plus: 3882
districts:
  - to: "us/states/oh/districts/12"
    rel: in-district
    area_weight: 0.7531
  - to: "us/states/oh/districts/07"
    rel: in-district
    area_weight: 0.2469
  - to: "us/states/oh/districts/senate/19"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/oh/districts/house/98"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Holmes County, OH

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 44418 |
| Under 18 | 13443 |
| 18–64 | 24546 |
| 65+ | 6429 |
| Median household income | 76140 |
| Poverty rate | 9.26 |
| Homeownership rate | 78.98 |
| Unemployment rate | 2.24 |
| Median home value | 267700 |
| Gini index | 0.4297 |
| Vacancy rate | 8.01 |
| White | 43480 |
| Black | 40 |
| Asian | 28 |
| Native | 44 |
| Hispanic/Latino | 467 |
| Bachelor's or higher | 3882 |

## Districts

- [OH-12](/us/states/oh/districts/12.md) — 75% (congressional)
- [OH-07](/us/states/oh/districts/07.md) — 25% (congressional)
- [OH Senate District 19](/us/states/oh/districts/senate/19.md) — 100% (state senate)
- [OH House District 98](/us/states/oh/districts/house/98.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
