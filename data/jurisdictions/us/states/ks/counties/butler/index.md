---
type: Jurisdiction
title: "Butler County, KS"
classification: county
fips: "20015"
state: "KS"
demographics:
  population: 68287
  population_under_18: 16796
  population_18_64: 40400
  population_65_plus: 11091
  median_household_income: 81610
  poverty_rate: 8.55
  homeownership_rate: 77.56
  unemployment_rate: 3.4
  median_home_value: 217600
  gini_index: 0.4228
  vacancy_rate: 7.81
  race_white: 59618
  race_black: 1329
  race_asian: 1159
  race_native: 415
  hispanic: 3992
  bachelors_plus: 19831
districts:
  - to: "us/states/ks/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/senate/14"
    rel: in-district
    area_weight: 0.5937
  - to: "us/states/ks/districts/senate/32"
    rel: in-district
    area_weight: 0.2564
  - to: "us/states/ks/districts/senate/16"
    rel: in-district
    area_weight: 0.1499
  - to: "us/states/ks/districts/house/75"
    rel: in-district
    area_weight: 0.5215
  - to: "us/states/ks/districts/house/12"
    rel: in-district
    area_weight: 0.3415
  - to: "us/states/ks/districts/house/77"
    rel: in-district
    area_weight: 0.117
  - to: "us/states/ks/districts/house/99"
    rel: in-district
    area_weight: 0.0113
  - to: "us/states/ks/districts/house/85"
    rel: in-district
    area_weight: 0.0063
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Butler County, KS

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 68287 |
| Under 18 | 16796 |
| 18–64 | 40400 |
| 65+ | 11091 |
| Median household income | 81610 |
| Poverty rate | 8.55 |
| Homeownership rate | 77.56 |
| Unemployment rate | 3.4 |
| Median home value | 217600 |
| Gini index | 0.4228 |
| Vacancy rate | 7.81 |
| White | 59618 |
| Black | 1329 |
| Asian | 1159 |
| Native | 415 |
| Hispanic/Latino | 3992 |
| Bachelor's or higher | 19831 |

## Districts

- [KS-04](/us/states/ks/districts/04.md) — 100% (congressional)
- [KS Senate District 14](/us/states/ks/districts/senate/14.md) — 59% (state senate)
- [KS Senate District 32](/us/states/ks/districts/senate/32.md) — 26% (state senate)
- [KS Senate District 16](/us/states/ks/districts/senate/16.md) — 15% (state senate)
- [KS House District 75](/us/states/ks/districts/house/75.md) — 52% (state house)
- [KS House District 12](/us/states/ks/districts/house/12.md) — 34% (state house)
- [KS House District 77](/us/states/ks/districts/house/77.md) — 12% (state house)
- [KS House District 99](/us/states/ks/districts/house/99.md) — 1% (state house)
- [KS House District 85](/us/states/ks/districts/house/85.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
