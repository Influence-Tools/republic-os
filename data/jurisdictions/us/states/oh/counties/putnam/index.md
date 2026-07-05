---
type: Jurisdiction
title: "Putnam County, OH"
classification: county
fips: "39137"
state: "OH"
demographics:
  population: 34314
  population_under_18: 8753
  population_18_64: 19069
  population_65_plus: 6492
  median_household_income: 84928
  poverty_rate: 5.49
  homeownership_rate: 87.08
  unemployment_rate: 1.8
  median_home_value: 201100
  gini_index: 0.4012
  vacancy_rate: 5.27
  race_white: 31599
  race_black: 278
  race_asian: 64
  race_native: 133
  hispanic: 2315
  bachelors_plus: 8017
districts:
  - to: "us/states/oh/districts/05"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/oh/districts/senate/1"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/oh/districts/house/82"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Putnam County, OH

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 34314 |
| Under 18 | 8753 |
| 18–64 | 19069 |
| 65+ | 6492 |
| Median household income | 84928 |
| Poverty rate | 5.49 |
| Homeownership rate | 87.08 |
| Unemployment rate | 1.8 |
| Median home value | 201100 |
| Gini index | 0.4012 |
| Vacancy rate | 5.27 |
| White | 31599 |
| Black | 278 |
| Asian | 64 |
| Native | 133 |
| Hispanic/Latino | 2315 |
| Bachelor's or higher | 8017 |

## Districts

- [OH-05](/us/states/oh/districts/05.md) — 100% (congressional)
- [OH Senate District 1](/us/states/oh/districts/senate/1.md) — 100% (state senate)
- [OH House District 82](/us/states/oh/districts/house/82.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
