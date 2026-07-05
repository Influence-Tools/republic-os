---
type: Jurisdiction
title: "Coahoma County, MS"
classification: county
fips: "28027"
state: "MS"
demographics:
  population: 20540
  population_under_18: 5541
  population_18_64: 11614
  population_65_plus: 3385
  median_household_income: 37461
  poverty_rate: 35.51
  homeownership_rate: 52.09
  unemployment_rate: 9.89
  median_home_value: 90300
  gini_index: 0.4958
  vacancy_rate: 17.52
  race_white: 3894
  race_black: 15292
  race_asian: 53
  race_native: 135
  hispanic: 636
  bachelors_plus: 3542
districts:
  - to: "us/states/ms/districts/02"
    rel: in-district
    area_weight: 0.9972
  - to: "us/states/ms/districts/senate/12"
    rel: in-district
    area_weight: 0.7499
  - to: "us/states/ms/districts/senate/11"
    rel: in-district
    area_weight: 0.2496
  - to: "us/states/ms/districts/house/26"
    rel: in-district
    area_weight: 0.7346
  - to: "us/states/ms/districts/house/9"
    rel: in-district
    area_weight: 0.2649
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Coahoma County, MS

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20540 |
| Under 18 | 5541 |
| 18–64 | 11614 |
| 65+ | 3385 |
| Median household income | 37461 |
| Poverty rate | 35.51 |
| Homeownership rate | 52.09 |
| Unemployment rate | 9.89 |
| Median home value | 90300 |
| Gini index | 0.4958 |
| Vacancy rate | 17.52 |
| White | 3894 |
| Black | 15292 |
| Asian | 53 |
| Native | 135 |
| Hispanic/Latino | 636 |
| Bachelor's or higher | 3542 |

## Districts

- [MS-02](/us/states/ms/districts/02.md) — 100% (congressional)
- [MS Senate District 12](/us/states/ms/districts/senate/12.md) — 75% (state senate)
- [MS Senate District 11](/us/states/ms/districts/senate/11.md) — 25% (state senate)
- [MS House District 26](/us/states/ms/districts/house/26.md) — 73% (state house)
- [MS House District 9](/us/states/ms/districts/house/9.md) — 26% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
