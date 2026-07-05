---
type: Jurisdiction
title: "Morehouse Parish, LA"
classification: county
fips: "22067"
state: "LA"
demographics:
  population: 24551
  population_under_18: 5661
  population_18_64: 13962
  population_65_plus: 4928
  median_household_income: 39454
  poverty_rate: 29.28
  homeownership_rate: 68.56
  unemployment_rate: 9.42
  median_home_value: 118800
  gini_index: 0.5182
  vacancy_rate: 17.89
  race_white: 11641
  race_black: 11874
  race_asian: 66
  race_native: 17
  hispanic: 419
  bachelors_plus: 3165
districts:
  - to: "us/states/la/districts/05"
    rel: in-district
    area_weight: 0.9973
  - to: "us/states/la/districts/senate/33"
    rel: in-district
    area_weight: 0.7634
  - to: "us/states/la/districts/senate/34"
    rel: in-district
    area_weight: 0.2364
  - to: "us/states/la/districts/house/19"
    rel: in-district
    area_weight: 0.8601
  - to: "us/states/la/districts/house/16"
    rel: in-district
    area_weight: 0.1395
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Morehouse Parish, LA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 24551 |
| Under 18 | 5661 |
| 18–64 | 13962 |
| 65+ | 4928 |
| Median household income | 39454 |
| Poverty rate | 29.28 |
| Homeownership rate | 68.56 |
| Unemployment rate | 9.42 |
| Median home value | 118800 |
| Gini index | 0.5182 |
| Vacancy rate | 17.89 |
| White | 11641 |
| Black | 11874 |
| Asian | 66 |
| Native | 17 |
| Hispanic/Latino | 419 |
| Bachelor's or higher | 3165 |

## Districts

- [LA-05](/us/states/la/districts/05.md) — 100% (congressional)
- [LA Senate District 33](/us/states/la/districts/senate/33.md) — 76% (state senate)
- [LA Senate District 34](/us/states/la/districts/senate/34.md) — 24% (state senate)
- [LA House District 19](/us/states/la/districts/house/19.md) — 86% (state house)
- [LA House District 16](/us/states/la/districts/house/16.md) — 14% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
