---
type: Jurisdiction
title: "Bennett County, SD"
classification: county
fips: "46007"
state: "SD"
demographics:
  population: 3345
  population_under_18: 1174
  population_18_64: 1659
  population_65_plus: 512
  median_household_income: 53750
  poverty_rate: 29.94
  homeownership_rate: 61.2
  unemployment_rate: 10.0
  median_home_value: 156400
  gini_index: 0.4444
  vacancy_rate: 20.07
  race_white: 1214
  race_black: 6
  race_asian: 49
  race_native: 1942
  hispanic: 169
  bachelors_plus: 375
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/sd/districts/senate/27"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/sd/districts/house/27"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Bennett County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3345 |
| Under 18 | 1174 |
| 18–64 | 1659 |
| 65+ | 512 |
| Median household income | 53750 |
| Poverty rate | 29.94 |
| Homeownership rate | 61.2 |
| Unemployment rate | 10.0 |
| Median home value | 156400 |
| Gini index | 0.4444 |
| Vacancy rate | 20.07 |
| White | 1214 |
| Black | 6 |
| Asian | 49 |
| Native | 1942 |
| Hispanic/Latino | 169 |
| Bachelor's or higher | 375 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 27](/us/states/sd/districts/senate/27.md) — 100% (state senate)
- [SD House District 27](/us/states/sd/districts/house/27.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
