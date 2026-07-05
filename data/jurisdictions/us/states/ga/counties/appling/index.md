---
type: Jurisdiction
title: "Appling County, GA"
classification: county
fips: "13001"
state: "GA"
demographics:
  population: 18493
  population_under_18: 4505
  population_18_64: 10557
  population_65_plus: 3431
  median_household_income: 46651
  poverty_rate: 22.48
  homeownership_rate: 72.51
  unemployment_rate: 3.14
  median_home_value: 76700
  gini_index: 0.4536
  vacancy_rate: 16.19
  race_white: 12668
  race_black: 3351
  race_asian: 73
  race_native: 56
  hispanic: 1992
  bachelors_plus: 2060
districts:
  - to: "us/states/ga/districts/01"
    rel: in-district
    area_weight: 0.9964
  - to: "us/states/ga/districts/senate/19"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/house/157"
    rel: in-district
    area_weight: 0.6221
  - to: "us/states/ga/districts/house/178"
    rel: in-district
    area_weight: 0.3778
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Appling County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18493 |
| Under 18 | 4505 |
| 18–64 | 10557 |
| 65+ | 3431 |
| Median household income | 46651 |
| Poverty rate | 22.48 |
| Homeownership rate | 72.51 |
| Unemployment rate | 3.14 |
| Median home value | 76700 |
| Gini index | 0.4536 |
| Vacancy rate | 16.19 |
| White | 12668 |
| Black | 3351 |
| Asian | 73 |
| Native | 56 |
| Hispanic/Latino | 1992 |
| Bachelor's or higher | 2060 |

## Districts

- [GA-01](/us/states/ga/districts/01.md) — 100% (congressional)
- [GA Senate District 19](/us/states/ga/districts/senate/19.md) — 100% (state senate)
- [GA House District 157](/us/states/ga/districts/house/157.md) — 62% (state house)
- [GA House District 178](/us/states/ga/districts/house/178.md) — 38% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
