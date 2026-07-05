---
type: Jurisdiction
title: "Quitman County, MS"
classification: county
fips: "28119"
state: "MS"
demographics:
  population: 5774
  population_under_18: 1334
  population_18_64: 3379
  population_65_plus: 1061
  median_household_income: 32412
  poverty_rate: 29.63
  homeownership_rate: 64.66
  unemployment_rate: 12.36
  median_home_value: 69600
  gini_index: 0.4868
  vacancy_rate: 12.66
  race_white: 1409
  race_black: 4258
  race_asian: 0
  race_native: 16
  hispanic: 17
  bachelors_plus: 867
districts:
  - to: "us/states/ms/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ms/districts/senate/11"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ms/districts/house/9"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Quitman County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5774 |
| Under 18 | 1334 |
| 18–64 | 3379 |
| 65+ | 1061 |
| Median household income | 32412 |
| Poverty rate | 29.63 |
| Homeownership rate | 64.66 |
| Unemployment rate | 12.36 |
| Median home value | 69600 |
| Gini index | 0.4868 |
| Vacancy rate | 12.66 |
| White | 1409 |
| Black | 4258 |
| Asian | 0 |
| Native | 16 |
| Hispanic/Latino | 17 |
| Bachelor's or higher | 867 |

## Districts

- [MS-02](/us/states/ms/districts/02.md) — 100% (congressional)
- [MS Senate District 11](/us/states/ms/districts/senate/11.md) — 100% (state senate)
- [MS House District 9](/us/states/ms/districts/house/9.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
