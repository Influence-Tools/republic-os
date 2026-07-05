---
type: Jurisdiction
title: "Stoddard County, MO"
classification: county
fips: "29207"
state: "MO"
demographics:
  population: 28470
  population_under_18: 6289
  population_18_64: 16302
  population_65_plus: 5879
  median_household_income: 57957
  poverty_rate: 15.13
  homeownership_rate: 71.82
  unemployment_rate: 3.72
  median_home_value: 143300
  gini_index: 0.4262
  vacancy_rate: 13.54
  race_white: 26612
  race_black: 316
  race_asian: 42
  race_native: 137
  hispanic: 633
  bachelors_plus: 4506
districts:
  - to: "us/states/mo/districts/08"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/25"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/house/151"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Stoddard County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 28470 |
| Under 18 | 6289 |
| 18–64 | 16302 |
| 65+ | 5879 |
| Median household income | 57957 |
| Poverty rate | 15.13 |
| Homeownership rate | 71.82 |
| Unemployment rate | 3.72 |
| Median home value | 143300 |
| Gini index | 0.4262 |
| Vacancy rate | 13.54 |
| White | 26612 |
| Black | 316 |
| Asian | 42 |
| Native | 137 |
| Hispanic/Latino | 633 |
| Bachelor's or higher | 4506 |

## Districts

- [MO-08](/us/states/mo/districts/08.md) — 100% (congressional)
- [MO Senate District 25](/us/states/mo/districts/senate/25.md) — 100% (state senate)
- [MO House District 151](/us/states/mo/districts/house/151.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
