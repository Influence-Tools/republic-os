---
type: Jurisdiction
title: "Bryan County, GA"
classification: county
fips: "13029"
state: "GA"
demographics:
  population: 48263
  population_under_18: 14061
  population_18_64: 28930
  population_65_plus: 5272
  median_household_income: 103408
  poverty_rate: 6.7
  homeownership_rate: 77.72
  unemployment_rate: 5.34
  median_home_value: 343200
  gini_index: 0.4126
  vacancy_rate: 7.54
  race_white: 34054
  race_black: 6461
  race_asian: 1270
  race_native: 28
  hispanic: 3972
  bachelors_plus: 14988
districts:
  - to: "us/states/ga/districts/01"
    rel: in-district
    area_weight: 0.9951
  - to: "us/states/ga/districts/senate/1"
    rel: in-district
    area_weight: 0.9955
  - to: "us/states/ga/districts/house/164"
    rel: in-district
    area_weight: 0.5025
  - to: "us/states/ga/districts/house/160"
    rel: in-district
    area_weight: 0.3104
  - to: "us/states/ga/districts/house/166"
    rel: in-district
    area_weight: 0.1821
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Bryan County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 48263 |
| Under 18 | 14061 |
| 18–64 | 28930 |
| 65+ | 5272 |
| Median household income | 103408 |
| Poverty rate | 6.7 |
| Homeownership rate | 77.72 |
| Unemployment rate | 5.34 |
| Median home value | 343200 |
| Gini index | 0.4126 |
| Vacancy rate | 7.54 |
| White | 34054 |
| Black | 6461 |
| Asian | 1270 |
| Native | 28 |
| Hispanic/Latino | 3972 |
| Bachelor's or higher | 14988 |

## Districts

- [GA-01](/us/states/ga/districts/01.md) — 100% (congressional)
- [GA Senate District 1](/us/states/ga/districts/senate/1.md) — 100% (state senate)
- [GA House District 164](/us/states/ga/districts/house/164.md) — 50% (state house)
- [GA House District 160](/us/states/ga/districts/house/160.md) — 31% (state house)
- [GA House District 166](/us/states/ga/districts/house/166.md) — 18% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
