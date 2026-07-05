---
type: Jurisdiction
title: "Toombs County, GA"
classification: county
fips: "13279"
state: "GA"
demographics:
  population: 27102
  population_under_18: 7122
  population_18_64: 15350
  population_65_plus: 4630
  median_household_income: 52621
  poverty_rate: 22.49
  homeownership_rate: 60.51
  unemployment_rate: 4.39
  median_home_value: 137000
  gini_index: 0.4518
  vacancy_rate: 14.0
  race_white: 16853
  race_black: 6404
  race_asian: 230
  race_native: 92
  hispanic: 3271
  bachelors_plus: 4450
districts:
  - to: "us/states/ga/districts/12"
    rel: in-district
    area_weight: 0.9973
  - to: "us/states/ga/districts/senate/19"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ga/districts/house/156"
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

# Toombs County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 27102 |
| Under 18 | 7122 |
| 18–64 | 15350 |
| 65+ | 4630 |
| Median household income | 52621 |
| Poverty rate | 22.49 |
| Homeownership rate | 60.51 |
| Unemployment rate | 4.39 |
| Median home value | 137000 |
| Gini index | 0.4518 |
| Vacancy rate | 14.0 |
| White | 16853 |
| Black | 6404 |
| Asian | 230 |
| Native | 92 |
| Hispanic/Latino | 3271 |
| Bachelor's or higher | 4450 |

## Districts

- [GA-12](/us/states/ga/districts/12.md) — 100% (congressional)
- [GA Senate District 19](/us/states/ga/districts/senate/19.md) — 100% (state senate)
- [GA House District 156](/us/states/ga/districts/house/156.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
