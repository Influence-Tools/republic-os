---
type: Jurisdiction
title: "Greene County, PA"
classification: county
fips: "42059"
state: "PA"
demographics:
  population: 34835
  population_under_18: 6591
  population_18_64: 21051
  population_65_plus: 7193
  median_household_income: 68041
  poverty_rate: 13.52
  homeownership_rate: 77.14
  unemployment_rate: 5.63
  median_home_value: 153900
  gini_index: 0.4315
  vacancy_rate: 11.59
  race_white: 31901
  race_black: 967
  race_asian: 75
  race_native: 23
  hispanic: 556
  bachelors_plus: 7504
districts:
  - to: "us/states/pa/districts/14"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/pa/districts/senate/46"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/pa/districts/house/50"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Greene County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 34835 |
| Under 18 | 6591 |
| 18–64 | 21051 |
| 65+ | 7193 |
| Median household income | 68041 |
| Poverty rate | 13.52 |
| Homeownership rate | 77.14 |
| Unemployment rate | 5.63 |
| Median home value | 153900 |
| Gini index | 0.4315 |
| Vacancy rate | 11.59 |
| White | 31901 |
| Black | 967 |
| Asian | 75 |
| Native | 23 |
| Hispanic/Latino | 556 |
| Bachelor's or higher | 7504 |

## Districts

- [PA-14](/us/states/pa/districts/14.md) — 100% (congressional)
- [PA Senate District 46](/us/states/pa/districts/senate/46.md) — 100% (state senate)
- [PA House District 50](/us/states/pa/districts/house/50.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
