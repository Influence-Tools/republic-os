---
type: Jurisdiction
title: "Callaway County, MO"
classification: county
fips: "29027"
state: "MO"
demographics:
  population: 44741
  population_under_18: 9258
  population_18_64: 27465
  population_65_plus: 8018
  median_household_income: 74176
  poverty_rate: 11.65
  homeownership_rate: 75.52
  unemployment_rate: 5.08
  median_home_value: 201600
  gini_index: 0.4154
  vacancy_rate: 11.58
  race_white: 39537
  race_black: 1684
  race_asian: 64
  race_native: 165
  hispanic: 1098
  bachelors_plus: 10237
districts:
  - to: "us/states/mo/districts/03"
    rel: in-district
    area_weight: 0.9988
  - to: "us/states/mo/districts/senate/10"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/house/49"
    rel: in-district
    area_weight: 0.686
  - to: "us/states/mo/districts/house/43"
    rel: in-district
    area_weight: 0.3138
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Callaway County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 44741 |
| Under 18 | 9258 |
| 18–64 | 27465 |
| 65+ | 8018 |
| Median household income | 74176 |
| Poverty rate | 11.65 |
| Homeownership rate | 75.52 |
| Unemployment rate | 5.08 |
| Median home value | 201600 |
| Gini index | 0.4154 |
| Vacancy rate | 11.58 |
| White | 39537 |
| Black | 1684 |
| Asian | 64 |
| Native | 165 |
| Hispanic/Latino | 1098 |
| Bachelor's or higher | 10237 |

## Districts

- [MO-03](/us/states/mo/districts/03.md) — 100% (congressional)
- [MO Senate District 10](/us/states/mo/districts/senate/10.md) — 100% (state senate)
- [MO House District 49](/us/states/mo/districts/house/49.md) — 69% (state house)
- [MO House District 43](/us/states/mo/districts/house/43.md) — 31% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
