---
type: Jurisdiction
title: "Dillon County, SC"
classification: county
fips: "45033"
state: "SC"
demographics:
  population: 27862
  population_under_18: 7048
  population_18_64: 15804
  population_65_plus: 5010
  median_household_income: 46605
  poverty_rate: 27.66
  homeownership_rate: 64.67
  unemployment_rate: 8.95
  median_home_value: 85400
  gini_index: 0.4526
  vacancy_rate: 16.15
  race_white: 12439
  race_black: 12609
  race_asian: 9
  race_native: 619
  hispanic: 979
  bachelors_plus: 3572
districts:
  - to: "us/states/sc/districts/07"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/sc/districts/senate/30"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/sc/districts/house/55"
    rel: in-district
    area_weight: 0.8568
  - to: "us/states/sc/districts/house/54"
    rel: in-district
    area_weight: 0.1423
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Dillon County, SC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 27862 |
| Under 18 | 7048 |
| 18–64 | 15804 |
| 65+ | 5010 |
| Median household income | 46605 |
| Poverty rate | 27.66 |
| Homeownership rate | 64.67 |
| Unemployment rate | 8.95 |
| Median home value | 85400 |
| Gini index | 0.4526 |
| Vacancy rate | 16.15 |
| White | 12439 |
| Black | 12609 |
| Asian | 9 |
| Native | 619 |
| Hispanic/Latino | 979 |
| Bachelor's or higher | 3572 |

## Districts

- [SC-07](/us/states/sc/districts/07.md) — 100% (congressional)
- [SC Senate District 30](/us/states/sc/districts/senate/30.md) — 100% (state senate)
- [SC House District 55](/us/states/sc/districts/house/55.md) — 86% (state house)
- [SC House District 54](/us/states/sc/districts/house/54.md) — 14% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
