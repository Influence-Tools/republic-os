---
type: Jurisdiction
title: "Muscatine County, IA"
classification: county
fips: "19139"
state: "IA"
demographics:
  population: 42559
  population_under_18: 10171
  population_18_64: 24697
  population_65_plus: 7691
  median_household_income: 69396
  poverty_rate: 13.68
  homeownership_rate: 73.91
  unemployment_rate: 3.2
  median_home_value: 182100
  gini_index: 0.4175
  vacancy_rate: 6.01
  race_white: 34297
  race_black: 958
  race_asian: 272
  race_native: 136
  hispanic: 8005
  bachelors_plus: 8744
districts:
  - to: "us/states/ia/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/senate/48"
    rel: in-district
    area_weight: 0.7049
  - to: "us/states/ia/districts/senate/41"
    rel: in-district
    area_weight: 0.295
  - to: "us/states/ia/districts/house/95"
    rel: in-district
    area_weight: 0.4285
  - to: "us/states/ia/districts/house/82"
    rel: in-district
    area_weight: 0.295
  - to: "us/states/ia/districts/house/96"
    rel: in-district
    area_weight: 0.2764
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Muscatine County, IA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 42559 |
| Under 18 | 10171 |
| 18–64 | 24697 |
| 65+ | 7691 |
| Median household income | 69396 |
| Poverty rate | 13.68 |
| Homeownership rate | 73.91 |
| Unemployment rate | 3.2 |
| Median home value | 182100 |
| Gini index | 0.4175 |
| Vacancy rate | 6.01 |
| White | 34297 |
| Black | 958 |
| Asian | 272 |
| Native | 136 |
| Hispanic/Latino | 8005 |
| Bachelor's or higher | 8744 |

## Districts

- [IA-01](/us/states/ia/districts/01.md) — 100% (congressional)
- [IA Senate District 48](/us/states/ia/districts/senate/48.md) — 70% (state senate)
- [IA Senate District 41](/us/states/ia/districts/senate/41.md) — 30% (state senate)
- [IA House District 95](/us/states/ia/districts/house/95.md) — 43% (state house)
- [IA House District 82](/us/states/ia/districts/house/82.md) — 30% (state house)
- [IA House District 96](/us/states/ia/districts/house/96.md) — 28% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
