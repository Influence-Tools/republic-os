---
type: Jurisdiction
title: "Dade County, GA"
classification: county
fips: "13083"
state: "GA"
demographics:
  population: 16165
  population_under_18: 3221
  population_18_64: 9551
  population_65_plus: 3393
  median_household_income: 64568
  poverty_rate: 8.17
  homeownership_rate: 79.96
  unemployment_rate: 3.19
  median_home_value: 198500
  gini_index: 0.4468
  vacancy_rate: 18.14
  race_white: 14866
  race_black: 181
  race_asian: 196
  race_native: 5
  hispanic: 465
  bachelors_plus: 2696
districts:
  - to: "us/states/ga/districts/14"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ga/districts/senate/53"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ga/districts/house/1"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Dade County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16165 |
| Under 18 | 3221 |
| 18–64 | 9551 |
| 65+ | 3393 |
| Median household income | 64568 |
| Poverty rate | 8.17 |
| Homeownership rate | 79.96 |
| Unemployment rate | 3.19 |
| Median home value | 198500 |
| Gini index | 0.4468 |
| Vacancy rate | 18.14 |
| White | 14866 |
| Black | 181 |
| Asian | 196 |
| Native | 5 |
| Hispanic/Latino | 465 |
| Bachelor's or higher | 2696 |

## Districts

- [GA-14](/us/states/ga/districts/14.md) — 100% (congressional)
- [GA Senate District 53](/us/states/ga/districts/senate/53.md) — 100% (state senate)
- [GA House District 1](/us/states/ga/districts/house/1.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
