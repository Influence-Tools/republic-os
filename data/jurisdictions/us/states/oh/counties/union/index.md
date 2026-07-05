---
type: Jurisdiction
title: "Union County, OH"
classification: county
fips: "39159"
state: "OH"
demographics:
  population: 67324
  population_under_18: 16248
  population_18_64: 42187
  population_65_plus: 8889
  median_household_income: 112322
  poverty_rate: 4.99
  homeownership_rate: 79.18
  unemployment_rate: 2.58
  median_home_value: 344900
  gini_index: 0.4139
  vacancy_rate: 3.68
  race_white: 57329
  race_black: 1550
  race_asian: 3375
  race_native: 90
  hispanic: 2260
  bachelors_plus: 24344
districts:
  - to: "us/states/oh/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/oh/districts/senate/26"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/oh/districts/house/86"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Union County, OH

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 67324 |
| Under 18 | 16248 |
| 18–64 | 42187 |
| 65+ | 8889 |
| Median household income | 112322 |
| Poverty rate | 4.99 |
| Homeownership rate | 79.18 |
| Unemployment rate | 2.58 |
| Median home value | 344900 |
| Gini index | 0.4139 |
| Vacancy rate | 3.68 |
| White | 57329 |
| Black | 1550 |
| Asian | 3375 |
| Native | 90 |
| Hispanic/Latino | 2260 |
| Bachelor's or higher | 24344 |

## Districts

- [OH-04](/us/states/oh/districts/04.md) — 100% (congressional)
- [OH Senate District 26](/us/states/oh/districts/senate/26.md) — 100% (state senate)
- [OH House District 86](/us/states/oh/districts/house/86.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
