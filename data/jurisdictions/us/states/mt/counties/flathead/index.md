---
type: Jurisdiction
title: "Flathead County, MT"
classification: county
fips: "30029"
state: "MT"
demographics:
  population: 110695
  population_under_18: 23948
  population_18_64: 63395
  population_65_plus: 23352
  median_household_income: 73925
  poverty_rate: 9.32
  homeownership_rate: 72.36
  unemployment_rate: 2.93
  median_home_value: 535500
  gini_index: 0.4566
  vacancy_rate: 14.41
  race_white: 100831
  race_black: 236
  race_asian: 931
  race_native: 976
  hispanic: 4076
  bachelors_plus: 39876
districts:
  - to: "us/states/mt/districts/01"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mt/districts/senate/2"
    rel: in-district
    area_weight: 0.4298
  - to: "us/states/mt/districts/senate/8"
    rel: in-district
    area_weight: 0.2421
  - to: "us/states/mt/districts/senate/1"
    rel: in-district
    area_weight: 0.1025
  - to: "us/states/mt/districts/senate/3"
    rel: in-district
    area_weight: 0.086
  - to: "us/states/mt/districts/senate/6"
    rel: in-district
    area_weight: 0.0766
  - to: "us/states/mt/districts/senate/5"
    rel: in-district
    area_weight: 0.0602
  - to: "us/states/mt/districts/house/3"
    rel: in-district
    area_weight: 0.4268
  - to: "us/states/mt/districts/house/15"
    rel: in-district
    area_weight: 0.2421
  - to: "us/states/mt/districts/house/2"
    rel: in-district
    area_weight: 0.1025
  - to: "us/states/mt/districts/house/11"
    rel: in-district
    area_weight: 0.0666
  - to: "us/states/mt/districts/house/6"
    rel: in-district
    area_weight: 0.0491
  - to: "us/states/mt/districts/house/9"
    rel: in-district
    area_weight: 0.0491
  - to: "us/states/mt/districts/house/5"
    rel: in-district
    area_weight: 0.0369
  - to: "us/states/mt/districts/house/10"
    rel: in-district
    area_weight: 0.011
  - to: "us/states/mt/districts/house/12"
    rel: in-district
    area_weight: 0.01
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Flathead County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 110695 |
| Under 18 | 23948 |
| 18–64 | 63395 |
| 65+ | 23352 |
| Median household income | 73925 |
| Poverty rate | 9.32 |
| Homeownership rate | 72.36 |
| Unemployment rate | 2.93 |
| Median home value | 535500 |
| Gini index | 0.4566 |
| Vacancy rate | 14.41 |
| White | 100831 |
| Black | 236 |
| Asian | 931 |
| Native | 976 |
| Hispanic/Latino | 4076 |
| Bachelor's or higher | 39876 |

## Districts

- [MT-01](/us/states/mt/districts/01.md) — 100% (congressional)
- [MT Senate District 2](/us/states/mt/districts/senate/2.md) — 43% (state senate)
- [MT Senate District 8](/us/states/mt/districts/senate/8.md) — 24% (state senate)
- [MT Senate District 1](/us/states/mt/districts/senate/1.md) — 10% (state senate)
- [MT Senate District 3](/us/states/mt/districts/senate/3.md) — 9% (state senate)
- [MT Senate District 6](/us/states/mt/districts/senate/6.md) — 8% (state senate)
- [MT Senate District 5](/us/states/mt/districts/senate/5.md) — 6% (state senate)
- [MT House District 3](/us/states/mt/districts/house/3.md) — 43% (state house)
- [MT House District 15](/us/states/mt/districts/house/15.md) — 24% (state house)
- [MT House District 2](/us/states/mt/districts/house/2.md) — 10% (state house)
- [MT House District 11](/us/states/mt/districts/house/11.md) — 7% (state house)
- [MT House District 6](/us/states/mt/districts/house/6.md) — 5% (state house)
- [MT House District 9](/us/states/mt/districts/house/9.md) — 5% (state house)
- [MT House District 5](/us/states/mt/districts/house/5.md) — 4% (state house)
- [MT House District 10](/us/states/mt/districts/house/10.md) — 1% (state house)
- [MT House District 12](/us/states/mt/districts/house/12.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
