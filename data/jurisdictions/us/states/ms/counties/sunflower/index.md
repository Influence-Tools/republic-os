---
type: Jurisdiction
title: "Sunflower County, MS"
classification: county
fips: "28133"
state: "MS"
demographics:
  population: 24333
  population_under_18: 5196
  population_18_64: 15391
  population_65_plus: 3746
  median_household_income: 39956
  poverty_rate: 28.87
  homeownership_rate: 54.94
  unemployment_rate: 11.23
  median_home_value: 100300
  gini_index: 0.5035
  vacancy_rate: 14.74
  race_white: 5627
  race_black: 17693
  race_asian: 48
  race_native: 33
  hispanic: 692
  bachelors_plus: 3741
districts:
  - to: "us/states/ms/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ms/districts/senate/13"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ms/districts/house/31"
    rel: in-district
    area_weight: 0.7544
  - to: "us/states/ms/districts/house/30"
    rel: in-district
    area_weight: 0.1133
  - to: "us/states/ms/districts/house/26"
    rel: in-district
    area_weight: 0.1072
  - to: "us/states/ms/districts/house/29"
    rel: in-district
    area_weight: 0.025
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Sunflower County, MS

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 24333 |
| Under 18 | 5196 |
| 18–64 | 15391 |
| 65+ | 3746 |
| Median household income | 39956 |
| Poverty rate | 28.87 |
| Homeownership rate | 54.94 |
| Unemployment rate | 11.23 |
| Median home value | 100300 |
| Gini index | 0.5035 |
| Vacancy rate | 14.74 |
| White | 5627 |
| Black | 17693 |
| Asian | 48 |
| Native | 33 |
| Hispanic/Latino | 692 |
| Bachelor's or higher | 3741 |

## Districts

- [MS-02](/us/states/ms/districts/02.md) — 100% (congressional)
- [MS Senate District 13](/us/states/ms/districts/senate/13.md) — 100% (state senate)
- [MS House District 31](/us/states/ms/districts/house/31.md) — 75% (state house)
- [MS House District 30](/us/states/ms/districts/house/30.md) — 11% (state house)
- [MS House District 26](/us/states/ms/districts/house/26.md) — 11% (state house)
- [MS House District 29](/us/states/ms/districts/house/29.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
