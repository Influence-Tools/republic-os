---
type: Jurisdiction
title: "Morrow County, OR"
classification: county
fips: "41049"
state: "OR"
demographics:
  population: 12300
  population_under_18: 3340
  population_18_64: 6925
  population_65_plus: 2035
  median_household_income: 75448
  poverty_rate: 13.21
  homeownership_rate: 71.61
  unemployment_rate: 2.4
  median_home_value: 240400
  gini_index: 0.4157
  vacancy_rate: 11.93
  race_white: 7278
  race_black: 103
  race_asian: 27
  race_native: 207
  hispanic: 5167
  bachelors_plus: 1017
districts:
  - to: "us/states/or/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/or/districts/senate/29"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/or/districts/house/57"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, or]
timestamp: "2026-07-03"
---

# Morrow County, OR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12300 |
| Under 18 | 3340 |
| 18–64 | 6925 |
| 65+ | 2035 |
| Median household income | 75448 |
| Poverty rate | 13.21 |
| Homeownership rate | 71.61 |
| Unemployment rate | 2.4 |
| Median home value | 240400 |
| Gini index | 0.4157 |
| Vacancy rate | 11.93 |
| White | 7278 |
| Black | 103 |
| Asian | 27 |
| Native | 207 |
| Hispanic/Latino | 5167 |
| Bachelor's or higher | 1017 |

## Districts

- [OR-02](/us/states/or/districts/02.md) — 100% (congressional)
- [OR Senate District 29](/us/states/or/districts/senate/29.md) — 100% (state senate)
- [OR House District 57](/us/states/or/districts/house/57.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
