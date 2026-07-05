---
type: Jurisdiction
title: "Yazoo County, MS"
classification: county
fips: "28163"
state: "MS"
demographics:
  population: 24835
  population_under_18: 5684
  population_18_64: 15371
  population_65_plus: 3780
  median_household_income: 39295
  poverty_rate: 30.75
  homeownership_rate: 55.31
  unemployment_rate: 9.7
  median_home_value: 153800
  gini_index: 0.5097
  vacancy_rate: 16.39
  race_white: 9887
  race_black: 14288
  race_asian: 14
  race_native: 22
  hispanic: 1337
  bachelors_plus: 3390
districts:
  - to: "us/states/ms/districts/02"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ms/districts/senate/23"
    rel: in-district
    area_weight: 0.5406
  - to: "us/states/ms/districts/senate/22"
    rel: in-district
    area_weight: 0.4592
  - to: "us/states/ms/districts/house/54"
    rel: in-district
    area_weight: 0.5264
  - to: "us/states/ms/districts/house/47"
    rel: in-district
    area_weight: 0.2881
  - to: "us/states/ms/districts/house/51"
    rel: in-district
    area_weight: 0.1557
  - to: "us/states/ms/districts/house/57"
    rel: in-district
    area_weight: 0.0297
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Yazoo County, MS

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 24835 |
| Under 18 | 5684 |
| 18–64 | 15371 |
| 65+ | 3780 |
| Median household income | 39295 |
| Poverty rate | 30.75 |
| Homeownership rate | 55.31 |
| Unemployment rate | 9.7 |
| Median home value | 153800 |
| Gini index | 0.5097 |
| Vacancy rate | 16.39 |
| White | 9887 |
| Black | 14288 |
| Asian | 14 |
| Native | 22 |
| Hispanic/Latino | 1337 |
| Bachelor's or higher | 3390 |

## Districts

- [MS-02](/us/states/ms/districts/02.md) — 100% (congressional)
- [MS Senate District 23](/us/states/ms/districts/senate/23.md) — 54% (state senate)
- [MS Senate District 22](/us/states/ms/districts/senate/22.md) — 46% (state senate)
- [MS House District 54](/us/states/ms/districts/house/54.md) — 53% (state house)
- [MS House District 47](/us/states/ms/districts/house/47.md) — 29% (state house)
- [MS House District 51](/us/states/ms/districts/house/51.md) — 16% (state house)
- [MS House District 57](/us/states/ms/districts/house/57.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
