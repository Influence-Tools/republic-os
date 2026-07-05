---
type: Jurisdiction
title: "Lake County, MT"
classification: county
fips: "30047"
state: "MT"
demographics:
  population: 32561
  population_under_18: 7167
  population_18_64: 17500
  population_65_plus: 7894
  median_household_income: 63360
  poverty_rate: 17.24
  homeownership_rate: 75.05
  unemployment_rate: 5.74
  median_home_value: 421800
  gini_index: 0.5019
  vacancy_rate: 23.63
  race_white: 21367
  race_black: 71
  race_asian: 218
  race_native: 6608
  hispanic: 1397
  bachelors_plus: 9822
districts:
  - to: "us/states/mt/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mt/districts/senate/8"
    rel: in-district
    area_weight: 0.3086
  - to: "us/states/mt/districts/senate/6"
    rel: in-district
    area_weight: 0.2859
  - to: "us/states/mt/districts/senate/7"
    rel: in-district
    area_weight: 0.2072
  - to: "us/states/mt/districts/senate/46"
    rel: in-district
    area_weight: 0.1983
  - to: "us/states/mt/districts/house/15"
    rel: in-district
    area_weight: 0.3086
  - to: "us/states/mt/districts/house/12"
    rel: in-district
    area_weight: 0.2859
  - to: "us/states/mt/districts/house/13"
    rel: in-district
    area_weight: 0.2072
  - to: "us/states/mt/districts/house/91"
    rel: in-district
    area_weight: 0.1983
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Lake County, MT

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 32561 |
| Under 18 | 7167 |
| 18–64 | 17500 |
| 65+ | 7894 |
| Median household income | 63360 |
| Poverty rate | 17.24 |
| Homeownership rate | 75.05 |
| Unemployment rate | 5.74 |
| Median home value | 421800 |
| Gini index | 0.5019 |
| Vacancy rate | 23.63 |
| White | 21367 |
| Black | 71 |
| Asian | 218 |
| Native | 6608 |
| Hispanic/Latino | 1397 |
| Bachelor's or higher | 9822 |

## Districts

- [MT-01](/us/states/mt/districts/01.md) — 100% (congressional)
- [MT Senate District 8](/us/states/mt/districts/senate/8.md) — 31% (state senate)
- [MT Senate District 6](/us/states/mt/districts/senate/6.md) — 29% (state senate)
- [MT Senate District 7](/us/states/mt/districts/senate/7.md) — 21% (state senate)
- [MT Senate District 46](/us/states/mt/districts/senate/46.md) — 20% (state senate)
- [MT House District 15](/us/states/mt/districts/house/15.md) — 31% (state house)
- [MT House District 12](/us/states/mt/districts/house/12.md) — 29% (state house)
- [MT House District 13](/us/states/mt/districts/house/13.md) — 21% (state house)
- [MT House District 91](/us/states/mt/districts/house/91.md) — 20% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
