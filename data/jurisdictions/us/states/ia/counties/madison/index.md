---
type: Jurisdiction
title: "Madison County, IA"
classification: county
fips: "19121"
state: "IA"
demographics:
  population: 16926
  population_under_18: 4258
  population_18_64: 9673
  population_65_plus: 2995
  median_household_income: 90855
  poverty_rate: 7.04
  homeownership_rate: 80.14
  unemployment_rate: 3.46
  median_home_value: 245100
  gini_index: 0.391
  vacancy_rate: 5.69
  race_white: 16101
  race_black: 149
  race_asian: 76
  race_native: 16
  hispanic: 383
  bachelors_plus: 3858
districts:
  - to: "us/states/ia/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/senate/12"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/house/23"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Madison County, IA

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16926 |
| Under 18 | 4258 |
| 18–64 | 9673 |
| 65+ | 2995 |
| Median household income | 90855 |
| Poverty rate | 7.04 |
| Homeownership rate | 80.14 |
| Unemployment rate | 3.46 |
| Median home value | 245100 |
| Gini index | 0.391 |
| Vacancy rate | 5.69 |
| White | 16101 |
| Black | 149 |
| Asian | 76 |
| Native | 16 |
| Hispanic/Latino | 383 |
| Bachelor's or higher | 3858 |

## Districts

- [IA-03](/us/states/ia/districts/03.md) — 100% (congressional)
- [IA Senate District 12](/us/states/ia/districts/senate/12.md) — 100% (state senate)
- [IA House District 23](/us/states/ia/districts/house/23.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
