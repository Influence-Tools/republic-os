---
type: Jurisdiction
title: "Jackson County, OH"
classification: county
fips: "39079"
state: "OH"
demographics:
  population: 32650
  population_under_18: 7767
  population_18_64: 19026
  population_65_plus: 5857
  median_household_income: 57106
  poverty_rate: 18.46
  homeownership_rate: 73.93
  unemployment_rate: 3.8
  median_home_value: 150700
  gini_index: 0.4784
  vacancy_rate: 11.1
  race_white: 31250
  race_black: 250
  race_asian: 171
  race_native: 111
  hispanic: 332
  bachelors_plus: 4806
districts:
  - to: "us/states/oh/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/oh/districts/senate/17"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/oh/districts/house/93"
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

# Jackson County, OH

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 32650 |
| Under 18 | 7767 |
| 18–64 | 19026 |
| 65+ | 5857 |
| Median household income | 57106 |
| Poverty rate | 18.46 |
| Homeownership rate | 73.93 |
| Unemployment rate | 3.8 |
| Median home value | 150700 |
| Gini index | 0.4784 |
| Vacancy rate | 11.1 |
| White | 31250 |
| Black | 250 |
| Asian | 171 |
| Native | 111 |
| Hispanic/Latino | 332 |
| Bachelor's or higher | 4806 |

## Districts

- [OH-02](/us/states/oh/districts/02.md) — 100% (congressional)
- [OH Senate District 17](/us/states/oh/districts/senate/17.md) — 100% (state senate)
- [OH House District 93](/us/states/oh/districts/house/93.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
