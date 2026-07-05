---
type: Jurisdiction
title: "Chattooga County, GA"
classification: county
fips: "13055"
state: "GA"
demographics:
  population: 25036
  population_under_18: 5501
  population_18_64: 14859
  population_65_plus: 4676
  median_household_income: 50285
  poverty_rate: 21.2
  homeownership_rate: 66.79
  unemployment_rate: 5.39
  median_home_value: 115600
  gini_index: 0.4305
  vacancy_rate: 15.88
  race_white: 20464
  race_black: 2241
  race_asian: 95
  race_native: 423
  hispanic: 1436
  bachelors_plus: 3047
districts:
  - to: "us/states/ga/districts/14"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ga/districts/senate/53"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ga/districts/house/12"
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

# Chattooga County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25036 |
| Under 18 | 5501 |
| 18–64 | 14859 |
| 65+ | 4676 |
| Median household income | 50285 |
| Poverty rate | 21.2 |
| Homeownership rate | 66.79 |
| Unemployment rate | 5.39 |
| Median home value | 115600 |
| Gini index | 0.4305 |
| Vacancy rate | 15.88 |
| White | 20464 |
| Black | 2241 |
| Asian | 95 |
| Native | 423 |
| Hispanic/Latino | 1436 |
| Bachelor's or higher | 3047 |

## Districts

- [GA-14](/us/states/ga/districts/14.md) — 100% (congressional)
- [GA Senate District 53](/us/states/ga/districts/senate/53.md) — 100% (state senate)
- [GA House District 12](/us/states/ga/districts/house/12.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
