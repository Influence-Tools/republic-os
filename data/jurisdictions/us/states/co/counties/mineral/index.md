---
type: Jurisdiction
title: "Mineral County, CO"
classification: county
fips: "08079"
state: "CO"
demographics:
  population: 729
  population_under_18: 86
  population_18_64: 405
  population_65_plus: 238
  median_household_income: 56250
  poverty_rate: 10.01
  homeownership_rate: 69.69
  unemployment_rate: 9.09
  median_home_value: 430500
  gini_index: 0.4888
  vacancy_rate: 67.26
  race_white: 662
  race_black: 0
  race_asian: 5
  race_native: 1
  hispanic: 46
  bachelors_plus: 424
districts:
  - to: "us/states/co/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/co/districts/senate/6"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/co/districts/house/62"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Mineral County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 729 |
| Under 18 | 86 |
| 18–64 | 405 |
| 65+ | 238 |
| Median household income | 56250 |
| Poverty rate | 10.01 |
| Homeownership rate | 69.69 |
| Unemployment rate | 9.09 |
| Median home value | 430500 |
| Gini index | 0.4888 |
| Vacancy rate | 67.26 |
| White | 662 |
| Black | 0 |
| Asian | 5 |
| Native | 1 |
| Hispanic/Latino | 46 |
| Bachelor's or higher | 424 |

## Districts

- [CO-03](/us/states/co/districts/03.md) — 100% (congressional)
- [CO Senate District 6](/us/states/co/districts/senate/6.md) — 100% (state senate)
- [CO House District 62](/us/states/co/districts/house/62.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
