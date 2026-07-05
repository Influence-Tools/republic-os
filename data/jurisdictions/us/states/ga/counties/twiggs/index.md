---
type: Jurisdiction
title: "Twiggs County, GA"
classification: county
fips: "13289"
state: "GA"
demographics:
  population: 7803
  population_under_18: 1467
  population_18_64: 4420
  population_65_plus: 1916
  median_household_income: 56324
  poverty_rate: 18.17
  homeownership_rate: 88.16
  unemployment_rate: 3.76
  median_home_value: 111300
  gini_index: 0.5105
  vacancy_rate: 28.78
  race_white: 4293
  race_black: 3075
  race_asian: 76
  race_native: 45
  hispanic: 88
  bachelors_plus: 876
districts:
  - to: "us/states/ga/districts/08"
    rel: in-district
    area_weight: 0.9953
  - to: "us/states/ga/districts/senate/26"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ga/districts/house/133"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Twiggs County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7803 |
| Under 18 | 1467 |
| 18–64 | 4420 |
| 65+ | 1916 |
| Median household income | 56324 |
| Poverty rate | 18.17 |
| Homeownership rate | 88.16 |
| Unemployment rate | 3.76 |
| Median home value | 111300 |
| Gini index | 0.5105 |
| Vacancy rate | 28.78 |
| White | 4293 |
| Black | 3075 |
| Asian | 76 |
| Native | 45 |
| Hispanic/Latino | 88 |
| Bachelor's or higher | 876 |

## Districts

- [GA-08](/us/states/ga/districts/08.md) — 100% (congressional)
- [GA Senate District 26](/us/states/ga/districts/senate/26.md) — 100% (state senate)
- [GA House District 133](/us/states/ga/districts/house/133.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
