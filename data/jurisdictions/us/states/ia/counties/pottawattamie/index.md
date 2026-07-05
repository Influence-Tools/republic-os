---
type: Jurisdiction
title: "Pottawattamie County, IA"
classification: county
fips: "19155"
state: "IA"
demographics:
  population: 93424
  population_under_18: 21407
  population_18_64: 54509
  population_65_plus: 17508
  median_household_income: 73602
  poverty_rate: 12.12
  homeownership_rate: 69.9
  unemployment_rate: 3.81
  median_home_value: 195700
  gini_index: 0.428
  vacancy_rate: 6.09
  race_white: 81761
  race_black: 1810
  race_asian: 829
  race_native: 253
  hispanic: 8536
  bachelors_plus: 20206
districts:
  - to: "us/states/ia/districts/04"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/ia/districts/senate/8"
    rel: in-district
    area_weight: 0.8784
  - to: "us/states/ia/districts/senate/6"
    rel: in-district
    area_weight: 0.0745
  - to: "us/states/ia/districts/senate/10"
    rel: in-district
    area_weight: 0.0464
  - to: "us/states/ia/districts/house/16"
    rel: in-district
    area_weight: 0.5919
  - to: "us/states/ia/districts/house/15"
    rel: in-district
    area_weight: 0.2865
  - to: "us/states/ia/districts/house/11"
    rel: in-district
    area_weight: 0.0745
  - to: "us/states/ia/districts/house/19"
    rel: in-district
    area_weight: 0.036
  - to: "us/states/ia/districts/house/20"
    rel: in-district
    area_weight: 0.0104
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Pottawattamie County, IA

County jurisdiction — 5 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 93424 |
| Under 18 | 21407 |
| 18–64 | 54509 |
| 65+ | 17508 |
| Median household income | 73602 |
| Poverty rate | 12.12 |
| Homeownership rate | 69.9 |
| Unemployment rate | 3.81 |
| Median home value | 195700 |
| Gini index | 0.428 |
| Vacancy rate | 6.09 |
| White | 81761 |
| Black | 1810 |
| Asian | 829 |
| Native | 253 |
| Hispanic/Latino | 8536 |
| Bachelor's or higher | 20206 |

## Districts

- [IA-04](/us/states/ia/districts/04.md) — 100% (congressional)
- [IA Senate District 8](/us/states/ia/districts/senate/8.md) — 88% (state senate)
- [IA Senate District 6](/us/states/ia/districts/senate/6.md) — 7% (state senate)
- [IA Senate District 10](/us/states/ia/districts/senate/10.md) — 5% (state senate)
- [IA House District 16](/us/states/ia/districts/house/16.md) — 59% (state house)
- [IA House District 15](/us/states/ia/districts/house/15.md) — 29% (state house)
- [IA House District 11](/us/states/ia/districts/house/11.md) — 7% (state house)
- [IA House District 19](/us/states/ia/districts/house/19.md) — 4% (state house)
- [IA House District 20](/us/states/ia/districts/house/20.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
