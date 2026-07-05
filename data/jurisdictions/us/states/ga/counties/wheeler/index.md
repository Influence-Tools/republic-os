---
type: Jurisdiction
title: "Wheeler County, GA"
classification: county
fips: "13309"
state: "GA"
demographics:
  population: 7335
  population_under_18: 1154
  population_18_64: 4884
  population_65_plus: 1297
  median_household_income: 40539
  poverty_rate: 32.73
  homeownership_rate: 65.57
  unemployment_rate: 5.04
  median_home_value: 88200
  gini_index: 0.4662
  vacancy_rate: 33.68
  race_white: 4301
  race_black: 2735
  race_asian: 0
  race_native: 28
  hispanic: 319
  bachelors_plus: 654
districts:
  - to: "us/states/ga/districts/12"
    rel: in-district
    area_weight: 0.993
  - to: "us/states/ga/districts/08"
    rel: in-district
    area_weight: 0.007
  - to: "us/states/ga/districts/senate/19"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ga/districts/house/156"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Wheeler County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7335 |
| Under 18 | 1154 |
| 18–64 | 4884 |
| 65+ | 1297 |
| Median household income | 40539 |
| Poverty rate | 32.73 |
| Homeownership rate | 65.57 |
| Unemployment rate | 5.04 |
| Median home value | 88200 |
| Gini index | 0.4662 |
| Vacancy rate | 33.68 |
| White | 4301 |
| Black | 2735 |
| Asian | 0 |
| Native | 28 |
| Hispanic/Latino | 319 |
| Bachelor's or higher | 654 |

## Districts

- [GA-12](/us/states/ga/districts/12.md) — 99% (congressional)
- [GA-08](/us/states/ga/districts/08.md) — 1% (congressional)
- [GA Senate District 19](/us/states/ga/districts/senate/19.md) — 100% (state senate)
- [GA House District 156](/us/states/ga/districts/house/156.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
