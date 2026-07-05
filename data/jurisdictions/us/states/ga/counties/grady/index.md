---
type: Jurisdiction
title: "Grady County, GA"
classification: county
fips: "13131"
state: "GA"
demographics:
  population: 26108
  population_under_18: 6432
  population_18_64: 14727
  population_65_plus: 4949
  median_household_income: 58980
  poverty_rate: 20.3
  homeownership_rate: 66.11
  unemployment_rate: 3.71
  median_home_value: 152400
  gini_index: 0.4615
  vacancy_rate: 13.2
  race_white: 15121
  race_black: 7545
  race_asian: 51
  race_native: 102
  hispanic: 3484
  bachelors_plus: 4110
districts:
  - to: "us/states/ga/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ga/districts/senate/11"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ga/districts/house/171"
    rel: in-district
    area_weight: 0.6006
  - to: "us/states/ga/districts/house/173"
    rel: in-district
    area_weight: 0.3993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Grady County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 26108 |
| Under 18 | 6432 |
| 18–64 | 14727 |
| 65+ | 4949 |
| Median household income | 58980 |
| Poverty rate | 20.3 |
| Homeownership rate | 66.11 |
| Unemployment rate | 3.71 |
| Median home value | 152400 |
| Gini index | 0.4615 |
| Vacancy rate | 13.2 |
| White | 15121 |
| Black | 7545 |
| Asian | 51 |
| Native | 102 |
| Hispanic/Latino | 3484 |
| Bachelor's or higher | 4110 |

## Districts

- [GA-02](/us/states/ga/districts/02.md) — 100% (congressional)
- [GA Senate District 11](/us/states/ga/districts/senate/11.md) — 100% (state senate)
- [GA House District 171](/us/states/ga/districts/house/171.md) — 60% (state house)
- [GA House District 173](/us/states/ga/districts/house/173.md) — 40% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
