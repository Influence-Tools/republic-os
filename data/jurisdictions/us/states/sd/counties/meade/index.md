---
type: Jurisdiction
title: "Meade County, SD"
classification: county
fips: "46093"
state: "SD"
demographics:
  population: 30546
  population_under_18: 7233
  population_18_64: 11081
  population_65_plus: 12232
  median_household_income: 74790
  poverty_rate: 7.1
  homeownership_rate: 72.92
  unemployment_rate: 3.2
  median_home_value: 310900
  gini_index: 0.391
  vacancy_rate: 7.02
  race_white: 26380
  race_black: 656
  race_asian: 211
  race_native: 558
  hispanic: 1489
  bachelors_plus: 7174
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/29"
    rel: in-district
    area_weight: 0.9941
  - to: "us/states/sd/districts/senate/33"
    rel: in-district
    area_weight: 0.0057
  - to: "us/states/sd/districts/house/29"
    rel: in-district
    area_weight: 0.9941
  - to: "us/states/sd/districts/house/33"
    rel: in-district
    area_weight: 0.0057
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Meade County, SD

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 30546 |
| Under 18 | 7233 |
| 18–64 | 11081 |
| 65+ | 12232 |
| Median household income | 74790 |
| Poverty rate | 7.1 |
| Homeownership rate | 72.92 |
| Unemployment rate | 3.2 |
| Median home value | 310900 |
| Gini index | 0.391 |
| Vacancy rate | 7.02 |
| White | 26380 |
| Black | 656 |
| Asian | 211 |
| Native | 558 |
| Hispanic/Latino | 1489 |
| Bachelor's or higher | 7174 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 29](/us/states/sd/districts/senate/29.md) — 99% (state senate)
- [SD Senate District 33](/us/states/sd/districts/senate/33.md) — 1% (state senate)
- [SD House District 29](/us/states/sd/districts/house/29.md) — 99% (state house)
- [SD House District 33](/us/states/sd/districts/house/33.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
