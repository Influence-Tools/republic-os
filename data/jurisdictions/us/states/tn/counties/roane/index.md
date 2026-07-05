---
type: Jurisdiction
title: "Roane County, TN"
classification: county
fips: "47145"
state: "TN"
demographics:
  population: 55208
  population_under_18: 10341
  population_18_64: 32003
  population_65_plus: 12864
  median_household_income: 71885
  poverty_rate: 11.97
  homeownership_rate: 78.11
  unemployment_rate: 4.9
  median_home_value: 232900
  gini_index: 0.4564
  vacancy_rate: 11.25
  race_white: 50301
  race_black: 1409
  race_asian: 359
  race_native: 153
  hispanic: 1357
  bachelors_plus: 12811
districts:
  - to: "us/states/tn/districts/03"
    rel: in-district
    area_weight: 0.9917
  - to: "us/states/tn/districts/senate/12"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tn/districts/house/32"
    rel: in-district
    area_weight: 0.9551
  - to: "us/states/tn/districts/house/41"
    rel: in-district
    area_weight: 0.0447
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Roane County, TN

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 55208 |
| Under 18 | 10341 |
| 18–64 | 32003 |
| 65+ | 12864 |
| Median household income | 71885 |
| Poverty rate | 11.97 |
| Homeownership rate | 78.11 |
| Unemployment rate | 4.9 |
| Median home value | 232900 |
| Gini index | 0.4564 |
| Vacancy rate | 11.25 |
| White | 50301 |
| Black | 1409 |
| Asian | 359 |
| Native | 153 |
| Hispanic/Latino | 1357 |
| Bachelor's or higher | 12811 |

## Districts

- [TN-03](/us/states/tn/districts/03.md) — 99% (congressional)
- [TN Senate District 12](/us/states/tn/districts/senate/12.md) — 100% (state senate)
- [TN House District 32](/us/states/tn/districts/house/32.md) — 96% (state house)
- [TN House District 41](/us/states/tn/districts/house/41.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
