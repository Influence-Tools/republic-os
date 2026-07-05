---
type: Jurisdiction
title: "Rockdale County, GA"
classification: county
fips: "13247"
state: "GA"
demographics:
  population: 95281
  population_under_18: 22585
  population_18_64: 57628
  population_65_plus: 15068
  median_household_income: 77247
  poverty_rate: 10.76
  homeownership_rate: 69.59
  unemployment_rate: 5.89
  median_home_value: 292900
  gini_index: 0.4286
  vacancy_rate: 4.93
  race_white: 24415
  race_black: 55413
  race_asian: 1502
  race_native: 437
  hispanic: 10369
  bachelors_plus: 29288
districts:
  - to: "us/states/ga/districts/13"
    rel: in-district
    area_weight: 0.9921
  - to: "us/states/ga/districts/senate/43"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/ga/districts/house/92"
    rel: in-district
    area_weight: 0.4419
  - to: "us/states/ga/districts/house/91"
    rel: in-district
    area_weight: 0.3273
  - to: "us/states/ga/districts/house/93"
    rel: in-district
    area_weight: 0.2302
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Rockdale County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 95281 |
| Under 18 | 22585 |
| 18–64 | 57628 |
| 65+ | 15068 |
| Median household income | 77247 |
| Poverty rate | 10.76 |
| Homeownership rate | 69.59 |
| Unemployment rate | 5.89 |
| Median home value | 292900 |
| Gini index | 0.4286 |
| Vacancy rate | 4.93 |
| White | 24415 |
| Black | 55413 |
| Asian | 1502 |
| Native | 437 |
| Hispanic/Latino | 10369 |
| Bachelor's or higher | 29288 |

## Districts

- [GA-13](/us/states/ga/districts/13.md) — 99% (congressional)
- [GA Senate District 43](/us/states/ga/districts/senate/43.md) — 100% (state senate)
- [GA House District 92](/us/states/ga/districts/house/92.md) — 44% (state house)
- [GA House District 91](/us/states/ga/districts/house/91.md) — 33% (state house)
- [GA House District 93](/us/states/ga/districts/house/93.md) — 23% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
