---
type: Jurisdiction
title: "Candler County, GA"
classification: county
fips: "13043"
state: "GA"
demographics:
  population: 11043
  population_under_18: 2734
  population_18_64: 6199
  population_65_plus: 2110
  median_household_income: 49581
  poverty_rate: 16.25
  homeownership_rate: 62.04
  unemployment_rate: 2.46
  median_home_value: 159200
  gini_index: 0.4417
  vacancy_rate: 10.98
  race_white: 6554
  race_black: 2538
  race_asian: 64
  race_native: 390
  hispanic: 1416
  bachelors_plus: 1721
districts:
  - to: "us/states/ga/districts/12"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/senate/4"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ga/districts/house/158"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Candler County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11043 |
| Under 18 | 2734 |
| 18–64 | 6199 |
| 65+ | 2110 |
| Median household income | 49581 |
| Poverty rate | 16.25 |
| Homeownership rate | 62.04 |
| Unemployment rate | 2.46 |
| Median home value | 159200 |
| Gini index | 0.4417 |
| Vacancy rate | 10.98 |
| White | 6554 |
| Black | 2538 |
| Asian | 64 |
| Native | 390 |
| Hispanic/Latino | 1416 |
| Bachelor's or higher | 1721 |

## Districts

- [GA-12](/us/states/ga/districts/12.md) — 100% (congressional)
- [GA Senate District 4](/us/states/ga/districts/senate/4.md) — 100% (state senate)
- [GA House District 158](/us/states/ga/districts/house/158.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
