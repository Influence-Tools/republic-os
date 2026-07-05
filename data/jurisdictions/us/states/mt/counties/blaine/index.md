---
type: Jurisdiction
title: "Blaine County, MT"
classification: county
fips: "30005"
state: "MT"
demographics:
  population: 6949
  population_under_18: 2016
  population_18_64: 3770
  population_65_plus: 1163
  median_household_income: 64813
  poverty_rate: 18.29
  homeownership_rate: 65.7
  unemployment_rate: 13.62
  median_home_value: 155500
  gini_index: 0.481
  vacancy_rate: 19.23
  race_white: 3069
  race_black: 29
  race_asian: 7
  race_native: 3351
  hispanic: 194
  bachelors_plus: 1351
districts:
  - to: "us/states/mt/districts/02"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mt/districts/senate/16"
    rel: in-district
    area_weight: 0.5818
  - to: "us/states/mt/districts/senate/14"
    rel: in-district
    area_weight: 0.4181
  - to: "us/states/mt/districts/house/32"
    rel: in-district
    area_weight: 0.5506
  - to: "us/states/mt/districts/house/28"
    rel: in-district
    area_weight: 0.4181
  - to: "us/states/mt/districts/house/31"
    rel: in-district
    area_weight: 0.0312
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Blaine County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6949 |
| Under 18 | 2016 |
| 18–64 | 3770 |
| 65+ | 1163 |
| Median household income | 64813 |
| Poverty rate | 18.29 |
| Homeownership rate | 65.7 |
| Unemployment rate | 13.62 |
| Median home value | 155500 |
| Gini index | 0.481 |
| Vacancy rate | 19.23 |
| White | 3069 |
| Black | 29 |
| Asian | 7 |
| Native | 3351 |
| Hispanic/Latino | 194 |
| Bachelor's or higher | 1351 |

## Districts

- [MT-02](/us/states/mt/districts/02.md) — 100% (congressional)
- [MT Senate District 16](/us/states/mt/districts/senate/16.md) — 58% (state senate)
- [MT Senate District 14](/us/states/mt/districts/senate/14.md) — 42% (state senate)
- [MT House District 32](/us/states/mt/districts/house/32.md) — 55% (state house)
- [MT House District 28](/us/states/mt/districts/house/28.md) — 42% (state house)
- [MT House District 31](/us/states/mt/districts/house/31.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
