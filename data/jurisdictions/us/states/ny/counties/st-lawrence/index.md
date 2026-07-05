---
type: Jurisdiction
title: "St. Lawrence County, NY"
classification: county
fips: "36089"
state: "NY"
demographics:
  population: 107226
  population_under_18: 21313
  population_18_64: 65761
  population_65_plus: 20152
  median_household_income: 62850
  poverty_rate: 16.86
  homeownership_rate: 71.87
  unemployment_rate: 5.26
  median_home_value: 121900
  gini_index: 0.4604
  vacancy_rate: 19.83
  race_white: 98372
  race_black: 2172
  race_asian: 1185
  race_native: 541
  hispanic: 2727
  bachelors_plus: 26767
districts:
  - to: "us/states/ny/districts/21"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ny/districts/senate/45"
    rel: in-district
    area_weight: 0.6076
  - to: "us/states/ny/districts/senate/49"
    rel: in-district
    area_weight: 0.3923
  - to: "us/states/ny/districts/house/117"
    rel: in-district
    area_weight: 0.6732
  - to: "us/states/ny/districts/house/116"
    rel: in-district
    area_weight: 0.3265
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# St. Lawrence County, NY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 107226 |
| Under 18 | 21313 |
| 18–64 | 65761 |
| 65+ | 20152 |
| Median household income | 62850 |
| Poverty rate | 16.86 |
| Homeownership rate | 71.87 |
| Unemployment rate | 5.26 |
| Median home value | 121900 |
| Gini index | 0.4604 |
| Vacancy rate | 19.83 |
| White | 98372 |
| Black | 2172 |
| Asian | 1185 |
| Native | 541 |
| Hispanic/Latino | 2727 |
| Bachelor's or higher | 26767 |

## Districts

- [NY-21](/us/states/ny/districts/21.md) — 100% (congressional)
- [NY Senate District 45](/us/states/ny/districts/senate/45.md) — 61% (state senate)
- [NY Senate District 49](/us/states/ny/districts/senate/49.md) — 39% (state senate)
- [NY House District 117](/us/states/ny/districts/house/117.md) — 67% (state house)
- [NY House District 116](/us/states/ny/districts/house/116.md) — 33% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
