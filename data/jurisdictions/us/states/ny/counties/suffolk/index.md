---
type: Jurisdiction
title: "Suffolk County, NY"
classification: county
fips: "36103"
state: "NY"
demographics:
  population: 1530146
  population_under_18: 317899
  population_18_64: 938209
  population_65_plus: 274038
  median_household_income: 130686
  poverty_rate: 6.42
  homeownership_rate: 82.16
  unemployment_rate: 4.73
  median_home_value: 578400
  gini_index: 0.4418
  vacancy_rate: 11.74
  race_white: 1007146
  race_black: 114943
  race_asian: 68632
  race_native: 6949
  hispanic: 348579
  bachelors_plus: 632462
districts:
  - to: "us/states/ny/districts/01"
    rel: in-district
    area_weight: 0.34
  - to: "us/states/ny/districts/02"
    rel: in-district
    area_weight: 0.1378
  - to: "us/states/ny/districts/03"
    rel: in-district
    area_weight: 0.011
  - to: "us/states/ny/districts/senate/1"
    rel: in-district
    area_weight: 0.2314
  - to: "us/states/ny/districts/senate/3"
    rel: in-district
    area_weight: 0.1021
  - to: "us/states/ny/districts/senate/2"
    rel: in-district
    area_weight: 0.064
  - to: "us/states/ny/districts/senate/8"
    rel: in-district
    area_weight: 0.0569
  - to: "us/states/ny/districts/senate/4"
    rel: in-district
    area_weight: 0.0296
  - to: "us/states/ny/districts/house/1"
    rel: in-district
    area_weight: 0.1679
  - to: "us/states/ny/districts/house/2"
    rel: in-district
    area_weight: 0.0715
  - to: "us/states/ny/districts/house/7"
    rel: in-district
    area_weight: 0.0576
  - to: "us/states/ny/districts/house/3"
    rel: in-district
    area_weight: 0.0344
  - to: "us/states/ny/districts/house/8"
    rel: in-district
    area_weight: 0.0268
  - to: "us/states/ny/districts/house/12"
    rel: in-district
    area_weight: 0.0244
  - to: "us/states/ny/districts/house/4"
    rel: in-district
    area_weight: 0.0226
  - to: "us/states/ny/districts/house/10"
    rel: in-district
    area_weight: 0.0212
  - to: "us/states/ny/districts/house/9"
    rel: in-district
    area_weight: 0.0189
  - to: "us/states/ny/districts/house/5"
    rel: in-district
    area_weight: 0.0173
  - to: "us/states/ny/districts/house/11"
    rel: in-district
    area_weight: 0.0121
  - to: "us/states/ny/districts/house/6"
    rel: in-district
    area_weight: 0.0095
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Suffolk County, NY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1530146 |
| Under 18 | 317899 |
| 18–64 | 938209 |
| 65+ | 274038 |
| Median household income | 130686 |
| Poverty rate | 6.42 |
| Homeownership rate | 82.16 |
| Unemployment rate | 4.73 |
| Median home value | 578400 |
| Gini index | 0.4418 |
| Vacancy rate | 11.74 |
| White | 1007146 |
| Black | 114943 |
| Asian | 68632 |
| Native | 6949 |
| Hispanic/Latino | 348579 |
| Bachelor's or higher | 632462 |

## Districts

- [NY-01](/us/states/ny/districts/01.md) — 34% (congressional)
- [NY-02](/us/states/ny/districts/02.md) — 14% (congressional)
- [NY-03](/us/states/ny/districts/03.md) — 1% (congressional)
- [NY Senate District 1](/us/states/ny/districts/senate/1.md) — 23% (state senate)
- [NY Senate District 3](/us/states/ny/districts/senate/3.md) — 10% (state senate)
- [NY Senate District 2](/us/states/ny/districts/senate/2.md) — 6% (state senate)
- [NY Senate District 8](/us/states/ny/districts/senate/8.md) — 6% (state senate)
- [NY Senate District 4](/us/states/ny/districts/senate/4.md) — 3% (state senate)
- [NY House District 1](/us/states/ny/districts/house/1.md) — 17% (state house)
- [NY House District 2](/us/states/ny/districts/house/2.md) — 7% (state house)
- [NY House District 7](/us/states/ny/districts/house/7.md) — 6% (state house)
- [NY House District 3](/us/states/ny/districts/house/3.md) — 3% (state house)
- [NY House District 8](/us/states/ny/districts/house/8.md) — 3% (state house)
- [NY House District 12](/us/states/ny/districts/house/12.md) — 2% (state house)
- [NY House District 4](/us/states/ny/districts/house/4.md) — 2% (state house)
- [NY House District 10](/us/states/ny/districts/house/10.md) — 2% (state house)
- [NY House District 9](/us/states/ny/districts/house/9.md) — 2% (state house)
- [NY House District 5](/us/states/ny/districts/house/5.md) — 2% (state house)
- [NY House District 11](/us/states/ny/districts/house/11.md) — 1% (state house)
- [NY House District 6](/us/states/ny/districts/house/6.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
