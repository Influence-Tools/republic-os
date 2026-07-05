---
type: Jurisdiction
title: "Snyder County, PA"
classification: county
fips: "42109"
state: "PA"
demographics:
  population: 39668
  population_under_18: 8114
  population_18_64: 23394
  population_65_plus: 8160
  median_household_income: 66876
  poverty_rate: 9.44
  homeownership_rate: 75.58
  unemployment_rate: 2.43
  median_home_value: 215300
  gini_index: 0.4131
  vacancy_rate: 9.05
  race_white: 37487
  race_black: 259
  race_asian: 258
  race_native: 6
  hispanic: 1035
  bachelors_plus: 7623
districts:
  - to: "us/states/pa/districts/15"
    rel: in-district
    area_weight: 0.9953
  - to: "us/states/pa/districts/senate/27"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/pa/districts/house/85"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Snyder County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 39668 |
| Under 18 | 8114 |
| 18–64 | 23394 |
| 65+ | 8160 |
| Median household income | 66876 |
| Poverty rate | 9.44 |
| Homeownership rate | 75.58 |
| Unemployment rate | 2.43 |
| Median home value | 215300 |
| Gini index | 0.4131 |
| Vacancy rate | 9.05 |
| White | 37487 |
| Black | 259 |
| Asian | 258 |
| Native | 6 |
| Hispanic/Latino | 1035 |
| Bachelor's or higher | 7623 |

## Districts

- [PA-15](/us/states/pa/districts/15.md) — 100% (congressional)
- [PA Senate District 27](/us/states/pa/districts/senate/27.md) — 100% (state senate)
- [PA House District 85](/us/states/pa/districts/house/85.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
