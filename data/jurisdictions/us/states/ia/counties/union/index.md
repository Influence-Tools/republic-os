---
type: Jurisdiction
title: "Union County, IA"
classification: county
fips: "19175"
state: "IA"
demographics:
  population: 11993
  population_under_18: 2697
  population_18_64: 6806
  population_65_plus: 2490
  median_household_income: 57772
  poverty_rate: 12.37
  homeownership_rate: 72.13
  unemployment_rate: 4.03
  median_home_value: 122000
  gini_index: 0.4194
  vacancy_rate: 11.56
  race_white: 11131
  race_black: 196
  race_asian: 106
  race_native: 16
  hispanic: 460
  bachelors_plus: 2428
districts:
  - to: "us/states/ia/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/senate/9"
    rel: in-district
    area_weight: 0.5821
  - to: "us/states/ia/districts/senate/12"
    rel: in-district
    area_weight: 0.4179
  - to: "us/states/ia/districts/house/17"
    rel: in-district
    area_weight: 0.5821
  - to: "us/states/ia/districts/house/23"
    rel: in-district
    area_weight: 0.4179
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Union County, IA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11993 |
| Under 18 | 2697 |
| 18–64 | 6806 |
| 65+ | 2490 |
| Median household income | 57772 |
| Poverty rate | 12.37 |
| Homeownership rate | 72.13 |
| Unemployment rate | 4.03 |
| Median home value | 122000 |
| Gini index | 0.4194 |
| Vacancy rate | 11.56 |
| White | 11131 |
| Black | 196 |
| Asian | 106 |
| Native | 16 |
| Hispanic/Latino | 460 |
| Bachelor's or higher | 2428 |

## Districts

- [IA-03](/us/states/ia/districts/03.md) — 100% (congressional)
- [IA Senate District 9](/us/states/ia/districts/senate/9.md) — 58% (state senate)
- [IA Senate District 12](/us/states/ia/districts/senate/12.md) — 42% (state senate)
- [IA House District 17](/us/states/ia/districts/house/17.md) — 58% (state house)
- [IA House District 23](/us/states/ia/districts/house/23.md) — 42% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
