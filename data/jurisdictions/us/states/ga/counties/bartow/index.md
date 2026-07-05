---
type: Jurisdiction
title: "Bartow County, GA"
classification: county
fips: "13015"
state: "GA"
demographics:
  population: 113113
  population_under_18: 26282
  population_18_64: 70311
  population_65_plus: 16520
  median_household_income: 82243
  poverty_rate: 10.32
  homeownership_rate: 72.85
  unemployment_rate: 4.73
  median_home_value: 289000
  gini_index: 0.4146
  vacancy_rate: 9.71
  race_white: 86287
  race_black: 12252
  race_asian: 1203
  race_native: 277
  hispanic: 12015
  bachelors_plus: 25016
districts:
  - to: "us/states/ga/districts/11"
    rel: in-district
    area_weight: 0.9985
  - to: "us/states/ga/districts/senate/52"
    rel: in-district
    area_weight: 0.9096
  - to: "us/states/ga/districts/senate/37"
    rel: in-district
    area_weight: 0.0903
  - to: "us/states/ga/districts/house/14"
    rel: in-district
    area_weight: 0.6878
  - to: "us/states/ga/districts/house/15"
    rel: in-district
    area_weight: 0.3121
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Bartow County, GA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 113113 |
| Under 18 | 26282 |
| 18–64 | 70311 |
| 65+ | 16520 |
| Median household income | 82243 |
| Poverty rate | 10.32 |
| Homeownership rate | 72.85 |
| Unemployment rate | 4.73 |
| Median home value | 289000 |
| Gini index | 0.4146 |
| Vacancy rate | 9.71 |
| White | 86287 |
| Black | 12252 |
| Asian | 1203 |
| Native | 277 |
| Hispanic/Latino | 12015 |
| Bachelor's or higher | 25016 |

## Districts

- [GA-11](/us/states/ga/districts/11.md) — 100% (congressional)
- [GA Senate District 52](/us/states/ga/districts/senate/52.md) — 91% (state senate)
- [GA Senate District 37](/us/states/ga/districts/senate/37.md) — 9% (state senate)
- [GA House District 14](/us/states/ga/districts/house/14.md) — 69% (state house)
- [GA House District 15](/us/states/ga/districts/house/15.md) — 31% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
