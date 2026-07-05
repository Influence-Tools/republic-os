---
type: Jurisdiction
title: "Price County, WI"
classification: county
fips: "55099"
state: "WI"
demographics:
  population: 14092
  population_under_18: 2464
  population_18_64: 7613
  population_65_plus: 4015
  median_household_income: 60546
  poverty_rate: 11.86
  homeownership_rate: 81.92
  unemployment_rate: 2.89
  median_home_value: 162500
  gini_index: 0.4249
  vacancy_rate: 39.56
  race_white: 13170
  race_black: 14
  race_asian: 78
  race_native: 77
  hispanic: 247
  bachelors_plus: 2536
districts:
  - to: "us/states/wi/districts/07"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wi/districts/senate/23"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/wi/districts/house/68"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Price County, WI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14092 |
| Under 18 | 2464 |
| 18–64 | 7613 |
| 65+ | 4015 |
| Median household income | 60546 |
| Poverty rate | 11.86 |
| Homeownership rate | 81.92 |
| Unemployment rate | 2.89 |
| Median home value | 162500 |
| Gini index | 0.4249 |
| Vacancy rate | 39.56 |
| White | 13170 |
| Black | 14 |
| Asian | 78 |
| Native | 77 |
| Hispanic/Latino | 247 |
| Bachelor's or higher | 2536 |

## Districts

- [WI-07](/us/states/wi/districts/07.md) — 100% (congressional)
- [WI Senate District 23](/us/states/wi/districts/senate/23.md) — 100% (state senate)
- [WI House District 68](/us/states/wi/districts/house/68.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
