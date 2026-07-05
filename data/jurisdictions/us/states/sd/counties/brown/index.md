---
type: Jurisdiction
title: "Brown County, SD"
classification: county
fips: "46013"
state: "SD"
demographics:
  population: 37877
  population_under_18: 8948
  population_18_64: 22198
  population_65_plus: 6731
  median_household_income: 70898
  poverty_rate: 11.72
  homeownership_rate: 67.63
  unemployment_rate: 3.29
  median_home_value: 221100
  gini_index: 0.4592
  vacancy_rate: 9.98
  race_white: 32343
  race_black: 561
  race_asian: 1121
  race_native: 1154
  hispanic: 1770
  bachelors_plus: 11184
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/1"
    rel: in-district
    area_weight: 0.9538
  - to: "us/states/sd/districts/senate/23"
    rel: in-district
    area_weight: 0.025
  - to: "us/states/sd/districts/senate/3"
    rel: in-district
    area_weight: 0.0212
  - to: "us/states/sd/districts/house/1"
    rel: in-district
    area_weight: 0.9538
  - to: "us/states/sd/districts/house/23"
    rel: in-district
    area_weight: 0.025
  - to: "us/states/sd/districts/house/3"
    rel: in-district
    area_weight: 0.0212
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Brown County, SD

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 37877 |
| Under 18 | 8948 |
| 18–64 | 22198 |
| 65+ | 6731 |
| Median household income | 70898 |
| Poverty rate | 11.72 |
| Homeownership rate | 67.63 |
| Unemployment rate | 3.29 |
| Median home value | 221100 |
| Gini index | 0.4592 |
| Vacancy rate | 9.98 |
| White | 32343 |
| Black | 561 |
| Asian | 1121 |
| Native | 1154 |
| Hispanic/Latino | 1770 |
| Bachelor's or higher | 11184 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 1](/us/states/sd/districts/senate/1.md) — 95% (state senate)
- [SD Senate District 23](/us/states/sd/districts/senate/23.md) — 2% (state senate)
- [SD Senate District 3](/us/states/sd/districts/senate/3.md) — 2% (state senate)
- [SD House District 1](/us/states/sd/districts/house/1.md) — 95% (state house)
- [SD House District 23](/us/states/sd/districts/house/23.md) — 2% (state house)
- [SD House District 3](/us/states/sd/districts/house/3.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
