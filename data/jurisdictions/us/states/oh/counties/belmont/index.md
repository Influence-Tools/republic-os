---
type: Jurisdiction
title: "Belmont County, OH"
classification: county
fips: "39013"
state: "OH"
demographics:
  population: 65473
  population_under_18: 12261
  population_18_64: 38834
  population_65_plus: 14378
  median_household_income: 57017
  poverty_rate: 15.77
  homeownership_rate: 73.61
  unemployment_rate: 5.43
  median_home_value: 154900
  gini_index: 0.4434
  vacancy_rate: 13.73
  race_white: 59509
  race_black: 2035
  race_asian: 379
  race_native: 57
  hispanic: 885
  bachelors_plus: 12630
districts:
  - to: "us/states/oh/districts/06"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/oh/districts/senate/30"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/oh/districts/house/95"
    rel: in-district
    area_weight: 0.5496
  - to: "us/states/oh/districts/house/96"
    rel: in-district
    area_weight: 0.4502
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Belmont County, OH

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 65473 |
| Under 18 | 12261 |
| 18–64 | 38834 |
| 65+ | 14378 |
| Median household income | 57017 |
| Poverty rate | 15.77 |
| Homeownership rate | 73.61 |
| Unemployment rate | 5.43 |
| Median home value | 154900 |
| Gini index | 0.4434 |
| Vacancy rate | 13.73 |
| White | 59509 |
| Black | 2035 |
| Asian | 379 |
| Native | 57 |
| Hispanic/Latino | 885 |
| Bachelor's or higher | 12630 |

## Districts

- [OH-06](/us/states/oh/districts/06.md) — 100% (congressional)
- [OH Senate District 30](/us/states/oh/districts/senate/30.md) — 100% (state senate)
- [OH House District 95](/us/states/oh/districts/house/95.md) — 55% (state house)
- [OH House District 96](/us/states/oh/districts/house/96.md) — 45% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
