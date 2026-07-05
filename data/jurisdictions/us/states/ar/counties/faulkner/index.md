---
type: Jurisdiction
title: "Faulkner County, AR"
classification: county
fips: "05045"
state: "AR"
demographics:
  population: 127717
  population_under_18: 28894
  population_18_64: 81278
  population_65_plus: 17545
  median_household_income: 67289
  poverty_rate: 14.51
  homeownership_rate: 62.3
  unemployment_rate: 3.39
  median_home_value: 232700
  gini_index: 0.4516
  vacancy_rate: 8.09
  race_white: 100664
  race_black: 15079
  race_asian: 1268
  race_native: 250
  hispanic: 7303
  bachelors_plus: 39045
districts:
  - to: "us/states/ar/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ar/districts/senate/24"
    rel: in-district
    area_weight: 0.6783
  - to: "us/states/ar/districts/senate/17"
    rel: in-district
    area_weight: 0.2277
  - to: "us/states/ar/districts/senate/18"
    rel: in-district
    area_weight: 0.0937
  - to: "us/states/ar/districts/house/42"
    rel: in-district
    area_weight: 0.3876
  - to: "us/states/ar/districts/house/57"
    rel: in-district
    area_weight: 0.2753
  - to: "us/states/ar/districts/house/69"
    rel: in-district
    area_weight: 0.1423
  - to: "us/states/ar/districts/house/54"
    rel: in-district
    area_weight: 0.1034
  - to: "us/states/ar/districts/house/56"
    rel: in-district
    area_weight: 0.0677
  - to: "us/states/ar/districts/house/55"
    rel: in-district
    area_weight: 0.0236
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Faulkner County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 127717 |
| Under 18 | 28894 |
| 18–64 | 81278 |
| 65+ | 17545 |
| Median household income | 67289 |
| Poverty rate | 14.51 |
| Homeownership rate | 62.3 |
| Unemployment rate | 3.39 |
| Median home value | 232700 |
| Gini index | 0.4516 |
| Vacancy rate | 8.09 |
| White | 100664 |
| Black | 15079 |
| Asian | 1268 |
| Native | 250 |
| Hispanic/Latino | 7303 |
| Bachelor's or higher | 39045 |

## Districts

- [AR-02](/us/states/ar/districts/02.md) — 100% (congressional)
- [AR Senate District 24](/us/states/ar/districts/senate/24.md) — 68% (state senate)
- [AR Senate District 17](/us/states/ar/districts/senate/17.md) — 23% (state senate)
- [AR Senate District 18](/us/states/ar/districts/senate/18.md) — 9% (state senate)
- [AR House District 42](/us/states/ar/districts/house/42.md) — 39% (state house)
- [AR House District 57](/us/states/ar/districts/house/57.md) — 28% (state house)
- [AR House District 69](/us/states/ar/districts/house/69.md) — 14% (state house)
- [AR House District 54](/us/states/ar/districts/house/54.md) — 10% (state house)
- [AR House District 56](/us/states/ar/districts/house/56.md) — 7% (state house)
- [AR House District 55](/us/states/ar/districts/house/55.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
