---
type: Jurisdiction
title: "Ulster County, NY"
classification: county
fips: "36111"
state: "NY"
demographics:
  population: 182601
  population_under_18: 31214
  population_18_64: 112544
  population_65_plus: 38843
  median_household_income: 86271
  poverty_rate: 14.64
  homeownership_rate: 69.9
  unemployment_rate: 5.41
  median_home_value: 352500
  gini_index: 0.48
  vacancy_rate: 14.13
  race_white: 136255
  race_black: 11342
  race_asian: 3913
  race_native: 751
  hispanic: 22264
  bachelors_plus: 75201
districts:
  - to: "us/states/ny/districts/19"
    rel: in-district
    area_weight: 0.6692
  - to: "us/states/ny/districts/18"
    rel: in-district
    area_weight: 0.3308
  - to: "us/states/ny/districts/senate/51"
    rel: in-district
    area_weight: 0.5435
  - to: "us/states/ny/districts/senate/41"
    rel: in-district
    area_weight: 0.4564
  - to: "us/states/ny/districts/house/101"
    rel: in-district
    area_weight: 0.5055
  - to: "us/states/ny/districts/house/103"
    rel: in-district
    area_weight: 0.4125
  - to: "us/states/ny/districts/house/104"
    rel: in-district
    area_weight: 0.082
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Ulster County, NY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 182601 |
| Under 18 | 31214 |
| 18–64 | 112544 |
| 65+ | 38843 |
| Median household income | 86271 |
| Poverty rate | 14.64 |
| Homeownership rate | 69.9 |
| Unemployment rate | 5.41 |
| Median home value | 352500 |
| Gini index | 0.48 |
| Vacancy rate | 14.13 |
| White | 136255 |
| Black | 11342 |
| Asian | 3913 |
| Native | 751 |
| Hispanic/Latino | 22264 |
| Bachelor's or higher | 75201 |

## Districts

- [NY-19](/us/states/ny/districts/19.md) — 67% (congressional)
- [NY-18](/us/states/ny/districts/18.md) — 33% (congressional)
- [NY Senate District 51](/us/states/ny/districts/senate/51.md) — 54% (state senate)
- [NY Senate District 41](/us/states/ny/districts/senate/41.md) — 46% (state senate)
- [NY House District 101](/us/states/ny/districts/house/101.md) — 51% (state house)
- [NY House District 103](/us/states/ny/districts/house/103.md) — 41% (state house)
- [NY House District 104](/us/states/ny/districts/house/104.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
