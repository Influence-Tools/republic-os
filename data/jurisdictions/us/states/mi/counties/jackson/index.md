---
type: Jurisdiction
title: "Jackson County, MI"
classification: county
fips: "26075"
state: "MI"
demographics:
  population: 160060
  population_under_18: 33464
  population_18_64: 96085
  population_65_plus: 30511
  median_household_income: 66073
  poverty_rate: 11.65
  homeownership_rate: 75.04
  unemployment_rate: 5.53
  median_home_value: 193700
  gini_index: 0.4453
  vacancy_rate: 9.74
  race_white: 133048
  race_black: 11836
  race_asian: 1239
  race_native: 495
  hispanic: 6542
  bachelors_plus: 35224
districts:
  - to: "us/states/mi/districts/05"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mi/districts/senate/14"
    rel: in-district
    area_weight: 0.7987
  - to: "us/states/mi/districts/senate/17"
    rel: in-district
    area_weight: 0.2013
  - to: "us/states/mi/districts/house/45"
    rel: in-district
    area_weight: 0.5511
  - to: "us/states/mi/districts/house/47"
    rel: in-district
    area_weight: 0.2078
  - to: "us/states/mi/districts/house/46"
    rel: in-district
    area_weight: 0.1724
  - to: "us/states/mi/districts/house/48"
    rel: in-district
    area_weight: 0.0686
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Jackson County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 160060 |
| Under 18 | 33464 |
| 18–64 | 96085 |
| 65+ | 30511 |
| Median household income | 66073 |
| Poverty rate | 11.65 |
| Homeownership rate | 75.04 |
| Unemployment rate | 5.53 |
| Median home value | 193700 |
| Gini index | 0.4453 |
| Vacancy rate | 9.74 |
| White | 133048 |
| Black | 11836 |
| Asian | 1239 |
| Native | 495 |
| Hispanic/Latino | 6542 |
| Bachelor's or higher | 35224 |

## Districts

- [MI-05](/us/states/mi/districts/05.md) — 100% (congressional)
- [MI Senate District 14](/us/states/mi/districts/senate/14.md) — 80% (state senate)
- [MI Senate District 17](/us/states/mi/districts/senate/17.md) — 20% (state senate)
- [MI House District 45](/us/states/mi/districts/house/45.md) — 55% (state house)
- [MI House District 47](/us/states/mi/districts/house/47.md) — 21% (state house)
- [MI House District 46](/us/states/mi/districts/house/46.md) — 17% (state house)
- [MI House District 48](/us/states/mi/districts/house/48.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
