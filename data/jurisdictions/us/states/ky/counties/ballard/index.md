---
type: Jurisdiction
title: "Ballard County, KY"
classification: county
fips: "21007"
state: "KY"
demographics:
  population: 7654
  population_under_18: 1520
  population_18_64: 4469
  population_65_plus: 1665
  median_household_income: 66164
  poverty_rate: 15.01
  homeownership_rate: 75.97
  unemployment_rate: 1.62
  median_home_value: 145800
  gini_index: 0.4354
  vacancy_rate: 13.32
  race_white: 7023
  race_black: 275
  race_asian: 22
  race_native: 12
  hispanic: 119
  bachelors_plus: 1356
districts:
  - to: "us/states/ky/districts/01"
    rel: in-district
    area_weight: 0.998
  - to: "us/states/ky/districts/senate/2"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/ky/districts/house/1"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Ballard County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7654 |
| Under 18 | 1520 |
| 18–64 | 4469 |
| 65+ | 1665 |
| Median household income | 66164 |
| Poverty rate | 15.01 |
| Homeownership rate | 75.97 |
| Unemployment rate | 1.62 |
| Median home value | 145800 |
| Gini index | 0.4354 |
| Vacancy rate | 13.32 |
| White | 7023 |
| Black | 275 |
| Asian | 22 |
| Native | 12 |
| Hispanic/Latino | 119 |
| Bachelor's or higher | 1356 |

## Districts

- [KY-01](/us/states/ky/districts/01.md) — 100% (congressional)
- [KY Senate District 2](/us/states/ky/districts/senate/2.md) — 100% (state senate)
- [KY House District 1](/us/states/ky/districts/house/1.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
