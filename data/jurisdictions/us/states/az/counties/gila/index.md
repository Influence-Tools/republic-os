---
type: Jurisdiction
title: "Gila County, AZ"
classification: county
fips: "04007"
state: "AZ"
demographics:
  population: 53795
  population_under_18: 10929
  population_18_64: 12953
  population_65_plus: 29913
  median_household_income: 61986
  poverty_rate: 16.89
  homeownership_rate: 77.52
  unemployment_rate: 7.05
  median_home_value: 269400
  gini_index: 0.4507
  vacancy_rate: 27.78
  race_white: 35199
  race_black: 289
  race_asian: 415
  race_native: 5279
  hispanic: 9659
  bachelors_plus: 10392
districts:
  - to: "us/states/az/districts/02"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/az/districts/senate/7"
    rel: in-district
    area_weight: 0.616
  - to: "us/states/az/districts/senate/6"
    rel: in-district
    area_weight: 0.3839
  - to: "us/states/az/districts/house/7"
    rel: in-district
    area_weight: 0.616
  - to: "us/states/az/districts/house/6"
    rel: in-district
    area_weight: 0.3839
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, az]
timestamp: "2026-07-03"
---

# Gila County, AZ

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 53795 |
| Under 18 | 10929 |
| 18–64 | 12953 |
| 65+ | 29913 |
| Median household income | 61986 |
| Poverty rate | 16.89 |
| Homeownership rate | 77.52 |
| Unemployment rate | 7.05 |
| Median home value | 269400 |
| Gini index | 0.4507 |
| Vacancy rate | 27.78 |
| White | 35199 |
| Black | 289 |
| Asian | 415 |
| Native | 5279 |
| Hispanic/Latino | 9659 |
| Bachelor's or higher | 10392 |

## Districts

- [AZ-02](/us/states/az/districts/02.md) — 100% (congressional)
- [AZ Senate District 7](/us/states/az/districts/senate/7.md) — 62% (state senate)
- [AZ Senate District 6](/us/states/az/districts/senate/6.md) — 38% (state senate)
- [AZ House District 7](/us/states/az/districts/house/7.md) — 62% (state house)
- [AZ House District 6](/us/states/az/districts/house/6.md) — 38% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
