---
type: Jurisdiction
title: "Ouray County, CO"
classification: county
fips: "08091"
state: "CO"
demographics:
  population: 5087
  population_under_18: 639
  population_18_64: 2628
  population_65_plus: 1820
  median_household_income: 91020
  poverty_rate: 4.25
  homeownership_rate: 82.54
  unemployment_rate: 3.52
  median_home_value: 739800
  gini_index: 0.4011
  vacancy_rate: 25.72
  race_white: 4563
  race_black: 77
  race_asian: 25
  race_native: 0
  hispanic: 308
  bachelors_plus: 3291
districts:
  - to: "us/states/co/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/co/districts/senate/6"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/co/districts/house/58"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Ouray County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5087 |
| Under 18 | 639 |
| 18–64 | 2628 |
| 65+ | 1820 |
| Median household income | 91020 |
| Poverty rate | 4.25 |
| Homeownership rate | 82.54 |
| Unemployment rate | 3.52 |
| Median home value | 739800 |
| Gini index | 0.4011 |
| Vacancy rate | 25.72 |
| White | 4563 |
| Black | 77 |
| Asian | 25 |
| Native | 0 |
| Hispanic/Latino | 308 |
| Bachelor's or higher | 3291 |

## Districts

- [CO-03](/us/states/co/districts/03.md) — 100% (congressional)
- [CO Senate District 6](/us/states/co/districts/senate/6.md) — 100% (state senate)
- [CO House District 58](/us/states/co/districts/house/58.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
