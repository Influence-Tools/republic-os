---
type: Jurisdiction
title: "Jasper County, GA"
classification: county
fips: "13159"
state: "GA"
demographics:
  population: 15929
  population_under_18: 3719
  population_18_64: 9419
  population_65_plus: 2791
  median_household_income: 60134
  poverty_rate: 15.97
  homeownership_rate: 85.6
  unemployment_rate: 7.2
  median_home_value: 243400
  gini_index: 0.4667
  vacancy_rate: 9.24
  race_white: 11958
  race_black: 2691
  race_asian: 25
  race_native: 3
  hispanic: 799
  bachelors_plus: 2975
districts:
  - to: "us/states/ga/districts/10"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/ga/districts/senate/25"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ga/districts/house/144"
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

# Jasper County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15929 |
| Under 18 | 3719 |
| 18–64 | 9419 |
| 65+ | 2791 |
| Median household income | 60134 |
| Poverty rate | 15.97 |
| Homeownership rate | 85.6 |
| Unemployment rate | 7.2 |
| Median home value | 243400 |
| Gini index | 0.4667 |
| Vacancy rate | 9.24 |
| White | 11958 |
| Black | 2691 |
| Asian | 25 |
| Native | 3 |
| Hispanic/Latino | 799 |
| Bachelor's or higher | 2975 |

## Districts

- [GA-10](/us/states/ga/districts/10.md) — 100% (congressional)
- [GA Senate District 25](/us/states/ga/districts/senate/25.md) — 100% (state senate)
- [GA House District 144](/us/states/ga/districts/house/144.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
