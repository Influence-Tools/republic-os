---
type: Jurisdiction
title: "Morgan County, OH"
classification: county
fips: "39115"
state: "OH"
demographics:
  population: 13651
  population_under_18: 2851
  population_18_64: 7726
  population_65_plus: 3074
  median_household_income: 59351
  poverty_rate: 12.91
  homeownership_rate: 78.89
  unemployment_rate: 3.48
  median_home_value: 150900
  gini_index: 0.407
  vacancy_rate: 21.95
  race_white: 12349
  race_black: 399
  race_asian: 18
  race_native: 15
  hispanic: 157
  bachelors_plus: 1769
districts:
  - to: "us/states/oh/districts/12"
    rel: in-district
    area_weight: 0.9983
  - to: "us/states/oh/districts/senate/30"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/oh/districts/house/95"
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

# Morgan County, OH

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13651 |
| Under 18 | 2851 |
| 18–64 | 7726 |
| 65+ | 3074 |
| Median household income | 59351 |
| Poverty rate | 12.91 |
| Homeownership rate | 78.89 |
| Unemployment rate | 3.48 |
| Median home value | 150900 |
| Gini index | 0.407 |
| Vacancy rate | 21.95 |
| White | 12349 |
| Black | 399 |
| Asian | 18 |
| Native | 15 |
| Hispanic/Latino | 157 |
| Bachelor's or higher | 1769 |

## Districts

- [OH-12](/us/states/oh/districts/12.md) — 100% (congressional)
- [OH Senate District 30](/us/states/oh/districts/senate/30.md) — 100% (state senate)
- [OH House District 95](/us/states/oh/districts/house/95.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
