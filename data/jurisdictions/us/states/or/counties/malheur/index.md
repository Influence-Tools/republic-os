---
type: Jurisdiction
title: "Malheur County, OR"
classification: county
fips: "41045"
state: "OR"
demographics:
  population: 31954
  population_under_18: 8091
  population_18_64: 18391
  population_65_plus: 5472
  median_household_income: 54519
  poverty_rate: 17.57
  homeownership_rate: 63.22
  unemployment_rate: 5.24
  median_home_value: 248900
  gini_index: 0.4501
  vacancy_rate: 12.15
  race_white: 22103
  race_black: 321
  race_asian: 380
  race_native: 667
  hispanic: 10864
  bachelors_plus: 4129
districts:
  - to: "us/states/or/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/or/districts/senate/30"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/or/districts/house/60"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, or]
timestamp: "2026-07-03"
---

# Malheur County, OR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 31954 |
| Under 18 | 8091 |
| 18–64 | 18391 |
| 65+ | 5472 |
| Median household income | 54519 |
| Poverty rate | 17.57 |
| Homeownership rate | 63.22 |
| Unemployment rate | 5.24 |
| Median home value | 248900 |
| Gini index | 0.4501 |
| Vacancy rate | 12.15 |
| White | 22103 |
| Black | 321 |
| Asian | 380 |
| Native | 667 |
| Hispanic/Latino | 10864 |
| Bachelor's or higher | 4129 |

## Districts

- [OR-02](/us/states/or/districts/02.md) — 100% (congressional)
- [OR Senate District 30](/us/states/or/districts/senate/30.md) — 100% (state senate)
- [OR House District 60](/us/states/or/districts/house/60.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
