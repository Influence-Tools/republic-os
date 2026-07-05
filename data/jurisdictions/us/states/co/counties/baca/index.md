---
type: Jurisdiction
title: "Baca County, CO"
classification: county
fips: "08009"
state: "CO"
demographics:
  population: 3428
  population_under_18: 768
  population_18_64: 1776
  population_65_plus: 884
  median_household_income: 46215
  poverty_rate: 24.62
  homeownership_rate: 71.51
  unemployment_rate: 0.58
  median_home_value: 122900
  gini_index: 0.4733
  vacancy_rate: 16.44
  race_white: 3027
  race_black: 13
  race_asian: 88
  race_native: 16
  hispanic: 375
  bachelors_plus: 774
districts:
  - to: "us/states/co/districts/04"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/co/districts/senate/35"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/co/districts/house/47"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Baca County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3428 |
| Under 18 | 768 |
| 18–64 | 1776 |
| 65+ | 884 |
| Median household income | 46215 |
| Poverty rate | 24.62 |
| Homeownership rate | 71.51 |
| Unemployment rate | 0.58 |
| Median home value | 122900 |
| Gini index | 0.4733 |
| Vacancy rate | 16.44 |
| White | 3027 |
| Black | 13 |
| Asian | 88 |
| Native | 16 |
| Hispanic/Latino | 375 |
| Bachelor's or higher | 774 |

## Districts

- [CO-04](/us/states/co/districts/04.md) — 100% (congressional)
- [CO Senate District 35](/us/states/co/districts/senate/35.md) — 100% (state senate)
- [CO House District 47](/us/states/co/districts/house/47.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
