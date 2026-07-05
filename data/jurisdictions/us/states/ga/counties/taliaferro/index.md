---
type: Jurisdiction
title: "Taliaferro County, GA"
classification: county
fips: "13265"
state: "GA"
demographics:
  population: 1558
  population_under_18: 291
  population_18_64: 808
  population_65_plus: 459
  median_household_income: 52500
  poverty_rate: 20.36
  homeownership_rate: 82.14
  unemployment_rate: 4.95
  median_home_value: 68900
  gini_index: 0.4069
  vacancy_rate: 36.57
  race_white: 658
  race_black: 715
  race_asian: 1
  race_native: 0
  hispanic: 68
  bachelors_plus: 199
districts:
  - to: "us/states/ga/districts/10"
    rel: in-district
    area_weight: 0.9913
  - to: "us/states/ga/districts/12"
    rel: in-district
    area_weight: 0.0087
  - to: "us/states/ga/districts/senate/23"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/ga/districts/house/124"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Taliaferro County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1558 |
| Under 18 | 291 |
| 18–64 | 808 |
| 65+ | 459 |
| Median household income | 52500 |
| Poverty rate | 20.36 |
| Homeownership rate | 82.14 |
| Unemployment rate | 4.95 |
| Median home value | 68900 |
| Gini index | 0.4069 |
| Vacancy rate | 36.57 |
| White | 658 |
| Black | 715 |
| Asian | 1 |
| Native | 0 |
| Hispanic/Latino | 68 |
| Bachelor's or higher | 199 |

## Districts

- [GA-10](/us/states/ga/districts/10.md) — 99% (congressional)
- [GA-12](/us/states/ga/districts/12.md) — 1% (congressional)
- [GA Senate District 23](/us/states/ga/districts/senate/23.md) — 100% (state senate)
- [GA House District 124](/us/states/ga/districts/house/124.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
