---
type: Jurisdiction
title: "Beaver County, PA"
classification: county
fips: "42007"
state: "PA"
demographics:
  population: 166324
  population_under_18: 32226
  population_18_64: 96473
  population_65_plus: 37625
  median_household_income: 71089
  poverty_rate: 9.9
  homeownership_rate: 75.04
  unemployment_rate: 5.26
  median_home_value: 190900
  gini_index: 0.4316
  vacancy_rate: 8.91
  race_white: 144595
  race_black: 10367
  race_asian: 795
  race_native: 143
  hispanic: 3968
  bachelors_plus: 46077
districts:
  - to: "us/states/pa/districts/17"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/pa/districts/senate/47"
    rel: in-district
    area_weight: 0.8455
  - to: "us/states/pa/districts/senate/46"
    rel: in-district
    area_weight: 0.1544
  - to: "us/states/pa/districts/house/15"
    rel: in-district
    area_weight: 0.4806
  - to: "us/states/pa/districts/house/14"
    rel: in-district
    area_weight: 0.397
  - to: "us/states/pa/districts/house/16"
    rel: in-district
    area_weight: 0.1222
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Beaver County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 166324 |
| Under 18 | 32226 |
| 18–64 | 96473 |
| 65+ | 37625 |
| Median household income | 71089 |
| Poverty rate | 9.9 |
| Homeownership rate | 75.04 |
| Unemployment rate | 5.26 |
| Median home value | 190900 |
| Gini index | 0.4316 |
| Vacancy rate | 8.91 |
| White | 144595 |
| Black | 10367 |
| Asian | 795 |
| Native | 143 |
| Hispanic/Latino | 3968 |
| Bachelor's or higher | 46077 |

## Districts

- [PA-17](/us/states/pa/districts/17.md) — 100% (congressional)
- [PA Senate District 47](/us/states/pa/districts/senate/47.md) — 85% (state senate)
- [PA Senate District 46](/us/states/pa/districts/senate/46.md) — 15% (state senate)
- [PA House District 15](/us/states/pa/districts/house/15.md) — 48% (state house)
- [PA House District 14](/us/states/pa/districts/house/14.md) — 40% (state house)
- [PA House District 16](/us/states/pa/districts/house/16.md) — 12% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
