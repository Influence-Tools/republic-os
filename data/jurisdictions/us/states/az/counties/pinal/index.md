---
type: Jurisdiction
title: "Pinal County, AZ"
classification: county
fips: "04021"
state: "AZ"
demographics:
  population: 469006
  population_under_18: 100909
  population_18_64: 267061
  population_65_plus: 101036
  median_household_income: 80266
  poverty_rate: 11.1
  homeownership_rate: 81.72
  unemployment_rate: 5.96
  median_home_value: 349000
  gini_index: 0.4197
  vacancy_rate: 12.31
  race_white: 290049
  race_black: 24954
  race_asian: 8256
  race_native: 20793
  hispanic: 139779
  bachelors_plus: 99437
districts:
  - to: "us/states/az/districts/02"
    rel: in-district
    area_weight: 0.5481
  - to: "us/states/az/districts/06"
    rel: in-district
    area_weight: 0.2522
  - to: "us/states/az/districts/07"
    rel: in-district
    area_weight: 0.1665
  - to: "us/states/az/districts/05"
    rel: in-district
    area_weight: 0.0331
  - to: "us/states/az/districts/senate/16"
    rel: in-district
    area_weight: 0.4526
  - to: "us/states/az/districts/senate/7"
    rel: in-district
    area_weight: 0.3626
  - to: "us/states/az/districts/senate/23"
    rel: in-district
    area_weight: 0.0775
  - to: "us/states/az/districts/senate/6"
    rel: in-district
    area_weight: 0.0395
  - to: "us/states/az/districts/senate/17"
    rel: in-district
    area_weight: 0.0389
  - to: "us/states/az/districts/senate/15"
    rel: in-district
    area_weight: 0.0283
  - to: "us/states/az/districts/house/16"
    rel: in-district
    area_weight: 0.4526
  - to: "us/states/az/districts/house/7"
    rel: in-district
    area_weight: 0.3626
  - to: "us/states/az/districts/house/23"
    rel: in-district
    area_weight: 0.0775
  - to: "us/states/az/districts/house/6"
    rel: in-district
    area_weight: 0.0395
  - to: "us/states/az/districts/house/17"
    rel: in-district
    area_weight: 0.0389
  - to: "us/states/az/districts/house/15"
    rel: in-district
    area_weight: 0.0283
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, az]
timestamp: "2026-07-03"
---

# Pinal County, AZ

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 469006 |
| Under 18 | 100909 |
| 18–64 | 267061 |
| 65+ | 101036 |
| Median household income | 80266 |
| Poverty rate | 11.1 |
| Homeownership rate | 81.72 |
| Unemployment rate | 5.96 |
| Median home value | 349000 |
| Gini index | 0.4197 |
| Vacancy rate | 12.31 |
| White | 290049 |
| Black | 24954 |
| Asian | 8256 |
| Native | 20793 |
| Hispanic/Latino | 139779 |
| Bachelor's or higher | 99437 |

## Districts

- [AZ-02](/us/states/az/districts/02.md) — 55% (congressional)
- [AZ-06](/us/states/az/districts/06.md) — 25% (congressional)
- [AZ-07](/us/states/az/districts/07.md) — 17% (congressional)
- [AZ-05](/us/states/az/districts/05.md) — 3% (congressional)
- [AZ Senate District 16](/us/states/az/districts/senate/16.md) — 45% (state senate)
- [AZ Senate District 7](/us/states/az/districts/senate/7.md) — 36% (state senate)
- [AZ Senate District 23](/us/states/az/districts/senate/23.md) — 8% (state senate)
- [AZ Senate District 6](/us/states/az/districts/senate/6.md) — 4% (state senate)
- [AZ Senate District 17](/us/states/az/districts/senate/17.md) — 4% (state senate)
- [AZ Senate District 15](/us/states/az/districts/senate/15.md) — 3% (state senate)
- [AZ House District 16](/us/states/az/districts/house/16.md) — 45% (state house)
- [AZ House District 7](/us/states/az/districts/house/7.md) — 36% (state house)
- [AZ House District 23](/us/states/az/districts/house/23.md) — 8% (state house)
- [AZ House District 6](/us/states/az/districts/house/6.md) — 4% (state house)
- [AZ House District 17](/us/states/az/districts/house/17.md) — 4% (state house)
- [AZ House District 15](/us/states/az/districts/house/15.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
