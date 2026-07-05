---
type: Jurisdiction
title: "Delaware County, IA"
classification: county
fips: "19055"
state: "IA"
demographics:
  population: 17558
  population_under_18: 4084
  population_18_64: 9690
  population_65_plus: 3784
  median_household_income: 74989
  poverty_rate: 7.76
  homeownership_rate: 79.59
  unemployment_rate: 2.05
  median_home_value: 177900
  gini_index: 0.4399
  vacancy_rate: 9.79
  race_white: 16536
  race_black: 13
  race_asian: 0
  race_native: 188
  hispanic: 301
  bachelors_plus: 3555
districts:
  - to: "us/states/ia/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/senate/34"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/house/67"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Delaware County, IA

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17558 |
| Under 18 | 4084 |
| 18–64 | 9690 |
| 65+ | 3784 |
| Median household income | 74989 |
| Poverty rate | 7.76 |
| Homeownership rate | 79.59 |
| Unemployment rate | 2.05 |
| Median home value | 177900 |
| Gini index | 0.4399 |
| Vacancy rate | 9.79 |
| White | 16536 |
| Black | 13 |
| Asian | 0 |
| Native | 188 |
| Hispanic/Latino | 301 |
| Bachelor's or higher | 3555 |

## Districts

- [IA-02](/us/states/ia/districts/02.md) — 100% (congressional)
- [IA Senate District 34](/us/states/ia/districts/senate/34.md) — 100% (state senate)
- [IA House District 67](/us/states/ia/districts/house/67.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
