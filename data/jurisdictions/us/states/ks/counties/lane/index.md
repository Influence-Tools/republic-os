---
type: Jurisdiction
title: "Lane County, KS"
classification: county
fips: "20101"
state: "KS"
demographics:
  population: 1461
  population_under_18: 361
  population_18_64: 725
  population_65_plus: 375
  median_household_income: 54526
  poverty_rate: 6.95
  homeownership_rate: 88.86
  unemployment_rate: 0.45
  median_home_value: 127100
  gini_index: 0.4502
  vacancy_rate: 19.25
  race_white: 1337
  race_black: 17
  race_asian: 0
  race_native: 4
  hispanic: 235
  bachelors_plus: 332
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/39"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ks/districts/house/118"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Lane County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1461 |
| Under 18 | 361 |
| 18–64 | 725 |
| 65+ | 375 |
| Median household income | 54526 |
| Poverty rate | 6.95 |
| Homeownership rate | 88.86 |
| Unemployment rate | 0.45 |
| Median home value | 127100 |
| Gini index | 0.4502 |
| Vacancy rate | 19.25 |
| White | 1337 |
| Black | 17 |
| Asian | 0 |
| Native | 4 |
| Hispanic/Latino | 235 |
| Bachelor's or higher | 332 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 39](/us/states/ks/districts/senate/39.md) — 100% (state senate)
- [KS House District 118](/us/states/ks/districts/house/118.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
